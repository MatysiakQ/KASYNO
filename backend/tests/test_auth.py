from datetime import UTC, datetime, timedelta

from fastapi.testclient import TestClient
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import token_digest
from app.modules.auth.models import LoginSession
from app.modules.users.models import User

CREDS = {"email": "lukasz@example.com", "password": "test-password-long-enough"}


def signup_and_login(client: TestClient) -> str:
    response = client.post("/api/v1/auth/register", json=CREDS)
    assert response.status_code == 201
    assert "password_hash" not in response.json()
    response = client.post("/api/v1/auth/login", json=CREDS)
    assert response.status_code == 200
    assert response.headers["cache-control"] == "no-store"
    return str(response.json()["access_token"])


def test_session_lifecycle(client: TestClient, db: Session) -> None:
    token = signup_and_login(client)
    session = db.scalar(select(LoginSession))
    assert session is not None and session.token_hash == token_digest(token)
    user = db.scalar(select(User))
    assert user is not None and user.password_hash != CREDS["password"]
    headers = {"Authorization": f"Bearer {token}"}
    assert client.get("/api/v1/users/me", headers=headers).json()["email"] == CREDS["email"]
    assert client.post("/api/v1/auth/logout", headers=headers).status_code == 204
    assert client.get("/api/v1/users/me", headers=headers).status_code == 401
    assert client.post("/api/v1/auth/logout", headers=headers).status_code == 204


def test_duplicate_and_bad_credentials(client: TestClient) -> None:
    signup_and_login(client)
    assert (
        client.post(
            "/api/v1/auth/register", json={**CREDS, "email": "LUKASZ@example.com"}
        ).status_code
        == 409
    )
    assert (
        client.post(
            "/api/v1/auth/login", json={**CREDS, "password": "wrong-password-long"}
        ).status_code
        == 401
    )
    assert (
        client.post(
            "/api/v1/auth/login", json={**CREDS, "email": "unknown@example.com"}
        ).status_code
        == 401
    )
    assert client.get("/api/v1/users/me").status_code == 401
    assert (
        client.get("/api/v1/users/me", headers={"Authorization": "Bearer invalid"}).status_code
        == 401
    )


def test_expired_session(client: TestClient, db: Session) -> None:
    token = signup_and_login(client)
    session = db.scalar(select(LoginSession))
    assert session is not None
    session.expires_at = datetime.now(UTC) - timedelta(seconds=1)
    db.commit()
    assert (
        client.get("/api/v1/users/me", headers={"Authorization": f"Bearer {token}"}).status_code
        == 401
    )


def test_disabled_user(client: TestClient, db: Session) -> None:
    token = signup_and_login(client)
    user = db.scalar(select(User))
    assert user is not None
    user.is_active = False
    db.commit()
    assert (
        client.get("/api/v1/users/me", headers={"Authorization": f"Bearer {token}"}).status_code
        == 401
    )
    assert client.post("/api/v1/auth/login", json=CREDS).status_code == 401


def test_validation_and_health(client: TestClient) -> None:
    assert (
        client.post(
            "/api/v1/auth/register", json={"email": "invalid", "password": "short"}
        ).status_code
        == 422
    )
    assert client.get("/health/live").json() == {"status": "ok"}
    assert client.get("/openapi.json").status_code == 200

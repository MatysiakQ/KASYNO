import secrets
from datetime import UTC, datetime, timedelta

from fastapi import HTTPException
from sqlalchemy import delete
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.security import DUMMY_HASH, token_digest, verify_password
from app.modules.auth.models import LoginSession
from app.modules.auth.schemas import TokenRead
from app.modules.users.repository import find_by_email
from app.modules.users.schemas import Credentials


def login(db: Session, data: Credentials) -> TokenRead:
    user = find_by_email(db, str(data.email))
    valid = verify_password(data.password, user.password_hash if user else DUMMY_HASH)
    if not valid or user is None or not user.is_active:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = secrets.token_urlsafe(32)
    ttl = get_settings().session_ttl_seconds
    db.add(
        LoginSession(
            token_hash=token_digest(token),
            user_id=user.id,
            expires_at=datetime.now(UTC) + timedelta(seconds=ttl),
        )
    )
    db.commit()
    return TokenRead(access_token=token, expires_in=ttl)


def logout(db: Session, token: str) -> None:
    db.execute(delete(LoginSession).where(LoginSession.token_hash == token_digest(token)))
    db.commit()

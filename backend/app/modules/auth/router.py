from fastapi import APIRouter, Response

from app.modules.auth.dependencies import Db, Token
from app.modules.auth.schemas import TokenRead
from app.modules.auth.service import login, logout
from app.modules.users.schemas import Credentials, UserRead
from app.modules.users.service import register

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserRead, status_code=201)
def register_user(data: Credentials, db: Db) -> UserRead:
    return UserRead.model_validate(register(db, data))


@router.post("/login", response_model=TokenRead)
def login_user(data: Credentials, db: Db, response: Response) -> TokenRead:
    response.headers["Cache-Control"] = "no-store"
    return login(db, data)


@router.post("/logout", status_code=204)
def logout_user(db: Db, token: Token) -> Response:
    logout(db, token)
    return Response(status_code=204)

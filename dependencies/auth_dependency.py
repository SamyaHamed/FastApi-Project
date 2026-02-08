from fastapi import Depends, HTTPException, status
from models.User import User
from core.security import decode_access_token, oauth2_scheme
from repositories.user_repository import UserRepository


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
) -> User:

    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception

    user_id: int | None = payload.get("user_id")
    if user_id is None:
        raise credentials_exception

    user = UserRepository.get_by_id(user_id)
    if user is None:
        raise credentials_exception

    return user



from datetime import datetime , timedelta , timezone
from jose import JWTError, jwt
from typing import Optional
from core.config import settings
from app_enums.UserRole import UserRole


def create_access_token(
    user_id: int,
    role: UserRole,
    expires_delta: Optional[timedelta] = None
    ) -> str:

    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    payload = {
        "sub": str(user_id),               
        "role": role.value,                      
        "type": "access",                 
        "iat": datetime.now(timezone.utc),
        "exp": expire
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def decode_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        if payload.get("type") != "access":
            return None

        user_id = payload.get("sub")
        role = payload.get("role")

        if user_id is None or role is None:
            return None

        return {
            "user_id": int(user_id),
            "role": UserRole(role)
        }

    except JWTError:
        return None


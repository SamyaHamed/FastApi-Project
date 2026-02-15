import bcrypt


class Hashing:

    @staticmethod
    def hash_pass(password: str) -> str:
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        return hashed.decode("utf-8")

    @staticmethod
    def verify_pass(plain_password: str, hashed_password: str) -> bool:
        plain_password = plain_password.encode("utf-8")
        hashed_password = hashed_password.encode("utf-8")
        return bcrypt.checkpw(plain_password, hashed_password)

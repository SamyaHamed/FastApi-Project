from sqlalchemy.orm import Session
from abc import ABC , abstractmethod

class SignUpStrategy(ABC):

    @abstractmethod
    def execute(self, db: Session, data):
        pass


from sqlalchemy import Column,String,ForeignKey,Integer,Enum
from sqlalchemy.orm import relationship 
from database.data import Base
from app_enums.UserRole import UserRole  


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key= True)
    email = Column(String(50),nullable= False,unique=True)
    password = Column(String(255),nullable = False)
    role = Column(Enum(UserRole),nullable=False)

    company = relationship("Company",back_populates="user", uselist=False ,cascade="all, delete-orphan")
    trainee = relationship("Trainee",back_populates="user",uselist=False ,cascade="all, delete-orphan")




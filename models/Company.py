from sqlalchemy import Column,Integer,String,ForeignKey
from database.data import Base
from sqlalchemy.orm import relationship

class Company(Base) :
    __tablename__ = "companies"
    id = Column(Integer,primary_key= True)
    name = Column(String(30),nullable = False)
    city = Column(String(30),nullable= False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=True)
    user = relationship("User", back_populates="company")

    internships = relationship("Internship",back_populates="company")

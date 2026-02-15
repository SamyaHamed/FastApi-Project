from sqlalchemy import Integer,String,Enum,ForeignKey,Column
from sqlalchemy.orm import relationship
from database.data import Base

class Internship(Base):
    __tablename__ = "internships"
    id = Column(Integer , primary_key= True)
    name = Column(String(30),nullable= False)

    company_id = Column(Integer,ForeignKey("companies.id"),nullable=False)
    company = relationship("Company", back_populates = "internships")
    applications = relationship("Application",back_populates="internship")



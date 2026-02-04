from sqlalchemy import Integer,Column,DateTime,ForeignKey,Enum,UniqueConstraint
from sqlalchemy.orm import relationship
from database.data import Base
from datetime import datetime
from app_enums import ApplicationStatus
from models.Internship import Internship

class Application(Base):
    __tablename__ = "applications"

    __table_args__ = (
        UniqueConstraint(
            "trainee_id",
            "internship_id",
            name="uq_trainee_internship"
        ),
    )

    id = Column(Integer,primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(Enum(ApplicationStatus), default=ApplicationStatus.pending ,nullable=False)

    trainee_id = Column(Integer,ForeignKey("trainees.id"),nullable= False)
    trainee = relationship("Trainee",back_populates="applications")

    internship_id  = Column(Integer,ForeignKey("internships.id"),nullable=False)
    internship = relationship("Internship",back_populates="applications")








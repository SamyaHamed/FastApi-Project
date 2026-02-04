from sqlalchemy import Integer,Column,String,ForeignKey,Table , UniqueConstraint
from sqlalchemy.orm import relationship
from database.data import Base

trainee_skills = Table (
    "trainee_skills",
    Base.metadata,
    Column("trainee_id", Integer, ForeignKey("trainees.id"), primary_key=True),
    Column("skill_id",Integer,ForeignKey("skills.id"), primary_key = True),
    UniqueConstraint("trainee_id","skill_id", name="uq_trainee_skill")

)
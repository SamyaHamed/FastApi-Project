from database.data import engine, Base

from models.Trainee import Trainee
from models.TraineeProfile import TraineeProfile
from models.Skill import Skill
from models.Company import Company
from models.Internship import Internship
from models.Application import Application
from models.associations import trainee_skills  
from models.User import User

def create_tables():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Done creating tables")



if __name__ == "__main__":
    create_tables()
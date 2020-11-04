from faker import Faker
from db import models
from db.database import engine, SessionLocal
from run_db import generate_migration


faker = Faker()
db = SessionLocal()



def generate_data():

    # Employee list
    for i in range(100):
        db_employee = models.Employee(name=faker.name(), email=faker.email(), password=faker.name(), salary=100)
        db.add(db_employee)
    db.commit()
    

if __name__ == "__main__":
    generate_migration()
    generate_data()
from typing import List
from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
# from basic_crud.user_dao import get_user_data, get_user_by_id, add_user
# from basic_crud.models import User
from app import schemas
from app.crud import employee_crud
from db import models
from db.database import engine, SessionLocal


router = APIRouter()

# CRUD using SQLAlchemy ORM
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db = 1
        # db.close()



@router.post('/add-employee')
def add_employee(employee: schemas.Employee, db: Session = Depends(get_db)):
    return employee_crud.create_employee(employee=employee, db=db)


@router.get('/get-employee/{employee_id}', response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = employee_crud.get_employee(db=db, employee_id=employee_id)
    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found!"
        )
    return employee

@router.get('/get-employee', response_model=List[schemas.Employee])
def read_employee_all(db: Session = Depends(get_db)):
    employees = employee_crud.get_employees_all(db=db)
    return employees

@router.delete('/delete-employee/{employee_id}')
def remove_employee(employee_id: int, db: Session = Depends(get_db)):
    affected_rows = employee_crud.delete_employee(employee_id=employee_id, db=db)
    status_code = 200
    msg = "Deleted Successfully"
    if affected_rows == 0:
        status_code = 404
        msg = "Employee not found"

    raise HTTPException(
        status_code=status_code,
        detail=msg
    )



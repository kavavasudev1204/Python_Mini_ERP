from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from app.core.security import get_password_hash

router = APIRouter()

@router.post("/employees/", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    # 1. Check if email already exists
    db_user = db.query(Employee).filter(Employee.email == employee.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 2. Hash the password
    hashed_pwd = get_password_hash(employee.password)

    # 3. Create the database object
    new_employee = Employee(
        email=employee.email,
        hashed_password=hashed_pwd,
        full_name=employee.full_name,
        role=employee.role
    )

    # 4. Add to DB and commit
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    
    return new_employee
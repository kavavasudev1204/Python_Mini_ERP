from pydantic import BaseModel, EmailStr
from typing import Optional

# Base schema with shared properties
class EmployeeBase(BaseModel):
    email: EmailStr
    full_name: str
    role: str = "staff"
    department_id: Optional[int] = None

# Schema for creating a user (includes password)
class EmployeeCreate(EmployeeBase):
    password: str

# Schema for reading a user (excludes password for security)
class EmployeeResponse(EmployeeBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
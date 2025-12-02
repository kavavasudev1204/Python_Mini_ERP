from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=False)
    role = Column(String(50), default="staff")  # Options: 'admin', 'staff', 'hr'
    is_active = Column(Boolean, default=True)
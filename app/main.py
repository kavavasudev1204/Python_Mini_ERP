from fastapi import FastAPI
from app.core.database import engine
from app.models import employee
from app.routers import employees, auth

# Create the database tables
employee.Base.metadata.create_all(bind=engine)

# --- THIS IS THE MISSING PART ---
app = FastAPI(title="Mini ERP System")
# --------------------------------

@app.get("/")
def health_check():
    return {"status": "System is active", "database": "Connected"}
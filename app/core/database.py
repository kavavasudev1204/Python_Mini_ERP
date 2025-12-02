from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus  # We need this to handle the '@' in your password

# 1. Your Password
password_raw = "Vasudev@1204"

# 2. Encode the password
# This converts 'Vasudev@1204' into 'Vasudev%401204' so the database driver can read it
password_encoded = quote_plus(password_raw)

# 3. Construct the URL
# FORMAT: mysql+mysqlconnector://<user>:<encoded_password>@<host>/<db_name>
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://root:{password_encoded}@localhost/minierp"

# 4. Create the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 5. Create SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 6. Base class
Base = declarative_base()

# 7. Dependency for API routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# MySQL Database URL
DATABASE_URL = "mysql+pymysql://avnadmin:YOUR_PASSWORD@mysql-23b344f4-bike-showroom.k.aivencloud.com:25225/defaultdb"


# Create Engine
engine = create_engine(
    DATABASE_URL,
    echo=True
)


# Create Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base Class
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

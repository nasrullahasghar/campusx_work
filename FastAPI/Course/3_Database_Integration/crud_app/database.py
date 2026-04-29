from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the Data Base file
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create the Data Base  connection
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args= {"check_same_thread":False}
)
# Create the Datas Base Session 
SessionLocal = sessionmaker(bind=engine , autoflush=False , autocommit=False)

# Connects with pythoin
Base = declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+psycopg2://user:pass@db:5432/python_flash_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db():
    from models import LearningTopic, HistoricalAcceptance, FlashCard
    Base.metadata.create_all(bind=engine)

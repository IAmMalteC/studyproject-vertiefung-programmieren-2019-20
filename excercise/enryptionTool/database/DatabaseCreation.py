from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .databasemodel import Base  # import the databasemodel


def create_database():
    database = 'sqlite:///database/datalog.db'
    engine = create_engine(database)
    Base.metadata.create_all(engine)
    return engine


def open_session(engine):
    temporary_session = sessionmaker(engine)
    session = temporary_session()
    return session




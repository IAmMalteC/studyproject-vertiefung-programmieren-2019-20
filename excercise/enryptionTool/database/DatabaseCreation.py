from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# import the databasemodel
from .databasemodel import Base


def create_database():
    database = 'sqlite:///database/datalog.db'
    engine = create_engine(database)
    Base.metadata.create_all(engine)
    return engine


def open_session(engine):
    Session = sessionmaker(engine)
    session = Session()
    return session




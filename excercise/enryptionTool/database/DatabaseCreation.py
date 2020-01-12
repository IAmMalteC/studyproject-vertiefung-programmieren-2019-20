from sqlalchemy.orm import sessionmaker
# relationship is used to connect the FK
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
# import the databasemodel
from .databasemodel import Base, User_TB, EncryptionType_TB, EncodedString_TB


def create_database():
    database = 'sqlite:///database/datalog.db'
    engine = create_engine(database)
    # Creates the relationships with the foreignkey
    User_TB.encrypted_string = relationship("EncodedString", order_by=EncodedString_TB.id, back_populates="userstr")
    EncryptionType_TB.encrypted_string = relationship("EncodedString", order_by=EncodedString_TB.id, back_populates="encryptiontyperelation")

    Base.metadata.create_all(engine)
    return engine


def open_session(engine):
    Session = sessionmaker(engine)
    session = Session()
    return session




from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def create_database():
    database = 'sqlite:///database/datalog.db'
    engine = create_engine(database)
    Base.metadata.create_all(engine)
    return engine


def open_session(engine):
    Session = sessionmaker(engine)
    session = Session()
    return session


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)

    # add to the others ? !Attention!
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "User [id: {0}, name: {1}]".format(self.id, self.name)


class EncryptionType(Base):
    __tablename__ = 'encryption_type'
    id = Column(Integer, primary_key=True)
    type = Column(String(30), nullable=False, unique=True)


class EncryptedString(Base):
    __tablename__ = 'encrypted_string'
    id = Column(Integer, primary_key=True)
    string = Column(String(256), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    encryption_type_id = Column(Integer, ForeignKey(EncryptionType.id), nullable=False)


class CesarEncryption(Base):
    __tablename__ = 'cesar_encryption'
    id = Column(Integer, ForeignKey(EncryptionType.id), primary_key=True)
    offset = Column(Integer)


class MonoAlphabeticSubstitution(Base):
    __tablename__ = 'mono_alphabetic_substitution'
    id = Column(Integer, ForeignKey(EncryptionType.id), primary_key=True)
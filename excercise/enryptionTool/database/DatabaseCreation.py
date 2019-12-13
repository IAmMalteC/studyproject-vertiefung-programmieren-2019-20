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

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "User [ID: {0}, name: {1}]".format(self.id, self.name)


class EncryptionType(Base):
    __tablename__ = 'encryption_type'
    id = Column(Integer, primary_key=True)
    type = Column(String(30), nullable=False, unique=True)

    def __init__(self, type: str):
        self.type = type

    def __repr__(self):
        return "Type of Encryption [ID: {0}, Type: {1}]".format(self.id, self.type)


class EncryptedString(Base):
    __tablename__ = 'encrypted_string'
    id = Column(Integer, primary_key=True)
    string = Column(String(256), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    encryption_type_id = Column(Integer, ForeignKey(EncryptionType.id), nullable=False)

    def __init__(self, string: str, user: int, encryption_type: int):
        self.string = string
        self.user_id = user
        self.encryption_type_id = encryption_type

    def __repr__(self):
        return "Encryptedstring [ID: {0}, String: {1}]".format(self.id, self.string)


class CesarEncryption(Base):
    __tablename__ = 'cesar_encryption'
    id = Column(Integer, ForeignKey(EncryptionType.id), primary_key=True)
    offset = Column(Integer)

    def __init__(self, offset: int):
        self.offset = offset

    def __repr__(self):
        return "Cesar:[ID: {0}, Offset: {1}]".format(self.id, self.offset)


class MonoAlphabeticSubstitution(Base):
    __tablename__ = 'mono_alphabetic_substitution'
    id = Column(Integer, ForeignKey(EncryptionType.id), primary_key=True)

    # def __init__(self, id: int):
    #     self.id = id

    def __repr__(self):
        return "MonoAlphabetic: [ID: {0}]".format(self.id)
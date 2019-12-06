from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from encryption.Cesar import Cesar
from encryption.MonoAlphabetic import MonoAlphabetic


def __menu__():
    print('ENCRYPTION TOOL\n1 : Cesar encryption\n2 : Mono alphabetic substitution\n3 : About\n4 : Quit program')

    while True:
        text = input('Please choose a value and press Enter:')
        # Cesar Encryption
        if text == '1':
            Cesar()
        # Mono alphabetic substitution
        elif text == '2':
            MonoAlphabetic()
        # About page
        elif text == '3':
            print('This is a basic encryption tool')
        # Quit program
        elif text == '4' or text == "exit":
            print('Goodbye')
            break
        else:
            print('You choose a non-valid value.\nPlease try again.')


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)


class EncryptionType(Base):
    __tablename__ = 'encryption_type'
    id = Column(Integer, primary_key=True)
    type = Column(String(30), nullable=False)


class EncryptedString(Base):
    __tablename__ = 'encrypted_string'
    id = Column(Integer, primary_key=True)
    string = Column(String(256), nullable=False)
    user_id = Column(Integer, ForeignKey("user.user_id"), nullable=False)
    encryption_type_id = Column(Integer, ForeignKey("encryption_type.encryption_type.id"), nullable=False)

class CesarEncryption(Base):
    __tablename__ = 'cesar_encryption'
    id = Column(Integer, primary_key=True)
    offset = Column(Integer)


class MonoAlphabeticSubstitution(Base):
    __tablename__ = 'mono_alphabetic_substitution'
    id = Column(Integer, primary_key=True)


if __name__ == "__main__":
    database = 'sqlite:///database/datalog.db'
    Base.metadata.create_all(database)
    engine = create_engine(database)
    __menu__()

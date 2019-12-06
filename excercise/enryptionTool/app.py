from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import string
from encryption.Cesar import Cesar
from encryption.MonoAlphabetic import MonoAlphabetic


def __startup__(db_session):
    print('LOGIN')
    username = input('Please enter your Username: ').lower()
    user = User(username)
    # checks if the user already exists (Wraps a .exists() query in another session.query()
    # with a scalar() call at the end.
    exists = db_session.query(db_session.query(User).filter_by(name=username).exists()).scalar()
    if exists is False:
        db_session.add(user)
        db_session.commit()
    else:
        user = db_session.query(User).filter_by(name=username).first()

    # Welcome message
    print("Welcome " + User.__repr__(user))


def __menu__():
    # list which defines the scope of values
    list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    while True:
        print('ENCRYPTION TOOL\n1 : Cesar encryption\n2 : Mono alphabetic substitution\n3 : About\n4 : Quit program')

        text = input('Please choose a value and press Enter: ')
        # Cesar Encryption
        if text == '1':
            Cesar(list_of_characters)
        # Mono alphabetic substitution
        elif text == '2':
            MonoAlphabetic(list_of_characters)
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


if __name__ == "__main__":
    # Database creation
    database = 'sqlite:///database/datalog.db'
    engine = create_engine(database)
    # Creates Tables
    Base.metadata.create_all(engine)
    # Opens Session
    Session = sessionmaker(engine)
    session = Session()

    # starts login process
    __startup__(session)

    # opens the menu
    __menu__()

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .databasemodel import Base  # import the databasemodel
from database.databasemodel import MonoAlphabeticSubstitutionTB, CesarTB, EncodedStringTB, EncryptionTypeTB, UserTB


# Creating connection
def create_database_connection():
    engine = create_database()
    global session
    session = open_session(engine)


def create_database():
    database = 'sqlite:///database/datalog.db'
    engine = create_engine(database)
    Base.metadata.create_all(engine)

    return engine


def open_session(engine):
    temporary_session = sessionmaker(engine)
    created_session = temporary_session()

    return created_session


# Saves input to the Database
def save_user_check_exists(name):
    current_user = UserTB(name)  # The password value is not used in the console app

    # checks if the user already exists (Wraps a .exists() query in another session.query() with a scalar() call at the end.
    exists = session.query(session.query(UserTB).filter_by(user_name=name).exists()).scalar()
    if exists is False:
        session.add(current_user)
        session.commit()
    else:
        current_user = session.query(UserTB).filter_by(user_name=name).first()

    return current_user # Returns the value to welcome the current user


def save_cesar(offsetvalue):
    cesar = CesarTB(offsetvalue)
    session.add(cesar)
    session.commit()


def save_monoalphabetic():
    monoalphabetic = MonoAlphabeticSubstitutionTB()
    session.add(monoalphabetic)
    session.commit()


def save_encryptedstring(output, username, encrytpiontype):
    current_user = session.query(UserTB).filter(UserTB.user_name == username).first()
    # Gets the latest encryption type
    encryption = session.query(EncryptionTypeTB).filter(EncryptionTypeTB.encryption_type_type == encrytpiontype).order_by(EncryptionTypeTB.encryption_type_id.desc()).first()
    # the saving
    encodestring = EncodedStringTB(output, current_user.user_id, encryption.encryption_type_id)
    session.add(encodestring)
    session.commit()
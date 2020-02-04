from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# Import the databasemodel
from .databasemodel import Base
from database.databasemodel import MonoAlphabeticSubstitutionTB, CesarTB, EncodedStringTB, EncryptionTypeTB, UserTB


def create_database_connection():
    """ Create a connection to our database """
    engine = create_database()
    global session
    session = open_session(engine)


def create_database():
    """ Defines where the database is created

    :returns engine
    """
    database = 'sqlite:///database/datalog.db'
    engine = create_engine(database)
    Base.metadata.create_all(engine)

    return engine


def open_session(engine):
    """ Open a session to the database

    :returns created_session
    """
    temporary_session = sessionmaker(engine)
    created_session = temporary_session()

    return created_session


def save_user_check_exists(name):
    """ Save the user to the Database,
     but before it checks if the user already is existing.
     The password value is not used in the console app

     :returns current_user
     """
    current_user = UserTB(name)  #

    # checks if the user already exists
    # (Wraps a .exists() query in another session.query() with a scalar() call at the end.
    exists = session.query(session.query(UserTB).filter_by(user_name=name).exists()).scalar()
    if exists is False:
        session.add(current_user)
        session.commit()
    else:
        current_user = session.query(UserTB).filter_by(user_name=name).first()

    # Returns the value to welcome the current user
    return current_user


def save_cesar(offsetvalue):
    """ Save the encryptiontype Cesar to the Database """
    cesar = CesarTB(offsetvalue)
    session.add(cesar)
    session.commit()


def save_monoalphabetic():
    """ Save the encryptiontype monoalphabetic to the Database """
    monoalphabetic = MonoAlphabeticSubstitutionTB()
    session.add(monoalphabetic)
    session.commit()


def save_encryptedstring(output, username):
    """ Save the encryptedstring to the database
    The encryptiontype is not important,
    because always the last saved is used.
    """
    # Get the current user via username
    current_user = session.query(UserTB).filter(UserTB.user_name == username).first()
    # Gets the latest used encryption type, which is used for this string.
    encryption = session.query(EncryptionTypeTB)\
        .order_by(EncryptionTypeTB.encryption_type_id.desc())\
        .first()

    # Saves the string
    encodestring = EncodedStringTB(output, current_user.user_id, encryption.encryption_type_id)
    session.add(encodestring)
    session.commit()

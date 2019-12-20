from database import DatabaseCreation
from database.DatabaseCreation import MonoAlphabeticSubstitution, Cesar, EncodedString, EncryptionType, User


class InsertIntoDatabase(object):
    def __init__(self):
        engine = DatabaseCreation.create_database()
        global session
        session = DatabaseCreation.open_session(engine)

    def insert_user_check_exists(self, value):
        user = DatabaseCreation.User(value)

        # checks if the user already exists (Wraps a .exists() query in another session.query()
        # with a scalar() call at the end.
        exists = session.query(session.query(DatabaseCreation.User).filter_by(name=value).exists()).scalar()
        if exists is False:
            session.add(user)
            session.commit()
        else:
            user = session.query(DatabaseCreation.User).filter_by(name=value).first()
        return user


def insert_cesar(offsetvalue):
    cesar = Cesar(offsetvalue)
    session.add(cesar)
    session.commit()


def insert_monoalphabetic():
    monoalphabetic = MonoAlphabeticSubstitution()
    session.add(monoalphabetic)
    session.commit()


def insert_encryptedstring(output, username, encrytpiontype):
    user = session.query(User).filter(User.name == username).first()
    # to get the latest encryption type
    encryption = session.query(EncryptionType).filter(EncryptionType.type == encrytpiontype).order_by(EncryptionType.id.desc()).first()
    # the saving
    encodestring = EncodedString(output, user.id, encryption.id)
    session.add(encodestring)
    session.commit()
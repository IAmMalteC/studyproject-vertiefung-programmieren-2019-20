from database import DatabaseCreation
from database.databasemodel import MonoAlphabeticSubstitution_TB, Cesar_TB, EncodedString_TB, EncryptionType_TB, User_TB


class InsertIntoDatabase(object):
    def __init__(self):
        engine = DatabaseCreation.create_database()
        global session
        session = DatabaseCreation.open_session(engine)

    def insert_user_check_exists(self, value):
        user = DatabaseCreation.User_TB(value)

        # checks if the user already exists (Wraps a .exists() query in another session.query()
        # with a scalar() call at the end.
        exists = session.query(session.query(DatabaseCreation.User_TB).filter_by(name=value).exists()).scalar()
        if exists is False:
            session.add(user)
            session.commit()
        else:
            user = session.query(DatabaseCreation.User_TB).filter_by(name=value).first()
        return user


def insert_cesar(offsetvalue):
    cesar = Cesar_TB(offsetvalue)
    session.add(cesar)
    session.commit()


def insert_monoalphabetic():
    monoalphabetic = MonoAlphabeticSubstitution_TB()
    session.add(monoalphabetic)
    session.commit()


def insert_encryptedstring(output, username, encrytpiontype):
    user = session.query(User_TB).filter(User_TB.name == username).first()
    # to get the latest encryption type
    encryption = session.query(EncryptionType_TB).filter(EncryptionType_TB.type == encrytpiontype).order_by(EncryptionType_TB.id.desc()).first()
    # the saving
    encodestring = EncodedString_TB(output, user.id, encryption.id)
    session.add(encodestring)
    session.commit()
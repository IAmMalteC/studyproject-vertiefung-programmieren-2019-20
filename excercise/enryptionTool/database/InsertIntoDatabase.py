from database import DatabaseCreation


def insert_user_check_exists(db_session, value):
    user = DatabaseCreation.User(value)

    # checks if the user already exists (Wraps a .exists() query in another session.query()
    # with a scalar() call at the end.
    exists = db_session.query(db_session.query(DatabaseCreation.User).filter_by(name=value).exists()).scalar()
    if exists is False:
        db_session.add(user)
        db_session.commit()
    else:
        user = db_session.query(DatabaseCreation.User).filter_by(name=value).first()
    return user


def insert_encoding_type(db_session, value):
    encodingtype = DatabaseCreation.EncodingType(value)
    # checks if the user already exists (Wraps a .exists() query in another session.query()
    # with a scalar() call at the end.
    exists = db_session.query(db_session.query(DatabaseCreation.EncodingType).filter_by(type=value).exists()).scalar()
    if exists is False:
        db_session.add(encodingtype)
        db_session.commit()


def insert_cesar(db_session, offsetvalue, encodingtype):
    cesar = DatabaseCreation.Cesar(offsetvalue, encodingtype)
    db_session.add(cesar)
    db_session.commit()


def insert_monoalphabetic(db_session, encodingtype):
    monoalphabetic = DatabaseCreation.MonoAlphabeticSubstitution(encodingtype)
    db_session.add(monoalphabetic)
    db_session.commit()


def insert_encodedstring(db_session, string, userid, encodingtype):
    encodestring = DatabaseCreation.EncodedString(string, userid, encodingtype)
    db_session.add(encodestring)
    db_session.commit()
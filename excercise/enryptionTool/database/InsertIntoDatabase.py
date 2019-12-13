from database import DatabaseCreation


def insert_encryption_type(db_session, value):
    new_data_base_input = DatabaseCreation.EncryptionType(value)
    # checks if the user already exists (Wraps a .exists() query in another session.query()
    # with a scalar() call at the end.
    exists = db_session.query(db_session.query(DatabaseCreation.EncryptionType).filter_by(type=value).exists()).scalar()
    if exists is False:
        db_session.add(new_data_base_input)
        db_session.commit()


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


class InsertIntoDatabase:
    # def __init__(self):
    #     return self

    pass
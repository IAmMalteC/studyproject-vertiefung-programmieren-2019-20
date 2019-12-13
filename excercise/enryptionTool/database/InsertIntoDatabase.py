import database
from sqlalchemy.orm import sessionmaker


def insert_user_check_exists(db_session, value):
    user = database.DatabaseCreation.User(value)

    # checks if the user already exists (Wraps a .exists() query in another session.query()
    # with a scalar() call at the end.
    exists = db_session.query(db_session.query(database.DatabaseCreation.User).filter_by(name=value).exists()).scalar()
    if exists is False:
        db_session.add(user)
        db_session.commit()
    else:
        user = db_session.query(database.DatabaseCreation.User).filter_by(name=value).first()
    return user


class InsertIntoDatabase:
    # def __init__(self):
    #     return self

    pass
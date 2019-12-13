import string
from database import DatabaseCreation, InsertIntoDatabase
from encryption.Cesar import Cesar
from encryption.MonoAlphabetic import MonoAlphabetic


def __startup__(db_session):
    # Saves the possible types of encryption
    InsertIntoDatabase.insert_encryption_type(db_session, 'Cesar')
    InsertIntoDatabase.insert_encryption_type(db_session, 'MonoAlphabetic')

    print('LOGIN')
    username = input('Please enter your Username: ').lower()
    user = InsertIntoDatabase.insert_user_check_exists(db_session, username)
    # Welcome message
    print("Welcome " + DatabaseCreation.User.__repr__(user))


def __menu__(db_session):
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


if __name__ == "__main__":
    # Database creation and create Tables
    engine = DatabaseCreation.create_database()
    session = DatabaseCreation.open_session(engine)

    # starts login process
    __startup__(session)

    # opens the menu
    __menu__(session)

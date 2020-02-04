"""
This is the console app
"""
import string
from database import databasemodel
from database.saves_to_database import save_user_check_exists, create_database_connection
from encryption.Cesar import Cesar
from encryption.MonoAlphabetic import MonoAlphabetic

# list which defines the scope of values
list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


def __startup__():
    print('LOGIN')
    current_username = input('Please enter your username: ').lower()
    create_database_connection()
    user = save_user_check_exists(current_username)
    print("Welcome " + databasemodel.UserTB.__repr__(user))  # Welcome message
    
    return current_username


def __menu__(current_username):
    while True:
        print('ENCRYPTION TOOL\n1 : Cesar encryption\n2 : Mono alphabetic substitution\n3 : About\n4 : Quit program')

        text = input('Please choose a value and press \"Enter\": ')
        # Cesar Encryption
        if text == '1':
            Cesar(current_username, list_of_characters)
        # Mono alphabetic substitution
        elif text == '2':
            MonoAlphabetic(current_username, list_of_characters)
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
    # starts login process
    username = __startup__()

    # opens the menu
    __menu__(username)

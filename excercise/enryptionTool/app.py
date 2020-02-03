# This is the console app
import string
from database import databasemodel, SavesToDatabase
from database.SavesToDatabase import SavesToDatabase
from encryption.Cesar import Cesar
from encryption.MonoAlphabetic import MonoAlphabetic

# list which defines the scope of values
list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


def __startup__():
    print('LOGIN')
    username = input('Please enter your Username: ').lower()
    #password = input("Please enter your password: ")
    insertIntoDatabase = SavesToDatabase()
    user = insertIntoDatabase.insert_user_check_exists(username)#, password)
    # Welcome message
    print("Welcome " + databasemodel.UserTB.__repr__(user))
    return username


def __menu__(username):
    while True:
        print('ENCRYPTION TOOL\n1 : Cesar encryption\n2 : Mono alphabetic substitution\n3 : About\n4 : Quit program')

        text = input('Please choose a value and press Enter: ')
        # Cesar Encryption
        if text == '1':
            Cesar(username, list_of_characters)
        # Mono alphabetic substitution
        elif text == '2':
            MonoAlphabetic(username, list_of_characters)
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

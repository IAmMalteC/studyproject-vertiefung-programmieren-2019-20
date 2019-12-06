"""from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker"""
from sqlalchemy import create_engine
import sqlite3 as lite
from sqlite3 import Error
from encryption.Cesar import Cesar
from encryption.Monoalphabetic import Monoalphabetic


'''def create_connection(db_file):
    """ create a database connection to a SQLite database """
    connection = None
    try:
        connection = lite.connect(db_file)
        print(lite.version)
    except Error as e:
        print(e)
    finally:
        if connection:
            connection.close()
'''

def __menu__():
    print('ENCRYPTION TOOL\n1 : Cesar encryption\n2 : Mono alphabetic substitution\n3 : About\n4 : Quit program')

    while True:
        text = input('Please choose a value and press Enter:')
        # Cesar Encryption
        if text == '1':
            Cesar()
        # Mono alphabetic substitution
        elif text == '2':
            Monoalphabetic()
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
    engine = create_engine("sqlite://database/datalog.db", echo = True) #= r"./database/datalog.db"
    #create_connection(database)
    __menu__()

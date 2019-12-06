from userinput import offset
from encryption.Cesar import Cesar
from encryption.Monoalphabetic import Monoalphabetic

print('ENCRYPTION TOOL\n1 : Cesar encryption\n2 : Mono alphabetic substitution\n3 : About\n4 : Quit program')

while True:
    text = input('Please choose a value and press Enter:')
    # Cesar Encryption
    if text == '1':
        Cesar()
    # Mono alphatic substition
    elif text == '2':
        Monoalphabetic()
    # About page
    elif text == '3':
        print('This is a basic encryption tool')
    # Quit programm
    elif text == '4' or text == "exit":
        print('Goodbye')
        break
    else:
        print('You choose a non-valid value.\nPlease try again.')

import string


class Monoalphabetic:
    def __init__(self):
        print('You are using the Monoalphabetic encryption')

        output=''
        listOfCharacters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        listOfCharactersReverse = listOfCharacters
        listOfCharactersReverse[::-1]

        while (True):
            textFromUser = input('Type the text you want to encrypt:')

            for letter in textFromUser:
                output = output + self.encrypter(letter, listOfCharacters, listOfCharactersReverse)

            print(output)
            output = ''

    def encrypter(self):
        pass
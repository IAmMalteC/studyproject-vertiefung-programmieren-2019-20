import string


class Monoalphabetic:
    def __init__(self):
        print('You are using the Monoalphabetic encryption')

        output = ''
        listOfCharacters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        listOfCharactersReverse = self.reverse_text(listOfCharacters)

        while(True):
            textFromUser = input('Type the text you want to encrypt:')

            for letter in textFromUser:
                output = output + self.encrypter(letter, listOfCharacters, listOfCharactersReverse)

            print(output)
            output = ''

    def encrypter(self, text, listeOriginal, listeReverse):
        if text == ' ':
            x = text
        else:
            x = listeReverse[listeOriginal.index(text)]
        return x

    def reverse_text(self, text):
        # [::-1] slices the string by step 1 and reverses the input
        return text[::-1]
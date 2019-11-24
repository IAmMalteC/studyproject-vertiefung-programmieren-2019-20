import string
from userinput import offset


class Cesar(object):
    def __init__(self):
        print('You are using the Cesar encryption')
        self.offsetFactor=offset.get_offset(input("Please choose an offset factor:"))
        print('Your offset factor is:', self.offsetFactor)

        output = ''
        listOfCharacters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        while (True):
            textFromUser = input('Type the text you want to encrypt:')

            for letter in textFromUser:
                output = output + self.encrypter(self.offsetFactor, letter, listOfCharacters)

            print(output)
            output = ''

    def encrypter(self, offsetFactor, text, liste):
        global x
        try:
            if text == ' ':
                x = text
            elif len(liste) < offsetFactor:
                newOffsetFactor = offsetFactor - len(liste)
                Cesar.encrypter(self, newOffsetFactor, text, liste)
            else:
                x = liste[liste.index(text) + offsetFactor]
        except IndexError:
            # to catch it when the index gets out of range. F. ex. text = ~ and offsetFactor 1
            Cesar.encrypter(self, offsetFactor - len(liste), text, liste)

        return x

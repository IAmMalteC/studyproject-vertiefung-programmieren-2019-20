import string
from userinput import offset


class Cesar(object):
    def __init__(self):
        print('You are using the Cesar encryption')
        self.offsetFactor = offset.get_offset(input("Please choose an offset factor:"))
        print('Your offset factor is:', self.offsetFactor)

        output = ''
        list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        while True:
            text_from_user = input('Type the text you want to encrypt:')

            for letter in text_from_user:
                output = output + self.encoder(self.offsetFactor, letter, list_of_characters)

            print(output)
            output = ''

    def encoder(self, offset_factor, text, character_list):
        global x
        try:
            if text == ' ':
                x = text
            elif len(character_list) < offset_factor:
                new_offset_factor = offset_factor - len(character_list)
                Cesar.encoder(self, new_offset_factor, text, character_list)
            else:
                x = character_list[character_list.index(text) + offset_factor]
        except IndexError:
            # to catch it when the index gets out of range. F. ex. text = ~ and offsetFactor 1
            Cesar.encoder(self, offset_factor - len(character_list), text, character_list)

        return x

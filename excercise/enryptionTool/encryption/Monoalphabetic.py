from app import list_of_characters
import string


class Monoalphabetic:
    def __init__(self):
        print('You are using the Mono alphabetic encryption')

        output = ''
        list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        list_of_characters_reverse = self.reverse_text(list_of_characters)

        while True:
            text_from_user = input('Type the text you want to encrypt:')

            for letter in text_from_user:
                output = output + self.encoder(letter, list_of_characters, list_of_characters_reverse)

            print(output)
            output = ''

    def encoder(self, text, list_original, list_reverse):
        if text == ' ':
            x = text
        else:
            x = list_reverse[list_original.index(text)]
        return x

    def reverse_text(self, text):
        # [::-1] slices the string by step 1 and reverses the input
        return text[::-1]

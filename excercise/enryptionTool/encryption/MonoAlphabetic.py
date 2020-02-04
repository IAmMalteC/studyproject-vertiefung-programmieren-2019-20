from database.saves_to_database import save_monoalphabetic, save_encryptedstring


class MonoAlphabetic(object):
    def __init__(self, username, list_of_characters):
        print('You are using the Mono alphabetic encryption')
        # saves encryption
        save_monoalphabetic()

        output = ''
        # list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        list_of_characters_reverse = reverse_text(list_of_characters)

        text_from_user = input('Type the text you want to encrypt: ')
        for letter in text_from_user:
            output = output + mono_encrypter(letter, list_of_characters, list_of_characters_reverse)

        # save string
        save_encryptedstring(output, username, "monoalphabeticsubstitution")
        print(output)


def mono_encrypter(unencoded_character, list_original, list_reverse):
    global encoded_character
    try:
        if unencoded_character == ' ':
            encoded_character = unencoded_character
        else:
            encoded_character = list_reverse[list_original.index(unencoded_character)]
    except ValueError:
        # if characters are used which are not in the character list print ¶
        encoded_character = "¶"

    return encoded_character


def reverse_text(text):
    return text[::-1]  # [::-1] slices the string by step 1 and reverses the input


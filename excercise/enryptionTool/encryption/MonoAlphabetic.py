from database.saves_to_database import save_monoalphabetic, save_encryptedstring


class MonoAlphabetic(object):
    """ Lets us encrypt and save given text """
    def __init__(self, username, list_of_characters):
        print('You are using the Mono alphabetic encryption')
        # Save encryptiontype to database
        save_monoalphabetic()

        output = ''
        # list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        list_of_characters_reverse = reverse_text(list_of_characters)

        text_from_user = input('Type the text you want to encrypt: ')
        for letter in text_from_user:
            output = output + mono_encrypter(letter, list_of_characters, list_of_characters_reverse)

        # Save string to database,
        # encryptiontype is not needed, because it is saved earlier in this class
        save_encryptedstring(output, username)
        print(output)


def mono_encrypter(unencoded_character, list_original, list_reverse):
    """ Lets encrypt a single character, by replacing it with its counterpart.
    :param unencoded_character: the character to encode
    :param list_original: list of given characters
    :param list_reverse: list of given characters reversed
    :return: encoded_character: the encoded character
    """
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
    """ Reorders the given text
    :param text: input text
    :return: the given input in reverse order
    """
    return text[::-1]  # [::-1] slices the string by step 1 and reverses the input


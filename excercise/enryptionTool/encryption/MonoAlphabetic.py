from database.InsertIntoDatabase import insert_monoalphabetic, insert_encryptedstring


class MonoAlphabetic(object):
    def __init__(self, username, list_of_characters):
        print('You are using the Mono alphabetic encryption')
        # saves encryption
        insert_monoalphabetic()

        output = ''
        # list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        list_of_characters_reverse = reverse_text(list_of_characters)

        text_from_user = input('Type the text you want to encrypt: ')

        for letter in text_from_user:
            output = output + encrypter(letter, list_of_characters, list_of_characters_reverse)

        # save string
        insert_encryptedstring(output, username, "monoalphabeticsubstitution")
        print(output)


def encrypter(text, list_original, list_reverse):
    global x
    try:
        if text == ' ':
            x = text
        else:
            x = list_reverse[list_original.index(text)]
    except ValueError:
        # if characters are used which are not in the character list, just print ?, not the best catch!
        x = "¶"
    return x


def reverse_text(text):
    # [::-1] slices the string by step 1 and reverses the input
    return text[::-1]

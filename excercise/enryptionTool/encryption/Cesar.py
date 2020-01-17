from database.InsertIntoDatabase import insert_cesar, insert_encryptedstring
from userinput import offset


class Cesar(object):
    def __init__(self, username, list_of_characters):
        print('You are using the Cesar encryption')
        offset_factor = offset.get_offset(input("Please choose an offset factor: "))
        print('Your offset factor is:', offset_factor)
        # saves encryption
        cesar = insert_cesar(offset_factor)

        output = ''
        # list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

        text_from_user = input('Type the text you want to encrypt:')
        for letter in text_from_user:
            output = output + encrypter(offset_factor, letter, list_of_characters)

        # save string
        insert_encryptedstring(output, username, "cesar")

        print(output)


def encrypter(offset_factor, text, character_list):
    global x
    try:
        if text == ' ':
            x = text
        elif len(character_list) < offset_factor:
            new_offset_factor = offset_factor - len(character_list)
            encrypter( new_offset_factor, text, character_list)
        else:
            x = character_list[character_list.index(text) + offset_factor]
    except IndexError:
        # to catch it when the index gets out of range. F. ex. text = ~ and offsetFactor 1
        encrypter( offset_factor - len(character_list), text, character_list)
    except ValueError:
        print("Your choose a character which is not in our list.\nIt is used \"¶\" instead.")
        x = "¶"
    except RecursionError:
        print("Your offsetfactor was to big.\nPlease try again.")
        x = text

    return x

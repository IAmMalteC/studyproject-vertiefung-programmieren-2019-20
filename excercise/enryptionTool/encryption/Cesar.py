from database.InsertIntoDatabase import insert_cesar, insert_encryptedstring
from userinput import offset


class Cesar(object):
    def __init__(self, username, list_of_characters):
        print('You are using the Cesar encryption')
        offset_factor = offset.get_offset(input("Please choose an offset factor: "))
        print('Your offset factor is:', offset_factor)
        insert_cesar(offset_factor)  # saves encryption to database

        # list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        output = ''
        text_from_user = input('Type the text you want to encrypt:')
        for letter in text_from_user:
            output = output + encrypter(offset_factor, letter, list_of_characters)

        insert_encryptedstring(output, username, "cesar")  # save string to database
        print(output)


def encrypter(offset_factor, text, character_list):
    global x
    try:
        if text == ' ':
            x = text
        else:
            while len(character_list) < offset_factor:  # Checks if the chosen offset factor is too long for the array
                offset_factor = offset_factor - len(character_list)
            x = character_list[character_list.index(text) + offset_factor]  # sets x to the character by adding the offsetfactor to the index of the given character
    except IndexError:
        # to catch it when the index gets out of range. F. ex. text = ~ and offsetFactor 1
        encrypter(offset_factor - len(character_list), text, character_list)
    except ValueError:
        print("Your choose a character which is not in our list.\nIt is used \"¶\" instead.")
        x = "¶"

    return x

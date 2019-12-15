from database import DatabaseCreation, InsertIntoDatabase
from userinput import offset


class Cesar(object):
    def __init__(self,db_session, username, list_of_characters):
        print('You are using the Cesar encryption')
        offset_factor = offset.get_offset(input("Please choose an offset factor: "))
        print('Your offset factor is:', offset_factor)
        InsertIntoDatabase.insert_cesar(db_session, offset_factor.__int__(), 1)

        output = ''
        # list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

        text_from_user = input('Type the text you want to encrypt:')
        for letter in text_from_user:
            output = output + self.encoder(offset_factor, letter, list_of_characters)

        print(output)
        # 1 is always Cesar
        # zurzeit wird nur die Art der Verschlüsselung gespeichert und keine direkte Verbindung zum Cesar geschaffen.
        # So hatte ich die Aufgabe verstanden. Aber nochmal Robert fragen, ob das so stimmt. Da es besser wäre den
        # OffsetFactor auch gebrauchen zu können.
        user = db_session.query(DatabaseCreation.User).filter(DatabaseCreation.User.name == username).first()
        encoding = db_session.query(DatabaseCreation.EncodingType).filter(DatabaseCreation.EncodingType.id == 1).first()
        InsertIntoDatabase.insert_encodedstring(db_session, output, user.id, encoding.id)

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

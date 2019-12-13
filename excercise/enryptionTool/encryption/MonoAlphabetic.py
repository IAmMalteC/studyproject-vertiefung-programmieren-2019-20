from database import DatabaseCreation, InsertIntoDatabase


class MonoAlphabetic(object):
    def __init__(self, db_session, username, list_of_characters):
        print('You are using the Mono alphabetic encryption')
        InsertIntoDatabase.insert_monoalphabetic(db_session, 2)

        output = ''
        # list_of_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        list_of_characters_reverse = self.reverse_text(list_of_characters)

        text_from_user = input('Type the text you want to encrypt: ')

        for letter in text_from_user:
            output = output + self.encoder(letter, list_of_characters, list_of_characters_reverse)

        print(output)
        # 2 is always MonoalphabeticSubstitution
        user = db_session.query(DatabaseCreation.User).filter(DatabaseCreation.User.name == username).first()
        encoding = db_session.query(DatabaseCreation.EncodingType).filter(DatabaseCreation.EncodingType.id == 2).first()
        InsertIntoDatabase.insert_encodedstring(db_session, output, user.id, encoding.id)

    def encoder(self, text, list_original, list_reverse):
        if text == ' ':
            x = text
        else:
            x = list_reverse[list_original.index(text)]
        return x

    def reverse_text(self, text):
        # [::-1] slices the string by step 1 and reverses the input
        return text[::-1]

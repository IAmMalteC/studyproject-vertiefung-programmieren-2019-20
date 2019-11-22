import string
from userinput import offset

factor = offset.get_offset(input("Please choose an offset factor:"))
print('Your offset factor is:', factor)

listOfCharacters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
output = ''

#Hier ist die alte Methode die muss nachher weg
while(True):
    textFromUser = input('Type the text you want to encrypt:')
    #Encryption with a random number (26*2+10 = 62)

    for letter in textFromUser:
        #checks for spaces
        if letter == ' ':
            x = letter
        else:
            if listOfCharacters.index(letter) + randomNumber < 62:
                x = listOfCharacters[listOfCharacters.index(letter) + randomNumber]
            else:
                x = listOfCharacters[listOfCharacters.index(letter) + randomNumber - 62]
        output = output + x

    print(output, '\nEncrypted with the factor', randomNumber)
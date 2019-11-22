from random import randint
import string

while(True):
    textFromUser = input('Feel free to write your text:')
    #amount in the list
    listOfCharacters = string.ascii_letters + string.digits
    output = ''
    #Encryption with a random number (26*2+10 = 62)
    randomNumber = randint(1, 61)

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

#loads modules
from random import randint

while(True):
    textFromUser = input('Feel free to write your text:')
    output = ''
    #Encryption with a random number
    randomNumber = randint(1, 73)
    for letter in textFromUser:
        #Unicode 0-9 = 48-57, A-Z = 65-90, a-z = 97-122
        if letter == ' ':
            x = ord(letter)
        else:
            x = ord(letter) + randomNumber
            if (x > 57 and x < 64) or (x > 90 and x < 97):
                #Um die Sonderzeichen zwischen 9 und A und zwischen Z und a zu überspringen
                x += 7
            elif x > 122:
                #Um die Sonderzeichen nach z zu überspringen und zu 0 zurückzukehren
                x -= 74
                if (x > 57 and x < 64) or (x > 90 and x < 97):
                    # Um die Sonderzeichen zwischen 9 und A und zwischen Z und a zu überspringen
                    x += 7
        output = output + chr(x)
    print(output, 'Encrypted with the factor ', randomNumber)

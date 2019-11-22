while(True):
    textFromUser = input('Feel free to write your text:')
    output = ''
    for letter in textFromUser:
        #Unicoderaum 0-9 = 48-57, A-Z = 65-90, a-z = 97-122
        if letter == ' ':
            newLetter = letter
        else:
            x = ord(letter)
            randomNumber = 3
            xNew = x + randomNumber
                if xNew < 57 and xNew > 64:
                    #Um die Sonderzeichen zwischen 9 und A zu überspringen
                    xNew+= 7
                elif xNew < 90 and xNew > 97:
                    #Um die Sonderzeichen zwischen Z und a zu überspringen
                    xNew+= 7
                elif xNew < 122:
                    #Um die Sonderzeichen nach z zu überspringen und zu 0 zurückzukehren
                    xNew-= 74
        output = output + char(xNew)
    print(output)

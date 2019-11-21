while(True):
    textFromUser = input('Feel free to write your text:')
    output = ''
    for abc in textFromUser:
        if abc == ' ':
            newAbc = abc
        else

        output = output + newAbc
    print(output)

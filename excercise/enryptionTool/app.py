from userinput import offset

print('ENCRYPTION TOOL\n1 : Cesar encryption\n2 : Mono alphabetic substitution\n3 : About\n4 : Quit program')

while(True):
    text = input('Please choose a value and press Enter:')
    # Cesar Encryption
    if(text == '1'):
        factor = offset.get_offset(input("Please choose an offset factor:"))
        print('Your Offset is:', factor)
    # Mono alphatic substition
    elif(text == '2'):
        break
    #About page
    elif(text == '3'):
        print('This is a basic encryption tool')
    #Quit programm
    elif(text == '4'):
        print('Goodbye')
        break
    else:
        print('You choose not a valid value.\nTry again.')

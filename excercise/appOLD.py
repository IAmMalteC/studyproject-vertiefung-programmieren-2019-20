programmlaeuft = True
while(programmlaeuft):
    eingabe = input('Bitte geben Sie einige Zeichen ein: ')
    ausgabe = ''
    for zeichen in eingabe:
        if zeichen == ' ':
            neuesZeichen = zeichen
        else:
            zahl = ord(zeichen)
            neueZahl = zahl + 3
            if neueZahl > ord('z') and neueZahl < ord('~'):
                neueZahl = neueZahl - 58
            elif neueZahl > ord('Z') and neueZahl < ord('^'):
                neueZahl = neueZahl - 43
            elif neueZahl > ord('9') and neueZahl < ord('='):
                neueZahl = neueZahl + 39
            neuesZeichen = chr(neueZahl)
        ausgabe = ausgabe + neuesZeichen
    print(ausgabe)
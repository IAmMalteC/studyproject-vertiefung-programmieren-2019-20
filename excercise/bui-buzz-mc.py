firstValue = 3
secondValue = 5

for i in range (1,100):
    if (i % firstValue == 0 and i % secondValue != 0):
        print "Umwelt"
    elif (i % secondValue == 0 and i % firstValue != 0):
        print "Informatik"
    elif (i % firstValue == 0 and i % secondValue == 0):
        print "Umweltinformatik"
    else:
        print i

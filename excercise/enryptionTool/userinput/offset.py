from random import randint


def get_offset(self):
    try:
        number = int(self)
        return number
    except ValueError:
        print('I could not read your value. So I chose a random value.')
        return randint(1, 1024)

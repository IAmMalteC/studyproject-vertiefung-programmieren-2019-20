from random import randint


def get_offset(self):
    """Checks in the input is a number,
    if not create a random number between 1 and 1024
    :return a random number between 1 and 1024
    """
    try:
        number = int(self)
        return number

    except ValueError:
        print('I could not read your value. So I chose a random value.')
        return randint(1, 1024)

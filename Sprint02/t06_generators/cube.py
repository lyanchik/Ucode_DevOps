def cube(number):
    while number > 0:
        yield number ** 3
        number -= 1
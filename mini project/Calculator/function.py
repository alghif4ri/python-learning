def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    #cek apakah value pada "y" = 0
    if y == 0:
        #jika value = 0 maka akan muncul error
        raise ValueError("Cannot divide by zero!")
    #jika tidak lakukan pembagian
    return x / y

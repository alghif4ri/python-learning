import random

def guessing_game():
    number = random.randint(1, 100) #generate angka random dari 1 -100
    percobaan = 0

    print("Hey, ayo main tebak angaka!")
    while True:
        guess = int(input("Tebak angka dari 1 sampa 100 : ")) # input angka tebakan
        percobaan += 1

        if guess < number:
            print("Angka terlalu kecil!, coba lagi!")
        elif guess > number:
            print("Angka terlalu besar!, coba lagi!")
        else:
            print(f"Yeay!, tebakan kamu benar dengan {percobaan} percobaan haha!")
            break

guessing_game()

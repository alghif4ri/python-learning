# argument list untuk menampung beberapa value pada satu parameter, di definisikan dengan (*) pada parameter
# argument list ditempatkan diakhir jika ada parameter lain, argument list hanya bisa satu
def total(angka, *listnumber): #parameter dengan argument list
    number = 0
    for no in listnumber:
        number = number + no
    print(f"Total {listnumber} = {number}")

total(10,20,10) #value pertama (10) masuk kedalam parameter angka, 
#sedangkan value kedua dan tiga (20,10) masuk ke dalam argument list dan dieksekusi pada kode blok for loop


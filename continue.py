for i in range(0, 100): # fungsi loop dengan data 0 - 100
    if i % 2 == 0:  # kondisi jika nilai i modulus 2 sama dengan 0
        print("even number:",i) # menampilakan nilai genap
        continue # berfungsi ketika nilai ganjil maka akan dilanjutkan ke tahap selanjutnya
    print("odd number:",i) # menampilkan nilai ganjil

#membuat program input data dengan implementasi for loop, list dan range

banyak_data = int(input("berapa banyak data?")) #masukan angka jumlah data yang ingin diinputkan

#variable untuk menampung data yang diinputkan
nama = []
umur = []
alamat = []

for i in range(0, banyak_data): #fungsi loop untuk melakukan perulangan sesuai angka yang di inputkan
    print(f"Data ke: {i}") #menampilkan angka data keberapa yang akan diinputkan
    input_nama = input("Nama :") #untuk menginputkan data nama
    input_umur = int(input("Umur :")) #untuk menginputkan data umur
    input_alamat = input("Alamat :") #untuk menginputkan data umur

# menambahkan data yang diinputkan kedalam list
    nama.append(input_nama) 
    umur.append(input_umur)
    alamat.append(input_alamat)

for i in range(0, len(nama)): # fungsi loop untuk melakukan perulangan dengan mengambil data dari yang diinputkan berdasarkan panjang data list
    data_nama = nama[i]
    data_umur = umur[i]
    data_alamat = alamat[i]
    print (f"{data_nama} - Umur:{data_umur} - Alamat: {data_alamat}") # menampilkan data yang telah diinputkan


# method menampilakan daftar kontak
def display_kontak(daftar_kontak):
    # lakukan for loop dari data dictionary
    for kontak in daftar_kontak:
        print("===================")
        print(f"Nama: {kontak['nama']}")
        print(f"Email: {kontak['email']}")
        print(f"Telepon: {kontak['telepon']}")

#method tambah kontak
def new_kontak():
    nama = input("Nama :")
    email = input("Email :")
    telepon = input("Telepon :")
    #buat variable "kontak" untuk menampung
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    #langsung return nilai kedalam kontak 
    return kontak

#method cari kontak
def cari_kontak(daftar_kontak):
    nama_dicari = input("Nama yang dicari : ")
#lakukan for loop untuk akses data
    for kontak in daftar_kontak:
        nama = kontak["nama"]
        #mencari data dengan method find, find mengembalikan posisi index karakter yang dicari, jika yang di cari "e" dari "eko" maka yang direturn adalah index[0], jika tidak ada maka -1
        if nama.lower().find(nama_dicari.lower()) != -1:
            print("=====================")
            print(f"Nama: {kontak['nama']}")
            print(f"Email: {kontak['email']}")
            print(f"Telepon: {kontak['telepon']}")
        else:
            print("Nama tidak ditemukan")


#menghapus kontak
def del_kontak(daftar_kontak):
    #masukan nomor telepon untuk dicari terlebih dahulu
    telepon = input("No Telepon yang ingin dihapus : ")
    # set index di -1 untuk trigger ketika data tidak ada
    index = -1
    # lakukan for loop untuk mencari data kontak dengan range dimulai dari index 0 untuk mengambil jumlah data menggunkan len
    for i in range(0,len(daftar_kontak)):
        #hasil pencarian dimasukan kedalam variable kontak
        kontak = daftar_kontak[i]
        #jika "telepon" yang telah diinputkan sama dengan value yang ada dalam "kontak" break untuk menghentikan perulangan
        if telepon == kontak["telepon"]:
            index = i
            break
    #jika hasil pencarian tidak ada didalam index yang dimulai dari 0 maka "kontak tidak ditemukan"
    if index == -1:
        print("Kontak tidak ditemukan!")
    #jika ditemukan maka eksekusi function del
    else:
        del daftar_kontak[index]
        print("kontak berhasil dihapus!")


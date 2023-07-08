
import function
# data dictionary
daftar_kontak = []
daftar_kontak.append({
    'nama':"John Doe",
    'email':"john@gmail.com",
    'telepon':'+62897-xxxxxxx'
})


#Menu Phonebook

#menggunakan while untuk menampilkan daftar menu phonebook, dicombine dengan if dan elif untuk kondisi menu yang dipilih
while True:
    print("#Menu")
    print("1. Lihat Daftar Kontak")
    print("2. Tambah Kontak Baru")
    print("3. Cari Kontak By Nomor")
    print("4. Ubah Data Kontak")
    print("5. Hapus Data Kontak")
    print("0. Keluar Program")

    menu = input("Pilih Menu : ")

    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
    elif menu == "3":
        function.cari_kontak(daftar_kontak)
    elif menu == "4":
        print("menu belum tersedia!")
    elif menu =="5":
        function.del_kontak(daftar_kontak)

print("Phonebook Close")

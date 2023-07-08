#set berfungsi untuk menampung data uniq dan tidak bisa mengubah data yang sudah ada. 
siswa = {"andi","budi", "caca"}

# set tidak bisa dipanggil dengan index

#set bisa dipanggil dengan for loop
for daftar_siswa in siswa:
    print("Nama Siswa:", daftar_siswa)

#set bisa ditambahkan data
siswa.add('didi')

#set bisa menghapus data
siswa.remove('caca')

#hasil set yang ditampilkan tidak bisa berurut, ketika dipanggil data yang ditampilkan akan selalu berubah posisi
print(siswa)

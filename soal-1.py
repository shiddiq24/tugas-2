print("Selamat Datang!")
print("--Menu--")
menu = ["Daftar Kontak", "Tambah Kontak", "Keluar"]
index=1
for i in menu:
  print(str(index)+"."+ i)
  index += 1

d = {
    "Nama" : "shiddiq",
    "No Telepon" : "08127161711", 
    "Nama" : "Jaka",
    "No Telepon" : "08127897877"   
}

Menu = int(input("Pilih menu: "))

if Menu == 1:
    print("Daftar kontak")
    print(d)
elif Menu == 2:
    print(input("Nama: "))
    print(input("No telepon: "))
    print("Kontak berhasil ditambahkan")
elif Menu == 3:
    print("Program selesai, sampai jumpa!")
else:
    print("Menu tidak tersedia")
 
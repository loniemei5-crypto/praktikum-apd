                                                    #set

#(tidak boleh duplikat) dan bersifat tidak berurutan (unordered). 
# Membuat set 
buah = {"apel", "jeruk", "mangga", "apel"}  
print(buah) 

angka_ganjil = {1, 3, 5, 7, 9} 
for angka in angka_ganjil: 
   print(angka)

add.(229, 245, 245, 1)
inputtambah = int(input("tambah angka : "))
angka_ganjil.add(inputtambah)
print(angka_ganjil)


                                           #remove untuk menghapus data 

#jika ada data yang di isi tidak sesuai yang di dalam data akan ada eror
#discard untuk biar tidak eror jika memilih yang tidak ada di dalam data(tetap menampilkan data walaupun tidak ada data tsb)
angka_ganjil.remove(9)

                                                 #union() 

#menggabungkan semua elemen dari set bersangkutan dan set yang lain diberikan, tanpa duplikasi. 
Daftar_buku = { 
# q           value            (q tidak boleh sama)
"Buku1" : "Bumi Manusia", 
"Buku2" : "Laut Bercerita" 
} 

print(Daftar_buku["Buku1"]) #hanya memanggil buku1 saja
print(Daftar_buku) #memanggil keduanya

#output 
#Bumi Manusia 
#{'Buku1': 'Bumi Manusia', 'Buku2': 'Laut Bercerita'} 

Biodata = { 
"Nama" : "Ananda Daffa Harahap", #str
"NIM" : 2409106050,              #int
"KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],  #set
"Mahasiswa_Aktif" : True, 
"Social Media" : { 
          "Instagram" : "daffahrhap" 
      } 
} 

List_game = {"GTA 5" : "Open World", "Valorant" : "FPS", "Honkai Star Rail" 
: "RPG"} 

                                                     #get

print(f"nama saya adalah {Biodata["Nama"]}") 
#                                            mengakses q     
print(f"Instagram : {Biodata['Social Media']['Instagram']}")
#get untuk ngeluarin value
print(f"nama saya adalah {Biodata.get("Nama")}") 
print(Biodata.get("Nama")) 

#output 
nama saya adalah Ananda Daffa Harahap 
Instagram : daffahrhap 
 
nama saya adalah Ananda Daffa Harahap 
Ananda Daffa Harahap 

#contoh2
print(Biodata.get("Nama")) 
print(Biodata.get("Alamat")) 
print(Biodata.get("Alamat", "Key tersebut tidak ada")) 
#output
Ananda Daffa Harahap 
None 
Key tersebut tidak ada 

                                                  #Items()

Nilai = { 
    "Matematika": 80, 
    "B. Indonesia": 90, 
        "B. Inggris": 81, 
    "Kimia": 78, 
    "Fisika": 80 
} 
 
# Tanpa menggunakan items() 
for i in Nilai: 
    print(i) 
 
print("")  # pemisah 
 
# Menggunakan items() 
for i, j in Nilai.items(): 
    print(f"Nilai {i} anda adalah {j}") 
 
# output 
Matematika 
B. Indonesia 
B. Inggris 
Kimia 
Fisika 
 
Nilai Matematika anda adalah 80 
Nilai B. Indonesia anda adalah 90 
Nilai B. Inggris anda adalah 81 
Nilai Kimia anda adalah 78 
Nilai Fisika anda adalah 80 

                                               #update().

Film = { 
"Avenger Endgame" : "Action", 
"Sherlock Holmes" : "Mystery", 
"The Conjuring" : "Horror"
} 
#Sebelum Ditambah 
print(Film) 
 
Film["Zombieland"] = "Comedy" 
#biar gak nimpa key dan key dan value di atas
Film.update({"Hours" : "Thriller"}) 
#Setelah Ditambah 
print(Film) 

#output
#Sebelum Ditambah 
{'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery', 
'The Conjuring': 'Horror'} 
 
#Setelah Ditambah 
{'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery', 
'The Conjuring': 'Horror', 'Zombieland': 'Comedy', 'Hours': 
'Thriller'}

#Del akan menghapus secara keseluruhan tanpa ada tersisa. 

data = { 
"Nama" : "Daffa", 
"Umur" : 19, 
"Jurusan" : "Informatika" 
} 
#Sebelum Dihapus 
print(data) 
 
del data["Nama"] 
 print(data) 
 
#memanggil data yang telah dihapus 
print(data.get("Nama")) 
 
{'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'} 
{'Umur': 19, 'Jurusan': 'Informatika'} 

None
#Setelah diubah

#pop() akan menghapus tetapi masih dapat kita lihat apa yang kita hapus dengan cara kita tampung pada sebuah variabel. 

data = { 
"Nama" : "Daffa", 
"Umur" : 19, 
"Jurusan" : "Informatika" 
} 
 
#Sebelum Dihapus 
print(data) 
 
cache = data.pop("Nama") 
 
#Setelah dihapus 
print(data) 
 
#memanggil data yang telah dihapus pada dictionary 
print(data.get("Nama")) 
 
#memanggil data yang telah dihapus pada variabel cache 
print(cache) 
 
{'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'} 
{'Umur': 19, 'Jurusan': 'Informatika'} 
None 
 
Daffa

#clear() akan menghapus baik itu key (kunci) maupun value (nilai).

data = { 
"Nama" : "Daffa", 
"Umur" : 19, 
"Jurusan" : "Informatika" 
} 
 
#output
#Sebelum Dihapus 
print(data) 
data.clear() 
 
#Setelah dihapus 
print(data) 
 
{'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'} 
{}

#copy buat diksonery baru
#contoh 1
buku = {                                   |  diksonery  |
 "Buku1" : "Bumi Manusia",                 |             |
 "Buku2" : "Laut Bercerita"                |             |
}                                          |             |
 
pinjam = buku.copy() 

print("Dictionary yang telah disalin : ", pinjam) 
 
Dictionary yang telah disalin : {"Buku1" : "Bumi Manusia", "Buku2" : "Laut 
Bercerita"}

#fromkeys()
#contoh 1
key = "apel", "jeruk", "mangga" 
value = 1
buah = dict.fromkeys(key, value) 
print(buah) 
 #output
{'apel': 1, 'jeruk': 1, 'mangga': 1} 

#contoh 2
key = "apel", "jeruk", "mangga" 
value = 1,2,3
buah = dict.fromkeys(key, value) 
print(buah) 
 #output
{'apel': 1, 'jeruk': 2, 'mangga': 3}

#Keys & Value 
Nilai = { 
"Matematika" : 80, 
"B. Indonesia" : 90, 
"B. Inggris" : 81, 
"Kimia" : 78, 
"Fisika" : 80 
} 
 
#menggunakan keys 
for i in Nilai.keys(): 
 print(i) 
print("") 
 
#menggunakan value 
for i in Nilai.values(): 
 print(i) 

#output
Matematika 
B. Indonesia 
B. Inggris 
Kimia 
Fisika 
 
80 
90 
81 
78 
80 

#SetDefault 
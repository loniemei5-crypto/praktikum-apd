#mendefinisikan list                       indeks baru
#                                            [0]  [1]
praktikum = ["Mahasiswa", 20, True, 45.10, ['APD',25]]
#indeks      [0]         [1]  [2]    [3]      [4]
print(prkatikum [2][1]) #yang akan di tampikan yang di atas pilih indeks ke berapa

#append menambah indeks paling terakhir
# list awal
studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# Tambahkan Web
studyclub.append("Web")
print(studyclub)
# output ['Data Science', 'Robotics', 'Multimedia', 'Network', 'Web']

#insert menambah indeks di tengah2
# list awal
studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
# Tambahkan Web
studyclub.insert(2,"Web")
print(studyclub)
# output ['Data Science', 'Robotics', 'Web', 'Multimedia', 'Network']

#mengubah data yang ada menjadi data baru
# list awal
studyclub = ["Data Science", "Robotics", "Multimedia", "Network"]
print(studyclub)
# Kita akan mengganti elemen di indeks ke-2, yakni "Multimedia"
studyclub[2] = "AI"
print(studyclub)
# output awal ['Data Science', 'Robotics', 'Multimedia', 'Network']
# output sesudah ['Data Science', 'Robotics', 'AI', 'Network']

#menghapus data
# list awal
matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
print(matakuliah)
# menghapus elemen pada indeks ke-2, yakni "Kalkulus"
del matakuliah[2]
print(matakuliah)
# output awal ['PTI', 'APD', 'Kalkulus', 'Diskrit']
# output sesudah ['PTI', 'APD', 'Diskrit']

# list awal
matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
print(matakuliah)
# menghapus elemen dengan nilai "Kalkulus"
matakuliah.remove('Kalkulus')
print(matakuliah)
# output awal ['PTI', 'APD', 'Kalkulus', 'Diskrit']
# output sesudah ['PTI', 'APD', 'Diskrit']

#del indeks ke berapa 
#remove apa nilai yang dalam indeks []

#pop terhapus tapi di tempat sampah
# list awal
matakuliah = ['PTI', 'APD','Kalkulus','Diskrit']
print(matakuliah)
# Menghapus & mengambil elemen 'Kalkulus' pada indeks ke-2
ambil_matkul = matakuliah.pop(2)
print(matakuliah)
print(ambil_matkul)
# output matakuliah ['PTI', 'APD', 'Diskrit']
# output elemen yang diambil "Kalkulus"

#start,stop,step
# list
matakuliah = ['PTI', 'APD','Kalkulus','Diskrit','Bahasa Inggris',
'Orsikom','Basis Data']
# Menampilkan list mulai dari indeks 1 hingga 5 dengan loncatan 2
print(matakuliah[1:6:2])
#              [s1][s2][s3] [stop,start bisa di kosongkan karena ]
#                [::2]
# output['APD','Diskrit', 'Orsikom']

#operator tambahan secara berurutan
# List
a = [1, 2, 3]
b = [4, 5, 6]
# menggabungkan kedua list dengan operator (+)
c = a + b
print(c)
# output [1, 2, 3, 4, 5, 6]

#pengulangan
# List
a = ["teknik", "informatika"]
# mengulang isi list dengan operator (*) sebanyak 3 kali
c = a*3
print(c)
# output
['teknik', 'informatika', 'teknik', 'informatika', 'teknik',
'informatika']

#pengulangan
# List
a = ["teknik", "informatika"]
# mengulang isi list dengan operator (*) sebanyak 3 kali
c = a*3
print(c)
# output ['teknik', 'informatika', 'teknik', 'informatika', 'teknik','informatika']

#membuat nasted
# Membuat Nested List
kelas = [
 #B [0]      [1]     [2]                A
["Ridho", "Lian", "Nabil"],        # indeks [0]
["Daffa", "Dante", "Santoso"]      # indeks [1]
["Pernanda", "Riyadi", "Ahnaf"],   # indeks [2]
]
# Memanggil elemen "Santoso"
print(kelas[1][2])
#          [A][B]
# output Santoso

# list mahasiswa    i                           j
mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]

# perulangan for untuk mendapatkan semua elemen
for i in mahasiswa: #kalau cuman i saja akan menampilkan semua mahasiswa
  for j in i : #akan menampikan i dan j 
    print (j)
# i dan j merupakan variabel sementara / temporary, kita dapat menggantinya dengan apa saja asal sesuai dengan syarat nama variabel
# output
#Daffa
#Dante
#Santoso
#Pernanda
#Triya
#Ahnaf

#mendefinisikan tuple
# anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
# menampilkan tuple
anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
print(anggota)
# output ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))

#cara mengubah tupel menjadi list anggota = list(anggota)
#anggota = list(anggota)

# tuple
tugas = ('rangkuman', 'arduino','scrapping')

# untuk membuat variabel pada list
(PTI, orsikom, basisdata) = tugas
#=>[rangkuman] [arduino] [scrapping]

print(PTI)
print(orsikom)
print(basisdata)
# output
#rangkuman
#Arduino
#scrapping

#cintoh 2 (* mengambil sampai mentok)
barang = ('triangle','bola','meja','handphon','televisi')
(segitiga,bulat,*kotak) = barang

print(segitiga)
print(bulat)
print(kotak)

#output triangle 
# bola
# ['meja', 'handphon', 'televisi']

#cintoh 3 (* mengambil sampai mentok)
barang = [['triangle','bola'],['meja','handphon'],['televisi','leptop']]
for nama_barang in barang:
  print(nama_barang)
  (barang1,barang2) = nama_barang

print(barang1)
print(barang2)

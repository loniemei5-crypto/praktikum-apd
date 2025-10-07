ulangi = 10
for i in range(ulangi):
    print(f'perulangan ke{i}')

ulangi = 10
for i in range(2,10,4):
    print(f'perulangan ke{i}')

for i in range(1,4): 
  print(f'i: {i}') #i:1(i akan berhenti sampai j berhenti) #j 1,2,3,4
  for j in range(1,3):
    print(f'{i} : {j}') 
    for k in range(1,3):
      print(f'i: {i},j: {j}, (k: {k})')

for i in range(1,4): 
  print(f'i: {i}') #i:1(i akan berhenti sampai j berhenti) #j 1,2,3,4
  for j in range(1,3):
    print(f'{i} : {j}') 
    for k in range(1,3):
      print(f'i: {i},j: {j}, (k: {k})')
      print(' ')


for i in range(1,4): #untuk baris(cuman sampai baris 3)
 for j in range(1,5): #untuk kolom
   print(f'{i} x {j} = {i * j}')
 print('')

simpan = [1, 'Dapupu', 4.00, True]
for i in simpan: # untuk menampilkan semuanya #agar printnya ke bawah bukan ke samping
 print(i)

for index,isilist in enumerate(simpan): #sama aja #index >[0],[1],[2],[3].isi list [1,'dapupu',4.00, true]
 print(simpan[index])


jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
  hitung += 1
  jawab = input("Ulang lagi? ")
print(f"Total perulangan: {hitung}")

hitung = 0
while (true):
  print(hitung)
  hitung +=1
  if hitung == 10:
  break #untuk berhenti sampai 10
print(f"total perulangan: {hitung}")

hitung = 0
while (true):
  print(hitung)
  hitung +=1
print(f"total perulangan: {hitung}")

for i in range(1, 11):
    if i % 2 != 0:
         continue
    print(f"Angka genap ditemukan: {i}")
print("\nProgram selesai.")
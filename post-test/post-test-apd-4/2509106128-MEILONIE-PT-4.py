print("========== MISI PERTAMA NARUTO ==========")
nim = input("Masukkan 3 NIM terakhir kamu: ")
stamina = int(nim)
chakra = 0

print(f"Stamina awal: {stamina}")
print(f"Target Chakra: 200")

while chakra < 200 and stamina > 0:
    chakra += 5
    stamina -= 3

print(f"Total Chakra: {chakra}")
print(f"Sisa Stamina: {stamina}")

if chakra >= 200:
    print("naruto mencapai 200 cakra")
else:
    print("Naruto kehabisan stamina")

print("========== MISI KEDUA NARUTO ==========")
nim = input("Masukkan 2 NIM terakhir kamu: ")
tinggi_menara = int(nim)

print(f"Tinggi menara: {tinggi_menara} meter")
gulungan = 0

for meter in range(1, tinggi_menara , 3):
    gulungan += 1
    print(f"NARUTO menemukan Gulungan Informasi di ketinggian {meter} meter")
print(f"jumlah Gulungan Informasi yang dikumpulkan: {gulungan}")

print("========== MISI TERAKHIR NARUTO ==========")
nim = input("Masukkan digit terakhir kedua NIM kamu: ")
jumlahkoridor = int(nim)

dataintel = 0
perangkap = 0

print(f"Jumlah koridor yang harus diselidiki: {jumlahkoridor}")

for koridor in range(1, jumlahkoridor + 1):
    print(f"Memasuki Koridor {koridor}:")
    for ruangan in range(1, 4):
        if ruangan % 2 == 1:
            dataintel += 1
            print(f"  Ruangan {ruangan}: Berisi Data Intelijen")
        else:
            perangkap += 1
            print(f"  Ruangan {ruangan}: Berisi Perangkap Peledak")

print("hasil akhir")
print(f"Total Data Intelijen ditemukan: {dataintel}")
print(f"Total Perangkap Peledak dijinakkan: {perangkap}")
print ("""harga:
batu bata = Rp100
karung semen = Rp100000""")

total_setelah_diskon=float

harga_batu_bata = 100
harga_semen = 100000


nama_pelanggan = str(input("masukkan nama anda:"))
jumlah_batu_bata = int(input("masukkan jumlah batu bata:"))
jumlah_semen = int(input("masukkan jumlah semen:"))

total_biaya_awal =(jumlah_batu_bata*harga_batu_bata)+(jumlah_semen*harga_semen)

if jumlah_batu_bata == 500 and jumlah_semen == 5:
    jenis_paket = "paket hemat (15%)"
    diskon= 0.15
elif jumlah_batu_bata == 2000 and jumlah_semen == 16:
    jenis_paket = "paket ultra mantap (30%)"
    diskon = 0.30
else:
    jenis_paket = "anda tidak mendapatkan diskon"
    diskon = 0

diskon = total_biaya_awal*diskon
total_setelah_diskon = total_biaya_awal-diskon

# --- Output Ringkasan Pesanan ---
print("=" * 44)
print("        PERKIRAAN HARGA BAHAN BAKU")
print("=" * 44)
print(f"nama pelanggan           : {nama_pelanggan}")
print("-" * 44)
print(f"{'| Barang':<13} | {'Jumlah':<8} | {'Harga barang':<15} |")
print("-" * 44)
print(f"{'| Batu Bata':<13} | {jumlah_batu_bata:<8} | {(harga_batu_bata):<15} |")
print(f"{'| Semen':<13} | {jumlah_semen:<8} | {(harga_semen):<15} |")
print("-" * 44)
print(f"Total Biaya Awal{'':<27}: {'Rp.'}{(total_biaya_awal)}")
print(f"Paket Yang Didapat{'':<25}: {jenis_paket}")
print(f"Jumlah Diskon{'':<30}: {'Rp.'}{diskon}")
print("-" * 44)  
print(f"TOTAL BIAYA AKHIR:{'Rp.'}{(total_setelah_diskon)}")
print("=" * 44)
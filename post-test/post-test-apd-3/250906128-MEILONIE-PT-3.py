print("=" * 40)
print ("   PENGHITUNGAN GAJI KARYAWAN PT.BOM")
print("=" * 40)

nama = str(input("NAMA ANDA:"))
jabatan = str(input("JABATAN PERACIK/PENGANTAR:"))
harikerja = int(input("JUMLAH HARI KERJA: "))
jamkerja = int(input("JAM KERJA PER HARI: "))
jumlahlembur = int(input("JUMLAH LEMBUR: "))

hargapetasan = 5000
bayaranperjam = 0
bayaranperlembur = 0

if jabatan == "peracik" :
    if harikerja >= 24 and jamkerja >= 8 and jumlahlembur >= 4:
        bayaranperjam = 25000
        bayaranperlembur = 15000
    elif harikerja >= 18 and jamkerja >= 6 and jumlahlembur >= 2:
        bayaranperjam = 20000
        bayaranperlembur = 10000
    else:
        bayaranperjam = 15000
        bayaranperlembur = 10000

elif jabatan == "pengantar":
    if harikerja >= 20 and jamkerja >= 7 and jumlahlembur >= 7:
        bayaranperjam = 25000
        bayaranperlembur = 20000
    elif harikerja >= 16 and jamkerja >= 5 and jumlahlembur >= 4:
        bayaranperjam = 20000
        bayaranperlembur = 15000
    else:
        bayaranperjam = 15000
        bayaranperlembur = 12000

totalgaji = ((bayaranperjam*jamkerja)*harikerja) + (jumlahlembur*bayaranperlembur)

print("------------GAJI------------" )
print(f"Nama Karyawan {'':<4}:{nama}")
print(f"Jabatan {'':<10}:{jabatan}")
print(f"Harga 1 pcs {'':<6}:Rp.{hargapetasan}")
print(f"Hari Kerja {'':<7}:{harikerja}")
print(f"Jam Kerja / Hari {'':<1}:{jamkerja}")
print(f"Jumlah Lembur {'':<4}:{jumlahlembur}")
print(f"Bayaran per Jam {'':<2}:Rp.{bayaranperjam}")
print(f"Bayaran per Lembur: Rp.{bayaranperlembur}")
print("=" * 34)
print(f"Total Gaji {'':<7}:Rp.{totalgaji}")
print("=" * 34)
import os

users = {
    "meilonie": {"password": "meilonie", "role": "admin"}
}
data = []
max_data = 100

def tampilkan_header():
    """Menampilkan judul utama program"""
    os.system("cls" if os.name == "nt" else "clear")
    print("=== APLIKASI CATATAN PEMINJAMAN BARANG TEMAN KOS ===")

def tampilkan_data(role):
    """Menampilkan data sesuai role"""
    if not data:
        print("Belum ada data.")
    else:
        for i, d in enumerate(data, start=1):
            print(f"{i}. {d['nama']} meminjam {d['barang']} pada {d['tanggal']}")
    input("ENTER...")

def prosedur_logout():
    """Menampilkan pesan logout"""
    print("Logout berhasil!")
    input("ENTER untuk kembali ke menu utama...")

def tambah_data(role):
    """Menambah data baru dengan role tertentu"""
    global data
    if len(data) >= max_data:
        print("Data penuh!")
        input("ENTER...")
        return

    n, b, t = "", "", ""

    try:
        if role == "admin":
            n = input("Nama: ")
        else:
            n = user_login 

        b = input("Barang: ")
        t = input("Tanggal: ")

        if n and b and t:
            data.append({"nama": n, "barang": b, "tanggal": t})
            print("Data berhasil ditambah!")
        else:
            print("Data tidak boleh kosong.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    input("ENTER...")

def menu_admin():
    """Menu khusus admin (rekursif untuk kembali ke menu utama)"""
    tampilkan_header()
    print("=== MENU ADMIN ===")
    print("1. Lihat Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Logout")
    pilih = input("Pilih: ")

    if pilih == "1":
        tampilkan_data("admin")
    elif pilih == "2":
        tambah_data("admin")
    elif pilih == "3":
        ubah_data()
    elif pilih == "4":
        hapus_data()
    elif pilih == "5":
        prosedur_logout()
        return
    else:
        print("Pilihan salah.")
        input("ENTER...")

    menu_admin()


def ubah_data():
    """Mengubah data yang sudah ada"""
    global data
    try:
        if not data:
            print("Belum ada data.")
            input("ENTER...")
            return

        for i, d in enumerate(data, start=1):
            print(f"{i}. {d}")
        no = int(input("Nomor ubah: ")) - 1

        if 0 <= no < len(data):
            n = input("Nama baru: ")
            b = input("Barang baru: ")
            t = input("Tanggal baru: ")

            if n and b and t:
                data[no] = {"nama": n, "barang": b, "tanggal": t}
                print("Data diubah!")
            else:
                print("Tidak boleh kosong.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    input("ENTER...")


def hapus_data():
    """Menghapus data dengan error handling"""
    global data
    try:
        if not data:
            print("Belum ada data.")
            input("ENTER...")
            return

        for i, d in enumerate(data, start=1):
            print(f"{i}. {d}")
        no = int(input("Nomor hapus: ")) - 1

        if 0 <= no < len(data):
            del data[no]
            print("Data dihapus!")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Input harus berupa angka.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    input("ENTER...")


def menu_pengguna():
    """Menu pengguna biasa"""
    while True:
        tampilkan_header()
        print("=== MENU PENGGUNA ===")
        print("1. Lihat Data")
        print("2. Tambah Data")
        print("3. Logout")
        pilih = input("Pilih: ")

        if pilih == "1":
            tampilkan_data("pengguna")
        elif pilih == "2":
            tambah_data("pengguna")
        elif pilih == "3":
            prosedur_logout()
            break
        else:
            print("Pilihan salah.")
            input("ENTER...")


while True:
    tampilkan_header()
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        user = input("Username: ")
        pw = input("Password: ")

        if user in users and users[user]["password"] == pw:
            user_login = user 
            role = users[user]["role"]

            if role == "admin":
                menu_admin() 
            else:
                menu_pengguna()
        else:
            print("Login gagal! Username atau password salah.")
            input("ENTER...")

    elif menu == "2":
        tampilkan_header()
        print("=== REGISTER ===")
        u = input("Username baru: ")
        p = input("Password: ")

        if u in users:
            print("Username sudah terdaftar.")
        elif u and p:
            users[u] = {"password": p, "role": "pengguna"}
            print("Register berhasil!")
        else:
            print("Input tidak boleh kosong.")
        input("ENTER...")

    elif menu == "3":
        print("Terima kasih telah menggunakan aplikasi!")
        break
    else:
        print("Pilihan salah.")
        input("ENTER...")

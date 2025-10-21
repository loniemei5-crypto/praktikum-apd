import os

users = {
    "meilonie": {"password": "meilonie", "role": "admin"}
}

data = []

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=== APLIKASI CATATAN PEMINJAMAN BARANG TEMAN KOS ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        user = input("Username: ")
        pw = input("Password: ")

        if user in users and users[user]["password"] == pw:
            role = users[user]["role"]
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"=== MENU {role.upper()} ===")

                if role == "admin":
                    print("1. Lihat Data")
                    print("2. Tambah Data")
                    print("3. Ubah Data")
                    print("4. Hapus Data")
                    print("5. Logout")
                else:
                    print("1. Lihat Data")
                    print("2. Tambah Data")
                    print("3. Logout")

                pilih = input("Pilih: ")

                if role == "admin":
                    if pilih == "1":
                        if not data:
                            print("Belum ada data.")
                        else:
                            for i, d in enumerate(data, start=1):
                                print(f"{i}. {d['nama']} meminjam {d['barang']} pada {d['tanggal']}")
                        input("ENTER...")

                    elif pilih == "2":
                        n = input("Nama: ")
                        b = input("Barang: ")
                        t = input("Tanggal: ")
                        if n and b and t:
                            data.append({"nama": n, "barang": b, "tanggal": t})
                            print("Data ditambah!")
                        else:
                            print("Data tidak boleh kosong.")
                        input("ENTER...")

                    elif pilih == "3":
                        for i, d in enumerate(data, start=1):
                            print(f"{i}. {d}")
                        no = input("Nomor ubah: ")
                        if no.isdigit():
                            no = int(no) - 1
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
                                print("Nomor salah.")
                        else:
                            print("Harus angka.")
                        input("ENTER...")

                    elif pilih == "4":
                        for i, d in enumerate(data, start=1):
                            print(f"{i}. {d}")
                        no = input("Nomor hapus: ")
                        if no.isdigit():
                            no = int(no) - 1
                            if 0 <= no < len(data):
                                del data[no]
                                print("Data dihapus!")
                            else:
                                print("Nomor salah.")
                        else:
                            print("Harus angka.")
                        input("ENTER...")

                    elif pilih == "5":
                        break
                    else:
                        print("Pilihan salah.")
                        input("ENTER...")

                else:
                    if pilih == "1":
                        if not data:
                            print("Belum ada data.")
                        else:
                            for i, d in enumerate(data, start=1):
                                print(f"{i}. {d['nama']} meminjam {d['barang']} pada {d['tanggal']}")
                        input("ENTER...")

                    elif pilih == "2":
                        b = input("Barang: ")
                        t = input("Tanggal: ")
                        if b and t:
                            data.append({"nama": user, "barang": b, "tanggal": t})
                            print("Data ditambah!")
                        else:
                            print("Tidak boleh kosong.")
                        input("ENTER...")

                    elif pilih == "3":
                        break
                    else:
                        print("Pilihan salah.")
                        input("ENTER...")
        else:
            print("Login gagal! Username atau password salah.")
            input("ENTER untuk lanjut...")

    elif menu == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== REGISTER ===")
        u = input("Username baru: ")
        p = input("Password: ")

        if u in users:
            print("Username sudah ada.")
        elif u and p:
            users[u] = {"password": p, "role": "pengguna"}
            print("Register berhasil!")
        else:
            print("Tidak boleh kosong.")
        input("ENTER...")

    elif menu == "3":
        print("Terima kasih!")
        break
    else:
        print("Pilihan salah.")
        input("ENTER...")

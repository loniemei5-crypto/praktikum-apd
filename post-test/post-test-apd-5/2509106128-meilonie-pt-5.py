import os

users = [["meilonie", "meilonie", "meilonie"]]
data = []

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=== APLIKASI CATATAN PEMINJAMAN TEMAN KOS ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu = input("Pilih menu: ")

    if menu == "1":
        user = input("Username: ")
        pw = input("Password: ")
        login = None

        for u in users:
            if u[0] == user and u[1] == pw:
                login = u
                break

        if login is None:
            print("Login gagal!")
            input("ENTER untuk lanjut...")
        else:
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"=== MENU {login[2].upper()} ===")
                if login[2] == "meilonie":
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

                if login[2] == "meilonie":
                    if pilih == "1":
                        if len(data) == 0:
                            print("Belum ada data.")
                        else:
                            for i in range(len(data)):
                                print(f"{i+1}. {data[i][0]} meminjam {data[i][1]} pada {data[i][2]}")
                        input("ENTER...")
                    elif pilih == "2":
                        n = input("Nama: ")
                        b = input("Barang: ")
                        t = input("Tanggal: ")
                        if n and b and t:
                            data.append([n,b,t])
                            print("Data ditambah!")
                        else:
                            print("Data tidak boleh kosong.")
                        input("ENTER...")
                    elif pilih == "3":
                        for i in range(len(data)):
                            print(f"{i+1}. {data[i]}")
                        no = input("Nomor ubah: ")
                        if no.isdigit():
                            no = int(no)-1
                            if 0 <= no < len(data):
                                n = input("Nama baru: ")
                                b = input("Barang baru: ")
                                t = input("Tanggal baru: ")
                                if n and b and t:
                                    data[no] = [n,b,t]
                                    print("Data diubah!")
                                else:
                                    print("Tidak boleh kosong.")
                            else:
                                print("Nomor salah.")
                        else:
                            print("Harus angka.")
                        input("ENTER...")
                    elif pilih == "4":
                        for i in range(len(data)):
                            print(f"{i+1}. {data[i]}")
                        no = input("Nomor hapus: ")
                        if no.isdigit():
                            no = int(no)-1
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
                        if len(data) == 0:
                            print("Belum ada data.")
                        else:
                            for i in range(len(data)):
                                print(f"{i+1}. {data[i][0]} meminjam {data[i][1]} pada {data[i][2]}")
                        input("ENTER...")
                    elif pilih == "2":
                        b = input("Barang: ")
                        t = input("Tanggal: ")
                        if b and t:
                            data.append([user,b,t])
                            print("Data ditambah!")
                        else:
                            print("Tidak boleh kosong.")
                        input("ENTER...")
                    elif pilih == "3":
                        break
                    else:
                        print("Pilihan salah.")
                        input("ENTER...")

    elif menu == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== REGISTER ===")
        u = input("Username baru: ")
        p = input("Password: ")
        sudah_ada = False
        for a in users:
            if a[0] == u:
                sudah_ada = True
                break
        if sudah_ada:
            print("Username sudah ada.")
        elif u and p:
            users.append([u,p,"pengguna"])
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
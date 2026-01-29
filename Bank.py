import sys,time as t
from colorama import Fore, Style,init
init(autoreset=True)

class Bank:
    data_nasabah = 0
    data_card = {
        "Blue Card" : 5000000,
        "White Card" : 20000000,
        "Black Card" : 100000000
    }
    data_teller = {
        "AB13618" : "Stella Putri, S.E.",
        "AC14611" : "Dimas, M.E.",
        "AA11601" : "Hamengkunegoro, S.E., MBA."
    }


    def __init__(self,name1st,name2nd,tempat,tanggal,nik,alamat):
        self.nama_depan = name1st
        self.nama_belakang = name2nd
        self.nama_lengkap = (name1st+" "+name2nd).title()
        self.tempat_lahir = tempat
        self.Tanggal_lahir = tanggal
        self.nik = nik
        self.alamat = alamat
        self.saldo = 0 #saldo awal
        self.warna_kartu = ""

        Bank.data_nasabah += 1

    def creat_card_color(self):
        print("\n--- Pilih kartu ----")
        #tampilkan isi data kartu
        for key, value in Bank.data_card.items():
            print(f"-{key} (Min. Saldo : Rp{value:,})")
        pilih = input("Masukkan nama kartu (contoh: Bule Card) : ").title()
        if pilih in Bank.data_card:
            self.warna_kartu = pilih
            self.saldo = Bank.data_card[pilih]
            print(f"Berhasil! anda memilih {self.warna_kartu}. saldo awal : Rp{self.saldo:,}")
        else:
            print("Kartu tidak tersedia!")

    def creat_account_number(self):
        return f"{self.nik}{self.Tanggal_lahir}"
    
    def bank_account(self):
        print("==========Bank Account Information==========")
        print(f"Nama nasabah              : {self.nama_lengkap}")
        print(f"Tempat, tanggal lahir     : {self.tempat_lahir}, {self.Tanggal_lahir} ")
        print(f"Alamat                    : {self.alamat}")
        print("-"*46)
        print(f"Number Rekening           : {Fore.BLUE}{self.creat_account_number()}{Style.RESET_ALL}")
        print(f"Jenis kartu               : {self.warna_kartu}")
        print(f"Total saldo               : Rp{self.saldo:,}") 
        print("-"*46)

    def deposit(self):
        tambah = int(input("Masukkan jumlah uang yang ignin ditabung : "))
        if tambah > 0:
            self.balance_update(tambah)
            print(f"Setoran berhasil!  saldo bertambah Rp{tambah:,}")
        else:
            print("Jumlah tidak valid!")

    def withdraw(self):
        tarik = int(input("Masukkan jumlah uang yang ingin diambil : "))
        if tarik > self.saldo:
            print("Maaf, saldo tidak mencukupi")
        else:
            self.balance_update(-tarik)#angka negatif untukmpenarikan
            print(f"Penarikan berhasil! anda mengambil uang Rp{tarik:,}")
    def balance_update(self,amount):
        self.saldo += amount

def checking_options(pesan):
    return input(f"{pesan} (Y/N) : ").strip().lower() == 'y'

def user():
    nasabah_baru = None
    
    while True:
        print("\n"+" "*5+"=== MENU BANK ===")
        print("1. Buat akun baru")
        print("2. Tambah uang (deposit)")
        print("3. Ambil uang (withdraw)")
        print("4. Lihat informasi & saldo")
        print("5. Jumlah nasabah (khusus teller)")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6) : ")

        if pilihan == "1":
            if not checking_options("Apakah anda ingi membuat account?"):continue
            print("Silahkan isi data diri")
            t.sleep(1)
            nama_depan = input("Nama depan : ")
            nama_belakang = input("Nama belakang : ")
            tempat = input("Tempat lahir : ").title()
            tanggal = input("Tanggal lahir (DDMMYY) : ")
            nik = input("NIK : ")
            alamat = input("Alamat : ").title()
            nasabah_baru = Bank(nama_depan,nama_belakang,tempat,tanggal,nik,alamat)
            nasabah_baru.creat_card_color()
            t.sleep(1)
            nasabah_baru.bank_account()

        elif pilihan == "2":
            if not checking_options("Apakah anda ingi membuat menambah saldo?"):continue
            print("Silahkan isi jumlah saldo yang ingin ditambahkan")
            t.sleep(1)
            if nasabah_baru:
                cek = input("Masukkan Number Account Anda: ")
                # Kita langsung cek number account
                if cek == nasabah_baru.creat_account_number():
                    nasabah_baru.deposit()
                else:
                    print("Nomor rekening salah! Akses ditolak.")
            else:
                print("Belum ada akun terdaftar!")

        elif pilihan == "3":
            if not checking_options("Apakah anda ingin mengambil uang?"):continue
            print("Silahkan isi berepa jumlah uang yang ingin anda tarik")
            t.sleep(1)
            if nasabah_baru:
                cek = input("Masukkan Number Account Anda: ")
                # Kita langsung cek number account
                if cek == nasabah_baru.creat_account_number():
                    nasabah_baru.withdraw()
                else:
                    print("Nomor rekening salah! Akses ditolak.")
            else:
                print("Belum ada akun terdaftar!")

        elif pilihan == "4":
            if not checking_options("Apakah anda ingi melihat info bank accoun anda?"):continue
            print("Silahkan masukkan nomor rekening anda")
            t.sleep(1)
            if nasabah_baru:
                cek = input("Masukkan Number Account Anda: ")
                # Kita langsung cek number account
                if cek == nasabah_baru.creat_account_number():
                    nasabah_baru.bank_account()
                else:
                    print("Nomor rekening salah! Akses ditolak.")
            else:
                print("Belum ada akun terdaftar!")

        elif pilihan == "5":
            if not checking_options("Apakah anda teller?"):continue
            print("Silahkan inpu ID anda")
            cek_id = input("Masukkan ID anda : ")
            if cek_id in Bank.data_teller:
                print(f"ID ditemukan, selamat datang Bapak/Ibu {Bank.data_teller[cek_id]}")
                print(f"ini adalah jumlah nasabah : {Bank.data_nasabah}")
            else:
                print("ID teller tidak ditemukan!akses ditolak")

        elif pilihan == "6":
            print("Trima kasih")
            sys.exit()
        else:
            print("Pilihan tidak ada")
if __name__ == "__main__":
    user()
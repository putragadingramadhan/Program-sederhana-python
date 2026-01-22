from colorama import Fore, Style, init
init(autoreset=True)
import time as t
class guru :
    data_tecther = 0

    def __init__(self,nama,id):
        self.nama_guru = nama
        self.id_guru = id

        guru.data_tecther += 1
        

    def tampilkan(self):
        t.sleep(0.5)
        print("===Data Guru===")
        print(f"Nama Guru   : {self.nama_guru}")
        print(f"Id Guru     : {self.id_guru}")

class Siswa:
    data_siswa = 0

    def __init__(self,nama,nisn,ips,ipa,mtk):
        self.nama = nama
        self.NISN = nisn
        self.nilai_ips = ips
        self.nilai_ipa = ipa
        self.nilai_mtk = mtk

        Siswa.data_siswa +=1

    def show_data(self):
        print("==Data siswa==")
        print(f"Nama siswa   : {self.nama}")
        print(f"NISN         : {self.NISN}")
        print(f"Nilai IPS    : {self.nilai_ips}")
        print(f"NIlai IPA    : {self.nilai_ipa}")
        print(f"Nilai MTK    : {self.nilai_mtk}")

    def total_value(self):
        return (self.nilai_ips + self.nilai_ipa + self.nilai_mtk)/3
    
    def status_lulus(self):
        if self.total_value()>= 75.00:
            return f"Dinyatakan {Fore.BLUE}Lulus{Style.RESET_ALL}"
        else:
            return f"Dinyatakan {Fore.RED}Tidak Lulus{Style.RESET_ALL}"
    
    def show_total_value(self):
        print("\n===NIlai Siswa===")
        print(f"Nama siswa      : {self.nama}")
        print(f"NISN            : {self.NISN}")
        print(f"Nilai IPS       : {self.nilai_ips}")
        print(f"NIlai IPA       : {self.nilai_ipa}")
        print(f"Nilai MTK       : {self.nilai_mtk}")
        print(f"Nilai Rata-rata : {self.total_value():.2f}")
        print(f"Status          : {self.status_lulus()}")

def tampilakn():
    data_siswa = []
    data_guru = []

    while True:
        for i in range(3,0,-1):
            print(i)
            t.sleep(1)
        print("\n"+"="*40)
        print("===Silahkan pilih menu===")
        t.sleep(1)
        print("1. Sebagai Guru")
        print("2. Sebagai Siswa")
        print("3. Keluar")
        print("="*40)
        t.sleep(0.3)

        try:
            pilihan = int(input("Silahkan pilih menu (1-3): "))

            if pilihan == 1 :
                if input("Apakah anda yakin (Y/N) : ").lower().strip() not in ("yes","y"):
                    continue
                print("Silahkan input data guru terlebih dahulu")

                nama_guru = input("Nama guru : ")
                try:
                    id_guru = int(input("ID guru : "))

                    sip = guru(nama_guru,id_guru)
                    data_guru.append(sip)
                    sip.tampilkan()
                    t.sleep(2)
                except ValueError:
                    print(Fore.RED,"Mohon masukkan id dengan angka!",Style.RESET_ALL)
                print(f"Baik Bapak/Ibu {nama_guru}, silahkan isi data siswa")
                t.sleep(0.5)

                #input data siswa
                nama_siswa = input("\nNama siswa : ")
                try:
                    nisn_siswa = int(input("NISN siswa : "))
                    nilai_ips = int(input("NIlai IPS : "))
                    nilai_ipa = int(input("Nilai IPA : "))
                    nilai_mtk = int(input("Nilai MTK : "))
                    simpan = Siswa(nama_siswa,nisn_siswa,nilai_ips,nilai_ipa,nilai_mtk)
                    data_siswa.append(simpan)
                    simpan.show_data()
                except ValueError:
                    print(Fore.RED,"Mohon masukkan angka",Style.RESET_ALL)
                print(f"Terima kasih Bapak/Ibu {nama_guru} yang sudah input data siswa")

            elif pilihan == 2:
                if input("Apakah anda yakin (Y/N) : ").strip().lower() not in ("yes","y"):
                    continue

                nisn = int(input("Silahkan masukkan NISN : "))
                ssw = next((s for s in data_siswa if s.NISN == nisn),None)
                if ssw:
                    print(Fore.GREEN,"NISN siswa ditemukan",Style.RESET_ALL)
                    ssw.show_total_value()
                else:
                    print(Fore.RED,"NISN tidak ditemukan",Style.RESET_ALL)
                
            elif pilihan == 3:
                if input("Apakah anda yakin (Y/N) : ").strip().lower() not in ("yes","y"):
                    continue
                print("Terima kasih telah menggunakan layanan kami")
                break
            
            else:
                print("Pilihan tidak ditemukan")
                break
        except ValueError:
            print("Mohon masukkan angka")

if __name__ =="__main__":
    tampilakn()
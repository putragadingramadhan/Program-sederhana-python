from colorama import Fore, Style, init
init(autoreset=True)
import time as t
import os
import json

class Siswa:
    data_siswa = 0

    def __init__(self,nama,nisn,ips,ipa,mtk):
        self.nama = nama
        self.NISN = nisn
        self.nilai_ips = ips
        self.nilai_ipa = ipa
        self.nilai_mtk = mtk
        self.nilai = {"IPS" : ips, "IPA" : ipa, "MTK" : mtk}

        Siswa.data_siswa +=1

    def show_data(self):
        print("==Data siswa==")
        print(f"Nama siswa   : {self.nama}")
        print(f"NISN         : {self.NISN}")
        print(f"Nilai IPS    : {self.nilai_ips}")
        print(f"NIlai IPA    : {self.nilai_ipa}")
        print(f"Nilai MTK    : {self.nilai_mtk}")

    def total_value(self):
        return sum(self.nilai.values())/len(self.nilai)
    
    def status_lulus(self):
        if self.total_value()>= 75.00:
            return f"Dinyatakan {Fore.BLUE}Lulus{Style.RESET_ALL}"
        else:
            return f"Dinyatakan {Fore.RED}Tidak Lulus{Style.RESET_ALL}"
    
    def show_total_value(self,rank):
        print("\n===NIlai Siswa===")
        print(f"Nama siswa      : {self.nama}")
        print(f"NISN            : {self.NISN}")
        print("-"*28)
        for mapel, skor in self.nilai.items():
            print(f"Nilai {mapel:<10} : {skor}")
        print("-"*28)
        print(f"Nilai Rata-rata : {self.total_value():.2f}")
        print(f"Status          : {self.status_lulus()}")
        color_rank = Fore.CYAN if rank <= 3 else Fore.WHITE
        print(f"Rangking ke-      : {color_rank}{rank} dari {Siswa.data_siswa} siswa")
        print(f"{Fore.YELLOW}=================\n")

def tampilkan_rangking(nisn_target,data_siswa):
    urutan_rangking = sorted(data_siswa, key=lambda s: s.total_value(), reverse=True)
    for index, siswa in enumerate(urutan_rangking):
        if siswa.NISN == nisn_target:
            return index + 1
        return None
    
def simpan_ke_file(data_siswa, nama_file = "Database_siswa.txt"):
    try:
        with open(nama_file, "w") as f:
            data_terstruktur = []
            for s in data_siswa:
                data_terstruktur.append({
                    "nama" : s.nama,
                    "nisn" : s.NISN,
                    "ips" : s.nilai_ips,
                    "ipa" : s.nilai_ipa,
                    "mtk" : s.nilai_mtk
                })
                json.dump(data_terstruktur,f)
    except Exception as e:
        print(f"Gagal menyimpan data : {e}")

def muat_dari_file(nama_file = "database_siswa.txt"):
    if not os.path.exists(nama_file):
        return []
    
    try:
        with open(nama_file, "r")as f:
            data_load = json.load(f)
            data_siswa =[]
            for d in data_load:
                siswa_obj = Siswa(d['nama'], d['nisn'], d['ips'], d['ipa'], d['mtk'])
                data_siswa.append(siswa_obj)
            return data_siswa
    except:
        return[]
    
def ge_input_konfirmasi (pesan):
    return input(f"{pesan} (Y/N) : ").strip().lower()=='y'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#data teacther
data_teacther = {
        "A22411" : "Arnanda raenaldi, S.Kom.",
        "A22412" : "Muhammad Rifqi Atsani, M.Kom.",
        "B22413" : "Atipa Muji, M.Kom",
        "B22414" : "Wakhidin, S.Pd."
}
def tampilakn():
    data_siswa = muat_dari_file()

    while True:
        for i in range(3,0,-1):
            print(i)
            t.sleep(1)
        print("\n"+"="*40)
        print("===Silahkan pilih menu===")
        t.sleep(0.5)
        print("1. Sebagai Guru")
        print("2. Sebagai Siswa")
        print("3. Keluar")
        print("="*40)
        t.sleep(0.3)

        try:
            pilihan = int(input("Silahkan pilih menu (1-3): "))

            if pilihan == 1 :
                if not ge_input_konfirmasi("Apakah anda guru?"): continue
                print("Silahkan input ID guru : ")

                cek_id_guru = input("Masukkan ID guru : ")
                if cek_id_guru in data_teacther:
                    print(f"ID guru ditemukan : {data_teacther[cek_id_guru]}")
                    print("Silahkan input data siswa")
                else:
                    print(f"ID guru {Fore.RED}tidak ditemukan{Style.RESET_ALL}")
                    continue

                #input data siswa
                nama_siswa = input("\nNama siswa : ")
                try:
                    nisn_siswa = int(input("NISN siswa : "))
                    nilai_ips = int(input("NIlai IPS : "))
                    nilai_ipa = int(input("Nilai IPA : "))
                    nilai_mtk = int(input("Nilai MTK : "))
                    simpan = Siswa(nama_siswa,nisn_siswa,nilai_ips,nilai_ipa,nilai_mtk)
                    data_siswa.append(simpan)
                    simpan_ke_file(data_siswa)
                    simpan.show_data()
                    print(f"Data berhasil disimpan ke file!")
                except ValueError:
                    print(Fore.RED,"Mohon masukkan angka",Style.RESET_ALL)
                print(f"Terima kasih Bapak/Ibu {data_teacther[cek_id_guru]} yang sudah input data siswa")

            elif pilihan == 2:
                if not ge_input_konfirmasi("Apakah anda siswa?"): continue
                nisn = int(input("Silahkan masukkan NISN : "))
                ssw = next((s for s in data_siswa if s.NISN == nisn),None)
                if ssw:
                    print(f"{Fore.GREEN}NISN siswa ditemukan{Style.RESET_ALL}")
                    rank = tampilkan_rangking(nisn,data_siswa)
                    ssw.show_total_value(rank)
                else:
                    print(f"{Fore.RED}NISN siswa tidak ditemukan{Style.RESET_ALL}")
                
            elif pilihan == 3:
                if not ge_input_konfirmasi("Apakah anda yakin?"): continue
                print("Terima kasih telah menggunakan layanan kami")
                break
            
            else:
                print(f"Pilihan {Fore.RED}tidak{Style.RESET_ALL} ditemukan")
                break
        except ValueError:
            print("Mohon masukkan angka")

if __name__ == "__main__":
    tampilakn()
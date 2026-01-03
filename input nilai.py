
class Dosen:
    data_mahasiswa = 0
    def __init__(self,nama,nim,kelas,matkul,kehadiran,uts,uas):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.namaMatkul = matkul
        self.kehadiran = kehadiran
        self.uts = uts
        self.uas = uas

        Dosen.data_mahasiswa += 1
        
    def Tampil_data_mentah(self):
        print(f"Nama               : {self.nama}")
        print(f"NIM                : {self.nim}")
        print(f"Kelas              : {self.kelas}")
        print(f"Mata kuliah        : {self.namaMatkul}")
        print(f"Nilai Kehadiran    : {self.kehadiran}")
        print(f"Nilai UTS          : {self.uts}")
        print(f"Nilai UAS          : {self.uas}")

    def Konversi_nilai(self):
        Kehadiran = (self.kehadiran*10)/100
        UtS = (self.uts*40)/100
        UaS = (self.uas*50)/100
        
        koversi = Kehadiran+UtS+UaS
        return koversi

    def tampilkan_nilaiALLA_matkl(self):
        print("====NILAI MATKUL====")
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Matkul  : {self.namaMatkul}")
        print(f"Nilai   : {self.Konversi_nilai()}")

def master():
    data_mahasiswa = []
    while True:
        print("\n"+"="*40)
        print("Silahkan pilih menu")
        print("1. Dosen")
        print("2. Mahasiswa")
        print("3. Keluar")
        print("="*40)
        try:
            pilihan = int(input("Silahkan pilih menu (1-3) : "))

            if pilihan == 1 :
                cek = input("Apakan anda yakin memilih menu ini (True/False) : ")
                if cek == "False":
                    continue
                else:
                    print("Silahkan lanjutkan ke pengisian data")

                
                nama_mhs = input("Nama mahasiswa : ")
                nim_mhs = input("Nim mahasiswa : ")
                kelas_mhs = input("Kelas mahasiswa : ")

                print("Data mahasiswa berhasil tersimpan!silahkan input nilai")
                nama_mtkl = input("Nama mata kuliah : ")
                
                try:
                    nilai_kehadiran = int(input("Nilai kehadiran : "))
                    nilai_uts = int(input("Nilai uts : "))
                    nilai_uas = int(input("Nilai UAS : "))
                except ValueError:
                    print("Silahkam masukkan angka")

                simpan = Dosen(nama_mhs,nim_mhs,kelas_mhs,nama_mtkl,nilai_kehadiran,nilai_uts,nilai_uas)
                data_mahasiswa.append(simpan)
                print("\nData berhasil disimpan")
                simpan.Tampil_data_mentah()

            elif pilihan == 2 :
                cek = input("Apakan anda yakin memilih menu ini (True/False) : ")
                if cek == "False":
                    continue
                else:
                    print("Berikut data diri anda")

                cek_NIM = input("Masukkan NIM anda : ")
                for mhs in data_mahasiswa:
                    if mhs.nim == cek_NIM:
                        mhs.tampilkan_nilaiALLA_matkl()
                        break
                    else:
                        print("NIM anda tidak ditemukan")
                        continue
            elif pilihan == 3:
                print("Terima kasih telah menggunakan layanan kami")
                break
        except ValueError : 
            print("Mohon masukkan angka")
master()




    

    
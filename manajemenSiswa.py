class Siswa : 

    def __init__(self,nama,kelas,nilai):
        self.nama = nama
        self.kelas = kelas
        self.nilai = nilai

    def tampilkanSiswa_sementara(self):
        return f"Berikut adalah daftar siswa sementara :\nNama : {self.nama} | Kelas {self.kelas} | Nilai {self.nilai}"

    def tampilkanSiswa(self):
        return f"Berikut adalah daftar siswa saat ini :\nNama : {self.nama} | Kelas {self.kelas} | Nilai {self.nilai}"
    

class Sekolah :

    def __init__(self):
        self.Daftar_siswa = [] 

    def tambah_siswa(self,tambah):#menambahkan data siswa
        self.Daftar_siswa.append(tambah)

    def tampilkan_siswa(self):
        if len(self.Daftar_siswa )==0:
            return "belum ada daftar siswa"
        data = "Data siswa\n"
        for j in self.Daftar_siswa:
            data += "-" + j.tampilkanSiswa_sementara()+ "\n"
            data += "-" +j.tampilkanSiswa()+"\n"
        return data
    
def master():
    dataSISWA_sementara = Sekolah()
    while True:
        print("\n"+"*"*40)
        print("Daftra menu")
        print("1. Masukkan daftar siswa")
        print("2. Tambah siswa")
        print("3. Cetak daftra siswa")
        print("4. Keluar")

        try:
            pilihan = int(input("Silahkan pilih daftar menu diatas (1-4) : "))

            if pilihan == 1 :
                #konfirmasi kembali pilihan user
                print("Anda memilih menu 'Masukkan daftar siswa' ")
                cek = str(input("Apakah benar?(True/False) : "))
                if cek == "True":
                    print("Anda telah konfirmasi, silahkan lanjutkan pendataan siswa")
                elif cek != "True":
                    print("Pendataan siswa dibatalkan")
                    continue

                nama_siswa = input("Masukkan nama siswa : ")
                kelas = input("Kelas : ")
                nilai = input("Masukkan nilai akhir : ")

                
                simpan = Siswa(nama_siswa,kelas,nilai)
                dataSISWA_sementara.tambah_siswa(simpan)
                

            elif pilihan == 2 :
                #konfirmasi kembali pilihan user
                print("Apakah anda memilih menu 'Tambah siswa'?")
                cek = str(input("Apakah benar?(True/False) : "))
                if cek == "True":
                    print("Anda telah konfirmasi, silahkan lanjutkan pendataan siswa")
                elif cek != "True":
                    print("Pendataan siswa dibatalkan")
                    continue
                
                namaSISWA_tambahan = input("Nama siswa tambahan  : ")
                kelas_tambahan = input("kelas : ")
                nilai_tambahan = input("Nilai akhir : ")

                simpen = Siswa(namaSISWA_tambahan,kelas_tambahan,nilai_tambahan)
                dataSISWA_sementara.tambah_siswa(simpen)

                print("Data siswa baru berhasil ditambahkan!!")

            elif pilihan == 3:
                #konfirmasi kembali pilihan user
                print("Apakah anda memilih menu 'Tampilkan data siswa'?")
                cek = str(input("Apakah benar?(True/False) : "))
                if cek == "True":
                    print("Anda telah konfirmasi, silahkan lanjutkan pendataan siswa")
                elif cek != "True":
                    print("Pendataan siswa dibatalkan")
                    continue
                #cek apakah sudah ada daftar siswa
                if dataSISWA_sementara== None:
                    print("Anda belum memasukkan data siswa!!")
                    continue
                else:
                    print("Berikut daftar siswa")
                #cetak data siswa 
                print(dataSISWA_sementara.tampilkan_siswa())
            
            elif pilihan == 4:
                print("Terima kasih telah memilih layanan kami")
                break
            else:
                print("pilihan menu tidak ada!!")
        except ValueError:
            print("Mohon masukkan angka!")
master()

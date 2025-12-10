"""Buatlah sebuah program dengan kasus sebagai berikut
Sebuah universitas X membutuhkan program untuk menghitung nilai akhir mahasiswa berdasarkan komponen berikut : tugas 20%, uts 30% , uas 50% setelah di hitung nilai akhir program harus menentukan grade dengan ketentuan
A 85-100
B 70-84
C 55-69
D 40-54
E < 40"""


class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan


class Nilai:
    universitas = 'Universitas X'

    def __init__(self, tugas, uts, uas):
        self.tugas_asli = tugas
        self.uts_asli = uts
        self.uas_asli = uas

        self.tugas = (tugas * 20) / 100
        self.uts   = (uts * 30) / 100
        self.uas   = (uas * 50) / 100

    def total_nilai(self):
        return self.tugas + self.uts + self.uas

    def konversi(self):
        total = self.total_nilai()
        
        if total >= 85:
            return "A"
        elif total >= 70:
            return "B"
        elif total >= 55:
            return "C"
        elif total >= 40:
            return "D"
        else:
            return "E"


def main():
    data_mhs = None
    nilai_mhs = None

    while True:
        print("\n== MENU NILAI MAHASISWA ==")
        print("1. Isi biodata mahasiswa")
        print("2. Input nilai mahasiswa")
        print("3. Konversi nilai mahasiswa")
        print("4. Keluar")

        pilihan = int(input("Pilih menu (1-4): "))

        if pilihan == 1:
            nama = input("Nama: ")
            nim = input("NIM: ")
            jurusan = input("Jurusan: ")

            data_mhs = Mahasiswa(nama, nim, jurusan)
            print("Biodata tersimpan!", data_mhs)

        elif pilihan == 2:
            nilai_tugas = int(input("Nilai tugas: "))
            nilai_uts = int(input("Nilai UTS: "))
            nilai_uas = int(input("Nilai UAS: "))

            nilai_mhs = Nilai(nilai_tugas, nilai_uts, nilai_uas)
            print("Nilai tersimpan!")

        elif pilihan == 3:
            if nilai_mhs is None:
                print("Anda belum mengisi nilai!")
                continue

            total = nilai_mhs.total_nilai()
            grade = nilai_mhs.konversi()

            print(f"Total nilai akhir: {total:.2f}")
            print(f"Grade: {grade}")

        elif pilihan == 4:
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak tersedia!")
            

main()


    


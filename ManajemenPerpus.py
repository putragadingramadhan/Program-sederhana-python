"""
Buat program OOP yang dapat:
Menambah buku baru (judul, penulis, tahun)
Meminjam buku
Mengembalikan buku
Menampilkan daftar buku beserta statusnya (dipinjam / tersedia)
Gunakan minimal:
Class Buku
Class Perpustakaan
"""
class Buku():
    def __init__(self, judul, penulis, TahunTerbit):
        self.judul = judul
        self.penulis = penulis
        self.TahunTerbit = TahunTerbit
        self.status = "tersedia"   # tambahan status

    def cetak(self):
        return f"{self.judul} | {self.penulis} | {self.TahunTerbit} | status: {self.status}"


class Perpustakaan():
    def __init__(self):
        self.daftar_buku = []

    def tambah(self, buku):
        self.daftar_buku.append(buku)

    def nyilih(self, judul):
        for b in self.daftar_buku:
            if b.judul.lower() == judul.lower():
                if b.status == "tersedia":
                    b.status = "dipinjam"
                    return f"Buku '{judul}' berhasil dipinjam"
                else:
                    return f"Buku '{judul}' sedang dipinjam"
        return f"Buku '{judul}' tidak ditemukan"

    def balekna(self, judul):
        for b in self.daftar_buku:
            if b.judul.lower() == judul.lower():
                if b.status == "dipinjam":
                    b.status = "tersedia"
                    return f"Buku '{judul}' berhasil dikembalikan"
                else:
                    return f"Buku '{judul}' tidak sedang dipinjam"
        return f"Buku '{judul}' tidak ditemukan"

    def tampil(self):
        print("\nDaftar Buku Saat Ini:")
        for b in self.daftar_buku:
            print(" -", b.cetak())


# ================== PROGRAM UTAMA ==================

def main():
    perpustakaan = Perpustakaan()

    # data awal sesuai gaya kamu
    perpustakaan.tambah(Buku("Rich Dad Poor Dad", "Robert T Kiyosaki", 1989))
    perpustakaan.tambah(Buku("The Atomic Habits", "James Clear", 1999))

    while True:
        print("\n" + "="*40)
        print('Pilih Menu')
        print('1. Menambah buku baru')
        print('2. Pinjam Buku')
        print('3. Mengembalikan buku')
        print('4. Menampilkan daftar buku dan status')
        print('5. Keluar')
        print("="*40)

        try:
            pilihan = int(input("Silahkan pilih menu (1-5) : "))

            if pilihan == 1:
                Judul = input("Judul buku : ")
                nama_penulis = input('Nama penulis : ')
                tahunTerbit = int(input("Tahun terbit : "))
                data_buku = Buku(Judul, nama_penulis, tahunTerbit)

                perpustakaan.tambah(data_buku)
                print("\nData buku berhasil tersimpan!")
                perpustakaan.tampil()

            elif pilihan == 2:
                Judul_pinjam = input("Judul buku yang mau dipinjam : ")
                output = perpustakaan.nyilih(Judul_pinjam)
                print(output)

            elif pilihan == 3:
                balekna_judul = input('Judul buku yang ingin dikembalikan : ')
                keluaran = perpustakaan.balekna(balekna_judul)
                print(keluaran)

            elif pilihan == 4:
                perpustakaan.tampil()

            elif pilihan == 5:
                print("anda keluar")
                break

            else:
                print("Pilihan tidak ada!")

        except ValueError:
            print('mohon masukkan angka')

main()


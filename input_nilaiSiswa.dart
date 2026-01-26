import 'dart:io';

class Guru {
  static int data_guru = 0;

  String nama_guru;
  int id_guru;

  Guru(this.nama_guru, this.id_guru) {
    data_guru += 1;
  }
  void tampilkan() {
    print("\n===Data Guru===");
    print("Nama Guru    : $nama_guru");
    print("ID Guru      : $id_guru");
  }
}

class Siswa {
  static int data_siswa = 0;
  String nama;
  int NISN;
  int nilai_ips;
  int nilai_ipa;
  int nilai_mtk;

  Siswa(this.nama, this.NISN, this.nilai_ips, this.nilai_ipa, this.nilai_mtk) {
    data_siswa += 1;
  }

  void show_data() {
    print("===Data Siswa===");
    print("Nama Siswa   : $nama");
    print("NISN         : $NISN");
    print("Nilai IPS    : $nilai_ips");
    print("Nilai IPA    : $nilai_ipa");
    print("Nilai MTK    : $nilai_mtk");
  }

  total_value() {
    return (nilai_ips + nilai_ipa + nilai_mtk) / 3;
  }

  status_lulus() {
    if (total_value() >= 75.00) {
      return "Lulus";
    } else {
      return "Tidak Lulus";
    }
  }

  void show_value() {
    print("===Data Siswa===");
    print("Nama Siswa      : $nama");
    print("NISN            : $NISN");
    print("Nilai IPS       : $nilai_ips");
    print("Nilai IPA       : $nilai_ipa");
    print("Nilai MTK       : $nilai_mtk");
    print("Nilai Rata-Rata : $total_value()");
    print("Status          : $status_lulus()");
  }
}

void main() {
  List<Siswa> data_siswa = [];
  List<Guru> data_guru = [];

  while (true) {
    print("\n==========");
    print("1. Sebagai Dosen");
    print("2, Sebagai siswa");
    print("3. Keluar");
    print("==========");

    stdout.write("Silahkan pilih menu (1-3): ");
    String? input = stdin.readLineSync();
    int? Pilihan = int.tryParse(input ?? "");

    if (Pilihan == null) {
      print("Mohon masukkan angka");
      continue;
    } else if (Pilihan == 1) {
      stdout.write("Apakah anda yakin (Y/N) : ");
      if (stdin.readLineSync() == "False") continue;

      print("Silahkan isi data guru");
      stdout.write("Nama guru : ");
      String NAMA_guru = stdin.readLineSync() ?? "";
      stdout.write("ID guru : ");
      int? ID_guru = int.tryParse(stdin.readLineSync() ?? "");
      if (ID_guru == null) {
        print("ID guru harus berupa angka");
      }
      Guru simpan = Guru(NAMA_guru, ID_guru);
      data_guru.add(simpan);
    }
  }
}

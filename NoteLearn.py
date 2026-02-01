#latihan
#this is a comment
"""another comment"""
#string
nama = 'gading'
print(nama,type(nama))
#Integer
umur = 18
print(umur,type(umur))
#bool
mahasiswa = True
print(mahasiswa,type(mahasiswa))
#Float
berat_badan = 90.8
print(berat_badan,type(berat_badan))
#none
nilai = None
print(nilai,type(nilai))
#list
Hewan_Peliharaan = ['kucing','gajah', 'harimau']
print(Hewan_Peliharaan,type(Hewan_Peliharaan))
#set
Nama_makanan = {'berger','nasi padang','mie ayam','bakso' }
print(Nama_makanan,type(Nama_makanan))
#tuple
Nama_orang = ('galih', 'amggit','ardi','maman')
print(Nama_orang,type(Nama_orang))
print(f'===print===')
print(f'nama saya {nama}, umur saya {umur}, berat badan saya{berat_badan}, saya adalah mahasiswa {mahasiswa}, hewan peliharaan saya {Hewan_Peliharaan}, nilai ujian saya{nilai}, nama teman saya{Nama_orang}')

"""konversi ke tipe data lain"""
print('==koversi tipe data==')
"""penggunaan python
1. web defelopment
2. software development
3. mathematical cumputasi
4. system scripting
5. microcontroller programing (micro-python)

keuntungan python
1. cross-platfrom compatibilty
2. simpel syntax
3. efficiency
4. rapid prototyping

penting!
python menggunakan baris baru untuk menyelesaikan perintah, berbeda dengan bahasa lain yang sering menggunakan (;)
python mengandalkan indentasi, menggunakan spasi untuk mendefinisikan ruang lingkup
setiap kali anda selesai dibaris perintah python, anda cukup mengetik yang berikut ini untuk keluar dari baris"""
if 5<2:
    print('five is greater than two!')
if 5<2:
    print('five is greater thab two!')
print('==operasi komparasi bool==')


#17 september 2025
"""materi tentang tanda petik (' ')dan (" ")"""
#contoh
n = "fad'li"
"""mas fad'li datang"""
"""jika memiliki kumpulan nilai dalam list, tuple,dll.python
memungkinkan anda mengestrak nilai kedalam variabel. ini disebut membongkar/lupping"""
print('nama saya'+n)

nama = "budi"+"pambudi" #akan menggabungkan nilai
print(nama)
umur = 17+8
print(umur)
#didalam python string adalah array
print(len(nama))#akan muncul jumlah huruf dari str
#dalam fungsi len, spasi ( ) akan dihitung sabagi karakter

z = "xaxa" + "baik"
print(len(z))

print("==modifikasi string==")
print('agar menjadi huruf besar semua, kita pakai variabel.upper. contoh',nama.upper())#operasi ini dinamakan method
print('agar menjadi huruf kecil semua, kita pakai variabel.lower. contoh',nama.lower())
print('agar menjadi huruf kapital di awal kalimat, kita pakai variabel.capitalize. contoh',nama.capitalize())
print('agar menjadi huruf kapital di setiap awal kata, kita pakai variabel.title. contoh',nama.title())

print("==menghapus spasi==")
nama1 = " sobirin sobirun"
print(nama.strip())
print(nama.rstrip())
print(nama.lstrip())

print('==mereaplace (mengganti) string==')
print(nama1.replace(' ','+'))

print('==menggabungkan string==')
#joint, memisahkan split
nama3 = ' sobirin birun'
print(nama3.split())#akan menjadi data list
# () disebut dengan delimiter
buah = ['apel','jeruk','mangga']
gabung = '-'.join(buah)
print(gabung)#manjadi apel-jeruk-mangga
print('jika kikta memakai delimiter yang ada, maka hasilnya',nama1.split(' '))#(' ')disebut dengan delimiter
print('jika kikta memakai delimiter yang tidak ada, maka hasilnya',nama1.split('z'))
#delimiter adalah
#menggabungkan string (jika str nya banyak)
kewan = ['kucing',',','harimau',',','ayam',',','kambing']
#print('menggunakan delimiter koma :'",".joint(kewan),"only valiabel list")#menulis delimiter-nya didepan
#menggabungkan method w/(.)
m = "nama saya gading"
print(m.upper().lstrip().split())
#format string
print('nama saya',m)
print('fungsi format =' f"nama saya{m}umur saya {umur}")


#Senin, 6 oktober 2025
m = int(input('masukkan nilai integer = '))
"""
def (nama function) parameter :
    isi funtion
print dengan nama fantion (argument)"""
def angka_ganjil_genap (m): #(m) adalah parameter
    if m %2 == 0 :
        print("angka genap")
    elif m != 0:
        print('angka genajil')
angka_ganjil_genap(m)#(m)adalah argument
#print---->untuk mencetak
#retrunt-->mengembalikan nilai
"""function arbitrary arguments"""
#dengan cara menambahkan (*)di depan nama variabel
def hitung_gangil_genap_all(*a):#parameter *a menunjukkan bahwa tipe datanya adalah list
    #(*a) tanda (*) namanya adalah arbitrairy
    #tipe data list,jika ingin menggunakan data didalmmnya harus menggunakan loop
    for angka in a :#for adalah loop
        if angka%2==0:
             print('angka genap',angka)
        else:
            print('angka ganjil',angka)
hitung_gangil_genap_all()

"""belanja = ['sampo','sabun','pasta gigi']
for barang in belanja:"""

"""variabel lokal, hanya variabel yang dikenali dalam satu blok code saja
variabel global, bisa dikenali dalam semua blok code"""

#13 Oktober 2025
#tipe data list
"""contoh
list_dari_str= ("python")--> ['p','y','t','h','o','n']
list_dari_range = list(range(5))-->[0,1,2,3,4]
angka = list(15)--> 0 sampai 14
"""
#mengakses element list
#1. Akses dengan indeks
buah = ['apel','jeruk','mangga','pisang']
#print(nama variabel[no indeks])
print(buah[0])#indeks mulai dari 0, bukan 1
print(buah[2])#indeks sampai dari jmlh data dikurang 1, 
print(buah[-1])#pakai (-1) untuk indeks terakhir

#2. Slicing (pemotongan)
angka = [0,1,2,3,4,5,6,7,8,9]
print(angka[2:5])#artinya dimulai dari indeks ke 2 sampai ke 5
print(angka[:3])#dari ideks <3 (0,1,2)
print(angka[5:])#[5,6,7,8,9]
print(angka[::2])#stiap du langkah [0,2,4,6,8]

#operasi dasar pada list
buah = ['apel','jeruk']
#append()-menambah diakhir
buah.append('mangga')
print(buah)
#insert()-menambahkan di posisi tertendu
buah2 = ['apel','jeruk']
buah2.insert(1,'pisang')
print(buah2)

#2. menghapus element
buah = ['apel','jeruk','mangga','pisang']
#remove()- hapus berdasarkan nilai
print(buah.remove('jeruk'))

#pop()-hapus berdasarkan indeks(default:elemen terakhir)
print(buah.pop(1))

#clear()-hapus semua elemen
print(buah.clear())

"""method pada list"""
print('==method pada list==')
angka = [3,1,4,1,5,9,2]
#len()-menghitung panjang list
print(len(angka))
#count()-hitung kemunculan nilai
print(angka.count(1))
#index()- cari posisi nilai
print(angka.index(4))
#copy()-buat salinan list
angka_salinan = angka.copy()

#modifikasi dengan lower
for keranjang in buah:
    print(keranjang.upper())

"""return
kegunaannya untuk mmenghentikan sebuah eksekusi dari fungsi, 
dan mengirimkannya kembali sebuah nilai(atau objek) ke bagian code yang memanggilnya"""
def tambah_angka(a,b):
    hasil = a+b
    return hasil#di function biasanya dia mengembalikan nilai
nilai=tambah_angka(4,2)

def pengurangan (a,b):
    hasilKurang = a-b
    return hasilKurang
nilai2=pengurangan(5,3)
Hasil_Bagi = nilai/nilai2
print(Hasil_Bagi)

#balajar mandiri
#function tanpa return
def hitung (a=10,b=5):
    print(a)
    print(b)
hitung(b=15,a=20)
#dia hanya sekedar print biasa

#retunr akan mengebalikan nilai tertentu dari fungsi return tertentu
def hitung(a,b):
   # print(a+b)
    print('sebelum return')
    return a+b#karakteristiknya, dia akan mengeksekusi kode sebelumya, tidak dengan setelahnya
    print('setelah return')#pernyataan setelah return, dia tidak akan dieksekusi
    print(a*b)
print(hitung(10,20))

def tampil():
    return#jika tidak ada value maka dia akan
print(tampil())#dia akan menampilkan none 

#selasa 14 oktober 2025
#input dan output dalam python
#print adalah syntak untuk output ke konsol
#print(....,sep"|"")
#print("{}berumur{}".format(nama,umur))

#sungsi input
#digunakan untuk menerima input dari user
#nama = input("masukkan nama anda : ")
#input str
#teks = input('masukkan teks :')
#input int
#db = int(input('masukkan nilai integer = '))
#haisl = db*10
#print(haisl)
#input float
#s = float(input('masukkan bilangan desimal = '))
#input boolean
#b = bool(input('apakahan anda mahasiswa(ya/tidak)?')).lower()
#if b == "ya":
 #   print(True)
#else:
  #  print(False)

#input dalam satu baris dipisahkan menggunakan spasi
"""data = input('masukkan nama dan umur').split()
#data = [nama,umur]->data = ['bambang',23]
nama = data[0]
umur = int(data[1])
print(nama,umur)"""

#file input/output
#tentukan daftar srring yang akan ditulis
with open("kelas1INFC.txt","w")as file:#"w= write", "file" adalah nama variabel
    #"kelas1INFC"adalah nama file .txt adalah jenis file
    file.write("hello world\n")
    file.write('ini adalah baris ke dua\n')#write tipe datanya harus str
#metode w lain
nama3 = input('nama : ')
nama = open("biodata.txt","w")
#tulis tekx ke file
nama.write(nama3)
#tutup fioe
nama.close()

#ada dua method yang bisa kita gunakan
text = ["ini baris pertama\n","ini baris kedua\n", 'ini baris ketiga\n']
#with = objek file, "contoh" = nama file, 'w'=mode/method (a,w,r)
with open('contoh_writelines.txt','w') as f:
    f.writelines(text)#writelines harus tipe list

#membaca seluruh file
with open('data.txt','r')as x:
    content = x.red()#->menjadi str
    print(content)
#membaca per baris
with open('data.txt',"r")as file:
    for line in file:
        print(line.strip())
print('==program biodata==')
nama = input('masukkan nama lengkap')
tempat_lahir = input('masukkan tempat lahir')
tangal_lahir = input('tanggal lahir (dd-mm-yyyy)')
alamat = input('alamat ')

print('\n==biodata anda==')
print(f"Nama Lengkap:{nama}")
print(f"Tempat, tanggal lahir:{tempat_lahir}{tangal_lahir}")
print(f"Nama Lengkap:{nama}")
print(f"Nama Lengkap:{nama}")

#percabangan if
#2 jenis if, if dasar dan if bersarang adalah if didalam if
nilai = int(input('nilai:'))
if nilai >= 80:
    print('a')
elif nilai >=70:
    print('b')

#nested if
if umur >18:
    print('anda adalah orang dewasa')
elif umur >=21:
    print('anda adalah remaja')
    if umur >=60:
        print('dia senior')
    elif umur >=21:
        print('dia remaja')
    else:
        print('anda adalah dewasa')
else:
    print('anda adalah remaja')

#perulangan
#for
"""digunakan untuk mengeksekusi blok kode secara berulang"""
#contoh
#for variabel in iterable:
    #blok code yang di ulang
buah_buahan=['apel','jerk','mangga']
for buah in buah_buahan:
    print(buah)

kata = 'python'
for huruf in kata:
    print(huruf)

for i in range(5):
    print(f'perulangan ke-{i}')    
for i in range(2,10,2):#strart=2, stop 10, step=2
    print(f'perulangan ke-{i}')

#nested loop
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")  
#kontroal break dan continue
for i in range(10):
    if i ==5:
        break
    print(i)

for i in range(10):
    if i %2==0:#jika genap
        continue #baris berikutnya setelah continu tdk akan di eksekusi sampai kondisinya tidak terpenuhi
    print(i)

for num in angka:
    total += num
print(f'{total}')

tinggi=5
for i in range (1,tinggi+1):
    print('*'*i)
#perulangan while
#adalah struktur kontrol yang mengeksekusi secara barulang selama kondisinya True
angka = 1
while angka <=5:
    print(f'angka:{angka}')
    angka += 1 #increment (+=), decrement(-=)
print('perulangan selesai')



#28 oktober 2025 Debugging and eror handling dalam python
"""
A.syntax eror
kesalahan dalam penulisan syntax python yang membuat program tidak bisa dijalankan sama sekali
ciri-ciri:
    .program berhenti sebelum dieksekusi
    .ditandai dengan garis merah di editor
    .pesan eoro menunjukkan lokasi syntax yang salah

B. run time eror (exceptions)
eorr yang terjadi saat program sedang berjalan, biasanya karena operasi yang tidak valid
ciri-ciri:
    .program berjalan normal samapi di titik tertentu
    .terjadi saat eksekusi operasi yang bermasalah
    .program berhenti sacara tiba-tiba
"""
#contoh
#contoh 1: type eror
x = "5"+2 #tidak bisa menjumlahkan string dan integer

#contoh 2: ValueEror
y = int('hallo') #tidak bisa menggunakan 'hallo' di int

#contoh 3: ZeroDivisionEror
z = 10/0 #pembagian dengan nol

#contoh 4: NameEror
#print(undefined_variabel)#variabel tidak didefinisikan

#contoh 5: IndexEror
list_kosong = []
print(list_kosong[0]) #mengakses indeks yang tidak ada

"""
c.Logical Eror
program berjalan tnpa eror tetapi menghasilakn=an output yang salah karena kesalahan logika
ciri-ciri:
    .program berjalan normal tanpa muncul pesan eror
    .output tidak sesuai dengan yang diharapkan
    .sulit dideteksi kerena tidak ada indeks eror

#contoh 1: rumuss luas lingkarang yang salah
r = 5
luas = 2*3.14*r #rumus seharusnya 3.14*r**
print(f"luas lingkaran : {luas}")

#contoh 2: logika percabangan terbalik
umur = 17
if umur > 18:
    print('anda anak-anak')
else:
    print('anda dewasa') #output:"anda anak-anak" (seharusnya terbalik)
contoh3: penghitungan rata-rata yang salah
nilai = [80,90,70]
rata_rata = sum(nilai) #seharusnya sum(nilai)/len(nilai)
print(f"Rata-rata : {rata_rata}) #output : 240, seharusnya : 80

EROR HANDLING DENGAN TRY-ES=XCEPT
Struktur dasar:
try:
    #kode yang menyebabkan eror
    kode_bermasalah()
except:
    #ditampilkan jika terjadi eror
    print('terjadi eror!')


"""


#3 November 2025
"""tipe data tuple dan set
tuple --> koleksi data yang immutable, artinya bahwa strukturnya tidak dapa dirubah dan ordered (terurut)atau dari kecil ke besar
karakteristik-->
1. Imumutable : tidak bisa diubah setelah di buat 
2. Ordered : urutan elemen tetap 
3. bisa berisi tie dapa lain 
4. boleh di duplikat 
"""
tuple_kosong = ()
tuple_angka = (1,2,2,3,4,5)
tuple_string = ("apel", "jeruk", "mangga")
tuple_campuran = (1,"hello",3.14,True)
#tuple dengan satu elemen {harus ada koma}
tuple_satu_elemen = (5,)
#contoh operasi tuple
buah = ("apel", "jeruk", "mangga","pisang")
#akses elemen
print(buah[0])
print(buah[-1])

#slicing
print(buah[1:3])
#panjang tuple
print(len(buah))
#count dan index
angka = (1,2,2,23,4,5)
print(angka.count(2))
print(angka.index())

def hitung_luas_keliling (panjang,lebar):
    luas = panjang*lebar
    keliling = 2*(panjang+lebar)
    return luas,keliling #kembali sebegai tuple
hasil = hitung_luas_keliling(5,3)
print(hasil)

"""
set ---> koleksi yang unik dan tidak terurut. set bersifat mutable, kebalikan dari tuple
karakteristik:
1. unik : tidak ada elemen duplikat
2. unordered : tidak menjamin urutan
3. mutable
4. tidak bisa berisi mutable objects seperti list
"""
#cara buat set
set_kosong = set()
set_angka = {1,2,3,4,5}
set_string = {"apel", "jerul", "mangga"}
#dari list (menghapus duplikat)
list_angka = [1,2,2,2,3,4,5]
set_dari_list = set(list_angka)
#contoh
himpunan_a = {1,2,3,4,5}
himpunan_b = {4,5,6,7,8}
#menambah elemen
himpunan_a.add(6) #{1,2,3,4,5,6} #hanya bisa nemambahkan 1 argumen dan bertipe int
himpunan_a.update([7,8]) #{1,2,3,4,5,6,7,8} #bisa lebih dari 1 int, dan dijasikan list
#menghapus elemen
himpunan_a.remove(8) #hapus 8
himpunan_a.discard(10) # hapus 10
himpunan_a.pop() #hapus elemen acak
#operasi himpunan
print(himpunan_a.union(himpunan_b)) #menggabungkan
print(himpunan_a.intersection(himpunan_b)) #Irisan : {4,5}
print(himpunan_a)

# Selasa, 4 November 2025
"""
Tipe Data Dictionary : key-value pairs
Dictionary --> adalah struktur data yang menyimpan data dalam pasangan key-value
Karkter:
1. Key-value pairs :"""
#syntax dasar
dic_kosong = {}
mahasiswa = {
    "nama":"andi",
    "umur":"20",
    "jurusan":"informatika",
    "ipk":3.78

}
#dengan constructor
buah = dict(apel=5000,jeruk=7000,mangga=1000)
#akses
print(mahasiswa["nama"]) #andi
print(mahasiswa.get["umur"])
print(mahasiswa.get["jurusan"])

#Tambahan/ubah nilai
mahasiswa["alamat"]="jakarta"
mahasiswa["umur"]=22

#hapus nilai
del mahasiswa["ipk"]

#panjang dict
print(len(mahasiswa))


#oop, file handling, recurshift, mini projek

#20/November/2025
"""
Rekursif
adalah teknik dimana sebuah fungsi itu memanggil dirinya sendiri
komponen penting rekursi : 
1. base case-kondisi berhenti
2. Recursive case - memanggil fungsi itu sendiri
3. progres menuju base case- setiap panggilan harus mendekari base case"""
"""n! = n x (n-1) x (n-2)x...x1
5! = 5x4x3x2x1=120
0! = 1 (menurut definisi)"""
def faktorial (n):
    #base case
    if n == 0 or n==1:
        return 1
    else : 
        return n* faktorial(n-1)
#testinh
print(f"5! = {faktorial(5)}")#output 120
print(f"0! = {faktorial(0)}")#output 1
print(f"3! = {faktorial(3)}")#output 6

def jumalah_deret(n):
    if n == 1:
        return 1
    else:
        return n + jumalah_deret(n-1)
print(f"\n Jumlah deret 1-5: {jumalah_deret(5)}")










































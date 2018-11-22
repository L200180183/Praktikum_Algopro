#praktikum 8 kegiatan 1
#NOMOR 1
x={'NIM':'L200180183','Nama':'Fakhar Swastika Al-Baihaqi','Alamat':'San Diego, California','Kelas':'D','Universitas':'Universitas Muhammadiyah Surakarta','Fakultas':'Fakultas Komunikasi dan Informatika','Prodi':'Informatika'}
print("Nama : "+ x['Nama'])
print("NIM : "+ x['NIM'])
print("Alamat : "+ x['Alamat'])
print("Universitas : "+ x['Universitas'])
print("Fakultas : "+ x['Fakultas'])
print("Program Studi : "+ x['Prodi'])
print("Kelas : "+ x['Kelas'])

#NOMOR 2
b="""Pilihan yang tersedia:
b menampilkan bantuan ini
n menampilkan Nama
N menampilkan NIM
A menampilkan Alamat
U menampilkan Universitas
F menampilkan Fakultas
P menampilkan Program Studi
K menampilkan Kelas
k keluar\n"""
def nim():
    print ("NIM: "+x['NIM'])
def nama():
    print ("Nama: "+x['Nama'])
def alamat():
    print ("Alamat: "+x['Alamat'])
def universitas():
    print ("Universitas: "+x['Universitas'])
def fakultas():
    print ("Fakultas: "+x['Fakultas'])
def prodi():
    print ("Program Studi: "+x['Prodi'])
def kelas():
    print ("Kelas: "+x['Kelas'])
key = ('b', 'n', 'N', 'A', 'U', 'F', 'P', 'K', 'k')
print(b)
data = input("Pilihan saudara: ")
while data != 'k':
    if data == 'b':
        print(b)
        data = input("Pilihan saudara: ")
    elif data == 'n':
        nama()
        data = input("Pilihan saudara: ")
    elif data == 'N':
        nim()
        data = input("Pilihan saudara: ")
    elif data == 'A':
        alamat()
        data = input("Pilihan saudara: ")
    elif data == 'U':
        universitas()
        data = input("Pilihan saudara: ")
    elif data == 'F':
        fakultas()
        data = input("Pilihan saudara: ")
    elif data == 'P':
        prodi()
        data = input("Pilihan saudara: ")
    elif data == 'K':
        kelas()
        data = input("Pilihan saudara: ")
    elif data != key:
        print ("perintah tidak dikenal")
        data = input("Pilihan saudara: ")
else:
        print ("Terima Kasih")
    
        

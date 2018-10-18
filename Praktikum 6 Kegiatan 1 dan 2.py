## Fakhar Swastika Al-Baihaqi(L200180183)

#kegiatan 1
Nama = 'Fakhar Swastika Al-Baihaqi'
Alamat = 'Wirorejan RT04/RW08 Ngadirejo, Kartasura, Sukoharjo'
NIM = 'L200180183'
Kelas = 'D'
TTL = 'Sukoharjo, 13 Maret 2000'
Kelamin = 'Laki-Laki'
Agama = 'Islam'
Fakultas = 'FKI'
Jurusan = 'Informatika'
Cita_cita = 'Programmer'

#kegiatan 2
import random
namaSingkat = Nama[:6] + ' ' + Nama[7] + '. ' + Nama[16] + '. ' + Nama[19]
username = Nama[0] + TTL[11:13] + TTL[20:]
password = Nama[:3] + str(random.randint(0, 1000))

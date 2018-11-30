#kegiatan 3
import shelve
a = open('L200180183', 'r')
NIM = a.readline()
TL = a.readline()
Nama = a.readline()
a.close()

a = shelve.open('Fakhar')
a['b'] = (NIM, TL, Nama)
a.close

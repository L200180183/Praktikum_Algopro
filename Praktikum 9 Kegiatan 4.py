#kegiatan 4
import shelve
a = shelve.open('Fakhar')
print 'NIM            : ',a['b'][0]
print 'Tanggal Lahir  : ',a['b'][1]
print 'Nama           : ',a['b'][2]
a.close()

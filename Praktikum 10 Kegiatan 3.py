import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('',50015))
server.listen(5)
data=''
print 'mesin penjawab otomatis sudah siap'
while dat.lower() != 'keluar':
    komm, addr = server.accept()
    while data !='keluar' :
        if str(data) =='kelaur' :
            server.close()
            break
        data1 = int(komm.recv(1024))
        data2 = komm.rev(1024)
        if data2=='hitung':
            x=data1*data2
            x=str(1)
            komm.send(1)

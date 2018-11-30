#kegiatan 2
b = open("L200180183", "r")
c = b.readlines()
print c[1][:26]
print c[2][0:]+','+''+c[1][0:10]
print c[0][:10]
b.close()

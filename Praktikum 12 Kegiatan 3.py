#!/usr/bin/python

def hitung_luas(jarijari):
    "fungsi menghitung luas dari Bola"
    r = jarijari
    phi = 3.14
    hasil = 4*phi*r*r
    return hasil

a = open('bola.jpg', 'rb').read().encode('base64').replace('\n', '')

print "<!DOCTYPE html>"
print
print """<html>
<head><title>Selamat Datang</title></head>
<body>
<table>
    <tr>
	<td rowspan='6'><img src="data:image/jpg;base64,{0}"></td>""".format(a)
print"""
	<td colspan='3'><b><font size='5'>Bangun Geometri</font><b></td>
    </tr>
    <tr>
	<td>Nama bangun
	<td>:</td>
	<td> bola</td>
    </tr>
    <tr>
	<td>Dimensi (2D/3D) </td>
	<td>:</td>
	<td> 3D</td>
    </tr>
    <tr>
	<td>Rumus luas </td>
	<td>:</td>
	<td> 4 x phi x r x r</td>
    </tr>"""
jarijari = 5
print"""
    <tr>
	<td>Jari-Jari </td>
	<td>:</td>
	<td> {0}</td>
    </tr>""".format(jarijari)
luas = hitung_luas(jarijari)
print"""
    <tr>
        <td>Luas </td>
        <td>:</td>
        <td> {0}</td>
    </tr>""".format(luas)
print"""
</table>
</body>
</html>"""

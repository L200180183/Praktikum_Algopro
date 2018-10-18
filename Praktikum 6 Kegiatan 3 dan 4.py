Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: C:\Users\Acer\Downloads\prak 6.1.py ================
>>> Nama = 'Fakhar Swastika Al-Baihaqi'
>>> NIM = 'L200180183'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> a / b
45.5
>>> a // b
45
>>> 10 * (a - 999)
1840
>>> b ** 2
676
>>> a % b
13
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> a / c
94.64
>>> a // c
94.0
>>> a % c
8.0
>>> c > b
False
>>> type(c > b)
<class 'bool'>
>>> a > b and b > c
True
>>> a > 1100 or b < 10
True
>>> ##Kegiatan 4##
>>> Nama = 'Fakhar Swastika Al-Baihaqi'
>>> NIM = 183
>>> Tinggi = 1.65
>>> Berat = 50
>>> TahunLahir = 2000
>>> Aku = (TahunLahir,Berat,Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> Aku[0]
2000
>>> a = NIM % 4; Aku[a]
183
>>> type(Aku[a])
<class 'int'>
>>> Aku[a:4]
(183,)
>>> type(Aku[4])
<class 'str'>
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> type(Data)
<class 'list'>
>>> type(Data[4])
<class 'str'>
>>> Data[4][5]
'r'
>>> Data[4][a:6]
'har'
>>> Data[0] = 'ok'; Data
['ok', 50, 1.65, 183, 'Fakhar Swastika Al-Baihaqi']
>>> Data[-a]
1.65
>>> range(a)
range(0, 3)
>>> 

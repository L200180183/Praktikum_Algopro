from Tkinter import*

my_app = Tk(className='kalkulator sederhana')

L1 = Label(my_app, text='Bangun Geometri', font=('Arial', 24))
L1.grid(row=0, column=0, columnspan=3, sticky=W)
L2 = Label(my_app, text='Deskripsi tentang bangun bola, antara lain nama, dimensi, contoh benda, dan lain-lain.')
L2.grid(row=1, column=0, columnspan=3, sticky=W)
L3 = Label(my_app, text='Jari-jari : ')
L3.grid(row=3, column=0, sticky=W)
E1 = Entry(my_app)
E1.grid(row=3, column=1, sticky=W)
L4 = Label(my_app, text='Luas = ')
L4.grid(row=4, column=1, sticky=W)
luas = StringVar()
L5 = Label(my_app, textvariable=luas)
L5.grid(row=4, column=2, sticky=W)

def hitung():
    phi=3.14
    luas.set(4 * phi * int(E1.get())**2)

B1 = Button(my_app, text='Hitung luas', command=hitung)
B1.grid(row=4,column=0, sticky=W)

my_app.mainloop()

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *


window = tk.Tk()
window.configure(background="#0b032d", height=600, width=800)
label1 = ttk.Label(window)
label1.configure(
    background="#0b032d",
    cursor="arrow",
    font="{Montserrat Black} 14 {}",
    foreground="#ffffff",
    text='Webinar Registration')
label1.place(anchor="nw", relx=0.0, rely=0.0, x=150, y=30)
label3 = ttk.Label(window)
label3.configure(
    background="#0b032d",
    cursor="arrow",
    font="{Montserrat Medium} 10 {}",
    foreground="#ffffff",
    text='Nama: *')
label3.place(anchor="nw", relx=0.0, rely=0.0, x=150, y=70)
entry1 = ttk.Entry(window)
_text_ = 'First name'
entry1.delete("0", "end")
entry1.insert("0", _text_)
entry1.place(
    anchor="nw",
    height=30,
    relwidth=0.0,
    relx=0.0,
    rely=0.0,
    width=200,
    x=150,
    y=100)
entry2 = ttk.Entry(window)
_text_ = 'Last name'
entry2.delete("0", "end")
entry2.insert("0", _text_)
entry2.place(
    anchor="nw",
    height=30,
    relwidth=0.0,
    relx=0.0,
    rely=0.0,
    width=200,
    x=380,
    y=100)
label4 = ttk.Label(window)
label4.configure(
    background="#0b032d",
    cursor="arrow",
    font="{Montserrat Medium} 10 {}",
    foreground="#ffffff",
    text='Email: *')
label4.place(anchor="nw", relx=0.0, rely=0.0, x=150, y=140)
entry3 = ttk.Entry(window)
_text_ = '@gmail.com'
entry3.delete("0", "end")
entry3.insert("0", _text_)
entry3.place(
    anchor="nw",
    height=30,
    relwidth=0.0,
    relx=0.0,
    rely=0.0,
    width=430,
    x=150,
    y=170)
label5 = ttk.Label(window)
label5.configure(
    background="#0b032d",
    cursor="arrow",
    font="{Montserrat Medium} 10 {}",
    foreground="#ffffff",
    text='Jenis Kelamin: *')
label5.place(anchor="nw", relx=0.0, rely=0.0, x=150, y=210)
radiobutton1 = tk.Radiobutton(window)
radiobutton1.configure(text='Wanita', value="wanita", bg='#0b032d',fg='#ffffff')
radiobutton1.place(anchor="nw", width=100, x=150, y=240)
radiobutton2 = tk.Radiobutton(window)
radiobutton2.configure(text='Pria', value="pria", bg='#0b032d',fg='#ffffff')
radiobutton2.place(anchor="nw", width=100, x=290, y=240)
label6 = ttk.Label(window)
label6.configure(
    background="#0b032d",
    cursor="arrow",
    font="{Montserrat Medium} 10 {}",
    foreground="#ffffff",
    text='Universitas: *')
label6.place(anchor="nw", relx=0.0, rely=0.0, x=150, y=270)
combobox2 = ttk.Combobox(window)
combobox2.configure(
    values='Universitas-Sulawesi-Barat Universitas-Terbuka Universitas-Hasanuddin Universitas-Negeri-Makassar')
combobox2.place(anchor="nw", height=30, width=430, x=150, y=300)
label7 = ttk.Label(window)
label7.configure(
    background="#0b032d",
    cursor="arrow",
    font="{Montserrat Medium} 10 {}",
    foreground="#ffffff",
    text='Tanggal Lahir: *')
label7.place(anchor="nw", relx=0.0, rely=0.0, x=150, y=340)
spinbox1 = ttk.Spinbox(window)
spinbox1.configure(
    values="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31")
spinbox1.place(anchor="nw", width=130, x=150, y=370)
spinbox2 = ttk.Spinbox(window)
spinbox2.configure(values="1 2 3 4 5 6 7 8 9 10 11 12  ")
spinbox2.place(anchor="nw", width=130, x=300, y=370)
spinbox3 = ttk.Spinbox(window)
spinbox3.configure(
    values="2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010")
spinbox3.place(anchor="nw", width=130, x=450, y=370)
label8 = ttk.Label(window)
label8.configure(
    background="#0b032d",
    cursor="arrow",
    font="{Montserrat Medium} 10 {}",
    foreground="#ffffff",
    text='Alamat: *')
label8.place(anchor="nw", relx=0.0, rely=0.0, x=150, y=400)
entry4 = ttk.Entry(window)
entry4.place(anchor="nw", height=50, width=430, x=150, y=430)
checkbutton1 = tk.Checkbutton(window)
checkbutton1.configure(
    offvalue="no",
    onvalue="yes",
    text='Privacy & Condition*',
    bg='#0b032d',
    fg='#ffffff')
checkbutton1.place(anchor="nw", x=150, y=490)
button1 = tk.Button(window)
button1.configure(text='Save', bg='#596475', fg='#ffffff', font="{Montserrat Medium} 10 {}")
button1.place(anchor="nw", height=30, width=215, x=265, y=530)

window.mainloop()

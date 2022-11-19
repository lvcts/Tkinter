import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

toplevel1 = tk.Tk()
toplevel1.configure(
    background="#DAF7DC",
    cursor="arrow",
    height=500,
    width=700)
toplevel1.title('Beasiswa')
label1 = ttk.Label(toplevel1)
label1.configure(
    background="#DAF7DC",
    font="{Montserrat} 12 {bold}",
    justify="center",
    text='FORM PENDAFTARAN BEASISWA S2')
label1.place(anchor="center", relx=0.0, rely=0.0, x=350, y=30)
canvas1 = tk.Canvas(toplevel1)
canvas1.configure(background="#ABC8C0")
canvas1.place(height=40, relx=0.0, rely=0.0, width=700, y=50)
label2 = ttk.Label(toplevel1)
label2.configure(
    background="#ABC8C0",
    font="{Montserrat} 12 {}",
    text='Nama Beasiswa *')
label2.place(x=20, y=57)
beasiswa = tk.StringVar(value='Beasiswa')
__values = ['LPDP', 'Bidikmisi', 'KIP-K']
jenis_beasiswa = tk.OptionMenu(
    toplevel1, beasiswa, *__values, command=None)
jenis_beasiswa.place(x=190, y=55)
canvas2 = tk.Canvas(toplevel1)
canvas2.configure(background="#9EE493")
canvas2.place(anchor="nw", height=400, width=700, y=100)
label4 = ttk.Label(toplevel1)
label4.configure(
    background="#9EE493",
    font="{Montserrat Medium} 11 {}",
    text='Data Calon Peserta Beasiswa S2*')
label4.place(x=20, y=120)
label5 = ttk.Label(toplevel1)
label5.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Nama Lengkap*')
label5.place(x=20, y=150)
nama = ttk.Entry(toplevel1)
nama.place(height=20, width=190, x=150, y=150)
separator1 = ttk.Separator(toplevel1)
separator1.configure(orient="vertical")
separator1.place(
    anchor="nw",
    height=400,
    relx=0.0,
    rely=0.0,
    width=5,
    x=350,
    y=102)
label6 = ttk.Label(toplevel1)
label6.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Jenis Kelamin*')
label6.place(x=20, y=175)
jk_pr = ttk.Radiobutton(toplevel1)
jk_pr.configure(text='Wanita', value="wanita")
jk_pr.place(anchor="nw", x=150, y=175)
jk_lk = ttk.Radiobutton(toplevel1)
jk_lk.configure(text='Pria', value="pria")
jk_lk.place(anchor="nw", x=230, y=175)
label7 = ttk.Label(toplevel1)
label7.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Tempat Lahir*')
label7.place(x=20, y=200)
combobox1 = ttk.Combobox(toplevel1)
combobox1.configure(
    values='Pare-Pare Makassar Majene Pinrang Mamuju Pasangkayu')
combobox1.place(anchor="nw", height=20, width=190, x=150, y=200)
label9 = ttk.Label(toplevel1)
label9.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Tanggal Lahir*')
label9.place(x=20, y=230)
tgl_lahir = tk.StringVar(value='Tgl')
__values = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21',
    '22',
    '23',
    '24',
    '25',
    '26',
    '27',
    '28',
    '29',
    '30',
    '31']
optionmenu6 = tk.OptionMenu(
    toplevel1, tgl_lahir, *__values, command=None)
optionmenu6.place(anchor="nw", height=25, x=150, y=225)
bln_lahir = tk.StringVar(value='Bln')
__values = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12']
optionmenu7 = tk.OptionMenu(
    toplevel1, bln_lahir, *__values, command=None)
optionmenu7.place(anchor="nw", height=25, x=215, y=225)
thn_lahir = tk.StringVar(value='Thn')
__values = [
    '2000',
    '2001',
    '2002',
    '2003',
    '2004',
    '2005',
    '2006',
    '2007',
    '2008',
    '2009',
    '2010']
optionmenu8 = tk.OptionMenu(
    toplevel1, thn_lahir, *__values, command=None)
optionmenu8.place(anchor="nw", height=25, x=280, y=225)
label11 = ttk.Label(toplevel1)
label11.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Nomor Identitas*')
label11.place(x=20, y=255)
entry3 = ttk.Entry(toplevel1)
entry3.place(height=20, width=190, x=150, y=255)
label12 = ttk.Label(toplevel1)
label12.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Alamat*')
label12.place(x=20, y=295)
text1 = tk.Text(toplevel1)
text1.configure(height=10, width=50)
text1.place(anchor="nw", height=50, width=190, x=150, y=280)
label13 = ttk.Label(toplevel1)
label13.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Kode POS*')
label13.place(x=20, y=350)
entry4 = ttk.Entry(toplevel1)
entry4.place(height=20, width=190, x=150, y=350)
label14 = ttk.Label(toplevel1)
label14.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Kabupaten/Kota*')
label14.place(x=20, y=375)
entry5 = ttk.Entry(toplevel1)
entry5.place(height=20, width=190, x=150, y=375)
label15 = ttk.Label(toplevel1)
label15.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Provinsi*')
label15.place(x=20, y=400)
entry6 = ttk.Entry(toplevel1)
entry6.place(height=20, width=190, x=150, y=400)
label16 = ttk.Label(toplevel1)
label16.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Status*')
label16.place(x=20, y=425)
entry7 = ttk.Entry(toplevel1)
entry7.place(height=20, width=190, x=150, y=425)


def message():
    tk.messagebox.showwarning(
        title='PERHATIAN', message='Apakah data sudah sesuai?', icon='warning')


button2 = tk.Button(toplevel1)
button2.configure(text='Next', command=message, bg='#70566D', fg='white')
button2.place(
    anchor="nw",
    height=25,
    relheight=0.0,
    width=125,
    x=120,
    y=460)

mainwindow = toplevel1
toplevel1.mainloop()

toplevel1 = tk.Tk()
toplevel1.configure(
    background="#DAF7DC",
    cursor="arrow",
    height=500,
    width=700)
toplevel1.title('Beasiswa')
label1 = ttk.Label(toplevel1)
label1.configure(
    background="#DAF7DC",
    font="{Montserrat} 12 {bold}",
    justify="center",
    text='FORM PENDAFTARAN BEASISWA S2')
label1.place(anchor="center", relx=0.0, rely=0.0, x=350, y=30)
canvas1 = tk.Canvas(toplevel1)
canvas1.configure(background="#ABC8C0")
canvas1.place(height=40, relx=0.0, rely=0.0, width=700, y=50)
label2 = ttk.Label(toplevel1)
label2.configure(
    background="#ABC8C0",
    font="{Montserrat} 12 {}",
    text='Nama Beasiswa *')
label2.place(x=20, y=57)
beasiswa = tk.StringVar(value='Beasiswa')
__values = ['LPDP', 'Bidikmisi', 'KIP-K']
jenis_beasiswa = tk.OptionMenu(
    toplevel1, beasiswa, *__values, command=None)
jenis_beasiswa.place(x=190, y=55)
canvas2 = tk.Canvas(toplevel1)
canvas2.configure(background="#9EE493")
canvas2.place(anchor="nw", height=400, width=700, y=100)
label4 = ttk.Label(toplevel1)
label4.configure(
    background="#9EE493",
    font="{Montserrat Medium} 11 {}",
    text='Data Calon Peserta Beasiswa S2*')
label4.place(x=20, y=120)
label5 = ttk.Label(toplevel1)
label5.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Nama Lengkap*')
label5.place(x=20, y=150)
nama = ttk.Entry(toplevel1)
nama.place(height=20, width=190, x=150, y=150)
separator1 = ttk.Separator(toplevel1)
separator1.configure(orient="vertical")
separator1.place(
    anchor="nw",
    height=400,
    relx=0.0,
    rely=0.0,
    width=5,
    x=350,
    y=102)
label6 = ttk.Label(toplevel1)
label6.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Jenis Kelamin*')
label6.place(x=20, y=175)
jk_pr = ttk.Radiobutton(toplevel1)
jk_pr.configure(text='Wanita', value="wanita")
jk_pr.place(anchor="nw", x=150, y=175)
jk_lk = ttk.Radiobutton(toplevel1)
jk_lk.configure(text='Pria', value="pria")
jk_lk.place(anchor="nw", x=230, y=175)
label7 = ttk.Label(toplevel1)
label7.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Tempat Lahir*')
label7.place(x=20, y=200)
combobox1 = ttk.Combobox(toplevel1)
combobox1.configure(
    values='Pare-Pare Makassar Majene Pinrang Mamuju Pasangkayu')
combobox1.place(anchor="nw", height=20, width=190, x=150, y=200)
label9 = ttk.Label(toplevel1)
label9.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Tanggal Lahir*')
label9.place(x=20, y=230)
tgl_lahir = tk.StringVar(value='Tgl')
__values = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21',
    '22',
    '23',
    '24',
    '25',
    '26',
    '27',
    '28',
    '29',
    '30',
    '31']
optionmenu6 = tk.OptionMenu(
    toplevel1, tgl_lahir, *__values, command=None)
optionmenu6.place(anchor="nw", height=25, x=150, y=225)
bln_lahir = tk.StringVar(value='Bln')
__values = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    '11',
    '12']
optionmenu7 = tk.OptionMenu(
    toplevel1, bln_lahir, *__values, command=None)
optionmenu7.place(anchor="nw", height=25, x=215, y=225)
thn_lahir = tk.StringVar(value='Thn')
__values = [
    '2000',
    '2001',
    '2002',
    '2003',
    '2004',
    '2005',
    '2006',
    '2007',
    '2008',
    '2009',
    '2010']
optionmenu8 = tk.OptionMenu(
    toplevel1, thn_lahir, *__values, command=None)
optionmenu8.place(anchor="nw", height=25, x=280, y=225)
label11 = ttk.Label(toplevel1)
label11.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Nomor Identitas*')
label11.place(x=20, y=255)
entry3 = ttk.Entry(toplevel1)
entry3.place(height=20, width=190, x=150, y=255)
label12 = ttk.Label(toplevel1)
label12.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Alamat*')
label12.place(x=20, y=295)
text1 = tk.Text(toplevel1)
text1.configure(height=10, width=50)
text1.place(anchor="nw", height=50, width=190, x=150, y=280)
label13 = ttk.Label(toplevel1)
label13.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Kode POS*')
label13.place(x=20, y=350)
entry4 = ttk.Entry(toplevel1)
entry4.place(height=20, width=190, x=150, y=350)
label14 = ttk.Label(toplevel1)
label14.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Kabupaten/Kota*')
label14.place(x=20, y=375)
entry5 = ttk.Entry(toplevel1)
entry5.place(height=20, width=190, x=150, y=375)
label15 = ttk.Label(toplevel1)
label15.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Provinsi*')
label15.place(x=20, y=400)
entry6 = ttk.Entry(toplevel1)
entry6.place(height=20, width=190, x=150, y=400)
label16 = ttk.Label(toplevel1)
label16.configure(
    background="#9EE493",
    font="{Montserrat} 10 {}",
    text='Status*')
label16.place(x=20, y=425)
entry7 = ttk.Entry(toplevel1)
entry7.place(height=20, width=190, x=150, y=425)

def message():
    tk.messagebox.showwarning(
        title='PERHATIAN', message='Apakah data sudah sesuai?', icon='warning')

button2 = tk.Button(toplevel1)
button2.configure(text='Next', command=message, bg='#70566D', fg='white')
button2.place(
    anchor="nw",
    height=25,
    relheight=0.0,
    width=125,
    x=120,
    y=460)

mainwindow = toplevel1
toplevel1.mainloop()

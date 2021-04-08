from tkinter import *
import sqlite3


root = Tk()
root.title("Halaman Reservasi")
root.geometry("600x410")

#Databases


#Create a database or connect to one
conn = sqlite3.connect('data.db')
#Create cursor
c = conn.cursor()

#create table
# c.execute(""" CREATE TABLE couple(
#   		nama_cowo text,
#   		nama_cewe text,
#   		no_telepon integer
#   		#view text,
#  		#Extra text,
#  		#Paket text
#   		)""")

#Create submit function
def submit():
	#Create a database or connect to one
	conn = sqlite3.connect('data.db')
	#Create cursor
	c = conn.cursor()

	#Insert Into Table
	c.execute("INSERT INTO couple VALUES (:nama_cowo, :nama_cewe, :no_telepon)",
				{
					'nama_cowo': nama_cowo.get(),
					'nama_cewe': nama_cewe.get(),
					'no_telepon': no_telepon.get()
					# 'view': view(),
					# 'Extra': Extra(),
					# 'Paket': Paket()

				})

	#commit Changes
	conn.commit()
	#close Connection
	conn.close()


	#Clear The Text boxes
	nama_cowo.delete(0, END)
	nama_cewe.delete(0, END)
	no_telepon.delete(0, END)
	# view.delete(0, END)
	# Extra.delete(0, END)
	# Paket.delete(0, END)
	
#Create Show data function
def query():
	top_q = Toplevel()
	top_q.title('Halaman Data')
	top_q.geometry("450x150")

	#Create a database or connect to one
	conn = sqlite3.connect('data.db')
	#Create cursor
	c = conn.cursor()

	#query the database
	c.execute("SELECT * FROM couple")
	records = c.fetchall() 
	print(records)

	#Loop thru Results
	print_records = ''
	for record in records[0]:
		print_records += str(record) + "\n"

	query_label = Label(top_q, text=print_records)
	query_label.grid(row=0, column=0, columnspan=2)

	#commit Changes
	conn.commit()
	#close Connection
	conn.close()

#Create clear data function
def clear():
	top_q = Toplevel()
	top_q.title('Halaman Data')
	top_q.geometry("450x150")

	#Create a database or connect to one
	conn = sqlite3.connect('data.db')
	#Create cursor
	c = conn.cursor()

	#delete a record
	lbl1 = Label(top_q, text="SEMUA DATA TELAH TERHAPUS ").pack()#isi Windows Baru
	c.execute("DELETE from couple WHERE oid=PLACEHOLDER")

	#commit Changes
	conn.commit()
	#close Connection
	conn.close()

#===================================== Label Judul =======================================.
Label_reser = Label(root, text="RESERVASI HERE!")
#Mendorongnya ke layar
Label_reser.grid(row=0, column=1, padx=10, pady=10)


#=================================Create Text Box Label====================================
nama_cowo_label = Label(root, text="Nama Cowo")
nama_cowo_label.grid(row=2, column=0)

nama_cewe_label = Label(root, text="Nama Cewe")
nama_cewe_label.grid(row=3, column=0)

no_telepon_label = Label(root, text="No Telepon")
no_telepon_label.grid(row=4, column=0)

view_label = Label(root, text="View")
view_label.grid(row=5, column=0)

Extra_label = Label(root, text="Extra")
Extra_label.grid(row=6, column=0)

Paket_label = Label(root, text="Paket")
Paket_label.grid(row=8, column=0)


#==================================Create text Boxes=========================================
nama_cowo = Entry(root, width=30)
nama_cowo.grid(row=2, column=1, padx=30)

nama_cewe = Entry(root, width=30)
nama_cewe.grid(row=3, column=1,)

no_telepon= Entry(root, width=30)
no_telepon.grid(row=4, column=1)


#=================================Create Dropdown(view)=============================================
clicked = StringVar()
clicked.set("City view")#untuk tampilan nya

drop = OptionMenu(root, clicked, "City view", "Nature View", "Pool View", "Beach View") #pilihan chckbox
drop.grid(row=5, column=1, ipadx=40, padx=1)


#===============================Create Chackbox (Extra)===============================================
c1 = IntVar()#var nya
c2 = IntVar()#var nya
c3 = IntVar()#var nya
c4 = IntVar()#var nya

c1 = Checkbutton(root, text="Flower", variable=c1)#chackbox nya
c1.grid(row=6, column=1)#munculin 

c2 = Checkbutton(root, text="Coklate", variable=c2)#chackbox nya
c2.grid(row=6, column=2)#munculin 

c3 = Checkbutton(root, text="Candle", variable=c3)#chackbox nya
c3.grid(row=7, column=1)#munculin 

c4 = Checkbutton(root, text="Instrumen", variable=c4, padx=20)#chackbox nya
c4.grid(row=7, column=2)#munculin 


#===============================Create Radio (Paket)=====================================================
r = IntVar()

Radiobutton(root, text="Anniversary", variable=r, value=1).grid(row=8, column=1)#untuk buat pilihnan radio 1
Radiobutton(root, text="Brithday", variable=r, value=2).grid(row=8, column=2)#untuk buat pilihan radio 2
Radiobutton(root, text="Date", variable=r, value=3).grid(row=9, column=1)#untuk buat pilihnan radio 1
Radiobutton(root, text="Dinner", variable=r, value=4).grid(row=9, column=2)#untuk buat pilihan radio 2


#===============================Create Per-Bottunan============================================
#Create Submit  Button *
submit_btn = Button(root, text="Submit", command=submit)
submit_btn.grid(row=10, column=0, columnspan=3, pady=10, padx=10, ipadx=95)

#Create Exit Button *
button_quit = Button(root, text="Exit", command=root.quit)
button_quit.grid(row=11, column=0, columnspan=3, pady=10, padx=10, ipadx=102)

#Create a Query Button / ngeliat seluruh data
query_btn = Button(root, text = "See All Submissons", command=query)
query_btn.grid(row=2, column=10, columnspan=3, pady=10, ipadx=20)

#Create Clear Button
clear_btn = Button(root, text="Clear Submissons", command=clear)
clear_btn.grid(row=3, column=10, columnspan=3, pady=10, ipadx=20)

#Create About Button
def window_about():#fungsi untuk munculin window about
	top_a = Toplevel()
	top_a.title('Halaman About')
	top_a.geometry("950x150")
	lbl1 = Label(top_a, text="JUDUL: Bucin (Budak Cinta) ").grid(row=1, column=0, sticky= "w")#isi Windows Baru
	lbl2 = Label(top_a, text="DESKRIPSI: App Bucin ini merukapan Aplikasi reservasi khusus yang kami buat untuk para couple yang akan mengadakan acara di restoran kami").grid(row=2, column=0, sticky= "w")#isi Windows Baru
	lbl3 = Label(top_a, text="Acara seperti anniversary, birthday, Dinner , dll yang sudah kami sediakan di bagian ‘paket’. ").grid(row=3, column=0, sticky= "w")#isi Windows Baru
	lbl4 = Label(top_a, text="Mereka juga dapat memilih view yang diinginkan, serta dapat memilih tambahan extra fasilitas apa saja yang ada, seperti buket bunga, sampai iringan instrumen biola pribadi.").grid(row=4, column=0,sticky= "w")#isi Windows Baru
	lbl5 = Label(top_a, text="Dengan ada nya App nya ini di harapkan dapat membatu mereka para couple untuk menciptakan pengalaman yang terencana , nyaman dan romantis.  ").grid(row=5, column=0,sticky= "w")#isi Windows Baru
	lbl6 = Label(top_a, text="PEMBUAT: Nenden Citra S.N / 1908589 ").grid(row=6, column=0, sticky= "w")#isi Windows Baru

about_btn = Button(root, text="About", command = window_about)
about_btn.grid(row=4, column=10, columnspan=3, pady=10, ipadx=20)



#commit Changes
conn.commit()
#close Connection
conn.close()

root.mainloop()
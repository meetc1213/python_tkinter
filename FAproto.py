#Importing modules
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as font
import mysql.connector
#Creating connection with the database
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="jorapura*",
	auth_plugin='mysql_native_password',
	database='new'
	)
cursor=mydb.cursor()
sqlenter="INSERT INTO data(Name,Contact,Email,I1 ,IQ1 ,I2 ,IQ2 ,I3 ,IQ3 ,I4 ,IQ4 ,I5 ,IQ5 ,I6 ,IQ6)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
i=0
fc=[]
sq="INSERT INTO food(Name,Availability,Price,Units) VALUES(%s,%s,%s,%s)"

p=[]
sql="SELECT * FROM data"
cursor.execute(sql)
mybill=cursor.fetchall()
for bill in mybill:
	p.append(bill[0])
#Defining functions
def clrdata():
	q=[tab2select,tab4select,tab10select]
	Name.delete('0',END)
	PN.delete('0',END)
	Email.delete('0',END)
	apadd.set("0")
	npedit.set("0")
	add_name.delete('0',END)
	#spinboxes
	for j in range(5):
		fdvar[j].set("0")
	#comboboxes
	for k in range(3):
		q[k].current(0)
def Back():
	tabsql="SELECT Tnum FROM tables WHERE Availability='v'"
	cursor.execute(tabsql)
	G=cursor.fetchall()
	S=['None']
	for t in G:
		S.append(t[0])
	admsc.withdraw()
	cussc.withdraw()
	Cbillsc.withdraw()
	top.update()
	top.deiconify()
	#resetting the value of spinboxes,entry boxes and checkbuttons
	clrdata()
def confirm():
	N=Name.get()
	E=Email.get()
	P=PN.get()
	y=190
	m=0
	

	if Name.get() and PN.get() and Email.get() :
		q=messagebox.askquestion("Confirmation","Do you want to confirm the transaction?")
		if q=="yes":
			q=[tab2select.get(),tab4select.get(),tab10select.get()]
			#
			



			for h in range(3):
				if q[h]!="None":
					Label(Cbillsc,text=q[h],bg="light yellow",font=(None,15)).place(x=900,y=190+m)
					c="UPDATE tables SET Availability='o' WHERE Tnum in ('"+q[i]+"')"
					cursor.execute(c)
					mydb.commit()
				m=m+50
			for j in range(6):
					Label(Cbillsc,text=foodict[fsf[j]].get(),bg="light yellow",fg="black",font=(None,15)).place(x=600,y=y)
					y=y+60					


			#POPULATING THE DATA TABLE
			crec=(Name.get(),PN.get(),Email.get(),items_entry["IE0"].get(),foodict["P"].get(),items_entry["IE1"].get(),foodict["B"].get(),items_entry["IE2"].get(),foodict["N"].get() ,items_entry["IE3"].get(),foodict["C"].get() ,items_entry["IE4"].get(),foodict["T"].get() ,items_entry["IE5"].get(),foodict["J"].get())
			cursor.execute(sqlenter,crec)
			mydb.commit()
			bill_rec()
			Total=0
			sql="SELECT * FROM data ORDER BY ID DESC LIMIT 1"
			cursor.execute(sql)
			mybill=cursor.fetchall()
			for bill in mybill:
				p.append(bill[0])

			ok=messagebox.showinfo("Success","Transaction done")
			Bill()
			
	else:
		messagebox.showwarning("Error","Complete the data")
def Customer():
	top.withdraw()
	Cbillsc.withdraw()
	cussc.update()
	cussc.deiconify()
def Bill():
	cussc.withdraw()
	Cbillsc.update()
	Cbillsc.deiconify()

#ADMIN WINS
def Administrator():
	top.withdraw()
	admsc.update()
	admsc.deiconify()
	


def quit():
	top.destroy()
#Lists,dictionaries, vars for the progrm

fd=["Pizza",12,"Burger",10,"Noodles",11,"Coffee",5,"Tea",3,"Juice",10]
foody=[]
qwerty="SELECT * FROM food WHERE Availability='a'"
cursor.execute(qwerty)
foods=cursor.fetchall()
print(foods[0][1])
for food in foods:
	foody.append(food[1])
	foody.append(food[3])
#QUERIES  to retrieve data from the database and store in certain lists
menu=[]
query="SELECT * FROM food WHERE Availability='a'"
cursor.execute(query)
foodtab=cursor.fetchall()
for food in foodtab:
	menu.append(food[1])
allfd=[]
FEstat=[]
QQ="SELECT * FROM food"
cursor.execute(QQ)
allfoods=cursor.fetchall()
for food in allfoods:
	allfd.append(food[1])
	FEstat.append(food[1])
	FEstat.append(food[3])



items_entry={}
fsf=["P","B","N","C","T","J"]
fdvar=["Pv","Bv","Nv","Cv","Tv","Jv"]
Combo_var=["C0","C1","C2","C3","C4","C5"]
foodict={}
info=["Full Name: ","Phone No: ","Email: "]
table=['Table 1: ','Table 2: ','Table 3: ']

cbdit={}
cbl=["a","b","c","d","e","f","g"]
#Window creation
top = Tk()
cussc=Tk()
admsc=Tk()
Cbillsc=Tk()
#Window closing
cussc.withdraw()
admsc.withdraw()
Cbillsc.withdraw()
#Window background
cussc['bg']='light blue'
admsc['bg']='light pink'
top['bg']='blue'
Cbillsc['bg']='light yellow'

#Creating fullscreen windows
top.attributes('-fullscreen', True)
cussc.attributes('-fullscreen', True)
admsc.attributes('-fullscreen', True)
Cbillsc.attributes('-fullscreen', True)


#Window titles
top.title("Meet's Curry")
cussc.title("Customer screen")
admsc.title("Administrator screen")
Cbillsc.title("Bill")
#fonts used 
fts=font.Font(family='Helvetica',size=40,weight='bold')
subfont=font.Font(family='Helvetica',size=30,weight='bold')
nom=font.Font(family='Cloture',size=5,weight='bold')
#INITIALISNG VARIABLES
for j in range(5):
	fdvar[j]=StringVar(cussc)
for k in range(6):
	Combo_var[k]=StringVar(cussc)
Tab2=StringVar()
Tab4=StringVar()
Tab10=StringVar()

S=Label(top,text="Choose your status",
	bg="green",fg="white",font=(None,60)).place(x=360,y=100)
#Customer screen essentials
#table work
tabsql="SELECT Tnum FROM tables WHERE Availability='v'"
cursor.execute(tabsql)
G=cursor.fetchall()
S=['None']
for t in G:
	S.append(t[0])

#TABLE SELECTION COMBOBOXES
tab2select=ttk.Combobox(cussc,textvariable=Tab2,state='readonly')
tab2select.place(x=1000,y=190)
tab2select['values']=S
tab4select=ttk.Combobox(cussc,textvariable=Tab4,state='readonly')
tab4select.place(x=1000,y=250)
tab4select['values']=S
tab10select=ttk.Combobox(cussc,textvariable=Tab10,state='readonly')
tab10select.place(x=1000,y=310)
tab10select['values']=S

#PRINTING LABELS FOR BILL AND FOOD ITMES 
SF=Label(cussc,text="Select Food",bg="red",fg="white",font=(None,30)).place(x=550,y=70)
x=a=500
y=b=d=140
item=Label(cussc,text="Item",bg="white",font=(None,15)).place(x=x,y=y)
price=Label(cussc,text="Price",bg="white",font=(None,15)).place(x=x+150,y=y)
fquant=Label(cussc,text="Quantity",bg="white",font=(None,15)).place(x=x+250,y=y)


itm=Label(Cbillsc,text="Item",bg="white",font=(None,15)).place(x=450,y=y)
fqunt=Label(Cbillsc,text="Quantity",bg="white",font=(None,15)).place(x=580,y=y)
prce=Label(Cbillsc,text="Price",bg="white",font=(None,15)).place(x=690,y=y)
scost=Label(Cbillsc,text="Subcost",bg="white",font=(None,15)).place(x=800,y=y)
Label(Cbillsc,text="Tables booked",bg="white",font=(None,15)).place(x=900,y=y)

i=0
def set_price(a):
	z=0
	y=140


	try:
		for k in range(6):
			#Label(cussc,text="  ",bg="light blue",fg="black",font=(None,15)).place(x=x+60,y=190+z)
			Label(cussc,text=" "+str(foody[foody.index((items_entry["IE"+str(k)]).get())+1])+" ",bg="light blue",fg="black",font=(None,15)).place(x=650,y=190+z)
			z=z+60
	except ValueError:
		print("List does not contain value")
	"""for i in range(6):
		Label(cussc,text=menu[str(items_entry["IE"+str(i)].get())],bg="light blue",fg="black",font=(None,15)).place(x=x+60,y=190+z)"""
	#printing bill screen item choices
for i in range(6):
	#printing names of food and drinks with prices in cussc and Cbillsc
	#populating the dictionary
	foodict["{}".format(fsf[i])]=Spinbox(cussc,from_=0,to=1000,width=5,state='readonly',fg='black',textvariable=fdvar[i])
	foodict["{}".format(fsf[i])].place(x=765,y=y+50)
	items_entry["IE{}".format(i)]=ttk.Combobox(cussc,values=menu, state='readonly',textvariable=Combo_var[i])
	items_entry["IE{}".format(i)].place(x=x-25,y=y+50)
	
	items_entry["IE{}".format(i)].bind("<<ComboboxSelected>>", set_price)
	y=y+60

#Retrieving data to output as part of bill
def bill_rec():
	x=190
	i=2
	z=0
	y=[]
	Total=0
	sql="SELECT * FROM data ORDER BY ID DESC LIMIT 1"
	cursor.execute(sql)
	mybill=cursor.fetchall()

	for bill in mybill:
		y.append(bill)
	Label(Cbillsc,text="Your order no : "+str(y[0][0]),bg="light yellow",fg="black",font=(None,15)).place(x=10,y=10)
	for k in range(6):
		#PRINTING ITEM NAMES
		Label(Cbillsc,text=items_entry["IE"+str(k)].get(),bg="light yellow",fg="black",font=(None,15)).place(x=450,y=x-10)
		#Label(Cbillsc,text=y[0][i+2],bg="light yellow",fg="black",font=(None,15)).place(x=450,y=x)

		#Label(Cbillsc,text=y[0][i+2],bg="light yellow",fg="black",font=(None,15)).place(x=690,y=x)
		try:
			Total=Total+int(foodict[fsf[k]].get())*int(foody[foody.index((items_entry["IE"+str(k)]).get())+1])
		except ValueError:
			print("totality")
		i=i+2
		x=x+60
		z=z+60
	try:
		z=0
		for k in range(6):
			#PRICE
			Label(Cbillsc,text=foody[foody.index(items_entry['IE'+str(k)].get())+1],bg="light yellow",fg="black",font=(None,15)).place(x=700,y=190+z)
			Label(Cbillsc,text=int(foodict[fsf[k]].get())*int(foody[foody.index(items_entry['IE'+str(k)].get())+1]),bg="light yellow",fg="black",font=(None,15)).place(x=800,y=190+z)
			Label(Cbillsc,text="Total bill= $"+str(Total),bg="light yellow",fg="black",font=(None,15)).place(x=610,y=600)
			z=z+60
	except ValueError:
		print("hi")
	return()

for i in range(3):
	Label(cussc,text=info[i],bg="light blue",fg="black",font=(None,15)).place(x=a-500,y=b+50)
	b=b+60
Name=Entry(cussc,bd=2,width=50)
Name.place(x=100,y=140+50)
PN=Entry(cussc,bd=2,width=50)
PN.place(x=100,y=140+50+60)
Email=Entry(cussc,bd=2,width=50)
Email.place(x=100,y=140+50+120)

#CUSTOMER details
CD=Label(cussc,text="Details",bg="red",fg="white",font=(None,30)).place(x=180,y=70)
#Booking table
CD=Label(cussc,text="Book Table",bg="red",fg="white",font=(None,30)).place(x=1000,y=70)
z=k=140
m=j=900


#Equal to b and x
#PRINTING TABLE BOOKING LABELS
for i in range(3):
	Label(cussc,text=table[i],bg="light blue",fg="black",font=(None,15)).place(x=900,y=z+50)
	z=z+60
Label(cussc,text="2 seater table no start with : 2 \n 4 seater table no start with : 4 \n 10 seater table no start with : 1 " ,bg="light blue",fg="black",font=(None,15)).place(x=900,y=400)

Olab=Label(Cbillsc,text="Your Order",bg="Blue",fg="white",font=(None,30)).place(x=575,y=70)


Adm = Button(top, text ="Administrator",command=Administrator,font=fts,relief="raised",borderwidth=5)
Cus = Button(top,text="Customer",command=Customer,font=fts,width=13,relief="ridge",borderwidth=5)
Ba=Button(admsc,text="Back",command=Back,width=10,font=nom)
Bc=Button(cussc,text="Back",command=Back,width=10,font=nom)
Csubmit=Button(cussc,text="Place Order",command=confirm,font=subfont,width=14,borderwidth=2)
Billok=Button(Cbillsc,text="Okay",command=Back,font=subfont,width=14,borderwidth=2)
exit=Button(top,text="Exit",command=quit).place(x=0,y=0)

Adm.place(x=240,y=330)
Cus.place(x=740,y=330)
Ba.place(x=0,y=0)
Bc.place(x=0,y=0)
Csubmit.place(x=610,y=600)
Billok.place(x=600,y=675)


#Administration screen

AdmButt=["Generate Bill","Update","Menu","Report"]
AdmButtdict={}
UpdItmlab=["Edit:","Add:","Delete:"]


#WINDOWS
Adm_bill=Tk()
Adm_bill['bg']='orange'
Adm_bill.attributes('-fullscreen',True)
Adm_bill.withdraw()

menu_sc=Tk()
menu_sc['bg']='orange'
menu_sc.attributes('-fullscreen',True)
menu_sc.withdraw()

report_sc=Tk()
report_sc['bg']='orange'
report_sc.attributes('-fullscreen',True)
report_sc.withdraw()

#Button functions
def Back_():
	Adm_bill.withdraw()
	menu_sc.withdraw()
	report_sc.withdraw()
	admsc.update()
	admsc.deiconify()
def Bill_adm():
	admsc.withdraw()
	Adm_bill.update()
	Adm_bill.deiconify()
	y=190
	i=5
	Total=0
	query="SELECT * FROM data WHERE ID in ('"+bill_adm_combo.get()+"')"
	cursor.execute(query)
	cus_bill=cursor.fetchall()
	id_no=cus_bill[0][0]
	Label(Adm_bill,text="Order No: "+str(id_no),font=("Cloture", 30),fg='black',bg='orange').place(x=525,y=30)
	Label(Adm_bill,text="Item",bg="white",font=(None,15)).place(x=450,y=140)
	Label(Adm_bill,text="Quantity",bg="white",font=(None,15)).place(x=580,y=140)
	Label(Adm_bill,text="Price",bg="white",font=(None,15)).place(x=690,y=140)
	Label(Adm_bill,text="Subcost",bg="white",font=(None,15)).place(x=800,y=140)
	Label(Adm_bill,text="Name:      "+cus_bill[0][1],bg='white',font=(None,15)).place(x=0,y=140+50)
	Label(Adm_bill,text="Contact:   "+cus_bill[0][2],bg='white',font=(None,15)).place(x=0,y=140+50+60)
	Label(Adm_bill,text="Email:      "+cus_bill[0][3],bg='white',font=(None,15)).place(x=0,y=140+50+120)
	for j in range(6):
		try:
			Total=Total+int(cus_bill[0][i])*int(foody[foody.index(cus_bill[0][i-1])+1])

			Label(Adm_bill,text=cus_bill[0][i],fg="black",font=(None,15),bg='orange').place(x=600,y=y)
			Label(Adm_bill,text=cus_bill[0][i-1],fg="black",font=(None,15),bg='orange').place(x=450,y=y)
			Label(Adm_bill,text=foody[foody.index(cus_bill[0][i-1])+1],fg="black",font=(None,15),bg='orange').place(x=700,y=y)
			Label(Adm_bill,text=int(cus_bill[0][i])*int(foody[foody.index(cus_bill[0][i-1])+1]),bg="orange",fg="black",font=(None,15)).place(x=800,y=y)
			Label(Adm_bill,text="Total bill= $"+str(Total),bg="orange",fg="black",font=(None,15)).place(x=600,y=600)

			y=y+60	
			i=i+2	
		except ValueError:
			print("bello")
def Menu_adm():
	y=190
	i=0
	x=50
	IQ1=IQ2=IQ3=IQ4=IQ5=IQ6=0	
	admsc.withdraw()
	menu_sc.update()
	menu_sc.deiconify()
	query="SELECT * FROM food WHERE Availability='a'"
	cursor.execute(query)
	foodtab=cursor.fetchall()
	qtotal="SELECT * FROM data"
	cursor.execute(qtotal)
	itotals=cursor.fetchall()
	Label(menu_sc,text="Item",bg="white",font=(None,15)).place(x=500,y=140)
	Label(menu_sc,text="Price",bg="white",font=(None,15)).place(x=661,y=140)

	for foods in foodtab:
		Label(menu_sc,text=foods[1],font=(None,15),bg='orange').place(x=x+450,y=y)
		Label(menu_sc,text=foods[3],font=(None,15),bg='orange').place(x=x+625,y=y)
		y=y+60
	
def Update_adm():
	tablist=[t_up1.get(),t_up2.get(),t_up3.get()]
	blank=[]
	y=190
	cursor.execute("SET @price = %s " % (npedit.get()))
	for k in range(3):
		qw="SELECT Availability FROM tables WHERE Tnum=('"+tablist[k]+"')"
		cursor.execute(qw)
		stat=cursor.fetchall()
		for s in stat:
			blank.append(s[0])
		if tstat.get()=='vaccant':
			if blank[k]=='o':
				h="UPDATE tables SET Availability='v' WHERE Tnum=('"+tablist[k]+"')"
				cursor.execute(h)
				mydb.commit()
		elif tstat.get()=='occupied':
			if blank[k]=='v':
				h="UPDATE tables SET Availability='o' WHERE Tnum=('"+tablist[k]+"')"
				cursor.execute(h)
				mydb.commit()
	if delete_combo.get():
		sql="UPDATE food SET Availability='na' WHERE Name in ('"+delete_combo.get()+"')"
		cursor.execute(sql)
		mydb.commit()
	if edit_combo.get():
		if npedit.get():
			sm="UPDATE food SET Price=@price WHERE Name in ('"+edit_combo.get()+"')"
			
			cursor.execute(sm)
			mydb.commit()

	if add_name.get() in allfd:
		sql="UPDATE food SET Availability='a' WHERE Name in ('"+add_name.get()+"')"
		cursor.execute(sql)
		mydb.commit()
	elif add_name.get() not in allfd:
		a=(add_name.get(),'a',apadd.get(),0)
		cursor.execute(sq,a)
		mydb.commit()

	#w = ttk.Combobox(admsc,values=["one", "two", "three"])
	#w.pack()
def Report_adm():
	T=E=0
	m=5
	n=100
	admsc.withdraw()
	report_sc.update()
	report_sc.deiconify()
	j="SELECT * FROM data"
	cursor.execute(j)
	billy=cursor.fetchall()
	print(FEstat)
	for bill in billy:
		m=5
		for k in range(6):
			T=T+int(bill[m])
			if bill[m-1] in foody:
				E=E+int(bill[m])*int(foody[foody.index(bill[m-1])+1])
			elif bill[m-1] in FEstat:
				E=E+int(bill[m])*int(FEstat[FEstat.index(bill[m-1])+1])
			m=m+2

	#for bill in biilly:



	Label(report_sc,text="Total items sold: ",font=("Cloture", 15),fg='black').place(x=300+n,y=190)
	Label(report_sc,text=str(T),font=("Cloture", 15),fg='black',bg='orange').place(x=550+n,y=190)
	Label(report_sc,text="Total Revenue: ",font=("Cloture", 15)).place(x=300+n,y=250)
	Label(report_sc,text=str(E),font=("Cloture", 15),fg='black',bg='orange').place(x=550+n,y=250)
x=s=620
y=t=200
 #Creating the main buttons
Button(Adm_bill,text="Okay",command=Back_,font=subfont,width=14,borderwidth=2).place(x=600,y=675)
Button(menu_sc,text="Okay",command=Back_,font=subfont,width=14,borderwidth=2).place(x=600,y=675)
Button(report_sc,text="Okay",command=Back_,font=subfont,width=14,borderwidth=2).place(x=600,y=675)
Button(admsc,text="Generate Bill",command=Bill_adm,width=15,height=5,font=5).place(x=x,y=y+120)
Button(admsc,text="Update",command=Update_adm,width=15,height=5,font=5).place(x=x,y=y+120*2)
Button(admsc,text="Menu",command=Menu_adm,width=15,height=5,font=5).place(x=x,y=y+120*3)
Button(admsc,text="Report",command=Report_adm,width=15,height=5,font=5).place(x=x,y=y+120*4)
#Computing bill
#main label
CBlabel=Label(admsc,text='Bill',bg='green',fg='white',
	font=("Cloture", 15),width=20,height=2).place(x=135,y=125)
#Secondary label
Comp_Bill=Label(admsc,text="Order No.",width=14,height=2,font=5).place(x=90,y=220)
bill_adm_combo=ttk.Combobox(admsc,state='readonly',values=p,width=25,height=25)
bill_adm_combo.place(x=230,y=230)
	#done
#Updating table status
x=70
y=500

Label(admsc,text='Update Table Status',bg='green',fg='white',
	font=("Cloture", 15),width=20,height=2).place(x=150,y=400)
for i in range(3):
	Label(admsc,text=table[i],font=("Cloture", 15)).place(x=x,y=y)
	y=y+50

tab_update="SELECT Tnum FROM tables"
cursor.execute(tab_update)
G=cursor.fetchall()
S_update=[]
for t in G:
	S_update.append(t[0])
Label(admsc,text="Status: ",font=("Cloture", 15)).place(x=x,y=y)
tstat=ttk.Combobox(admsc,state='readonly',values=["vaccant","occupied"])
tstat.place(x=x+130,y=y)
t_up1=ttk.Combobox(admsc,state='readonly',values=S_update)
t_up1.place(x=200,y=500)
t_up2=ttk.Combobox(admsc,state='readonly',values=S_update)
t_up2.place(x=200,y=550)
t_up3=ttk.Combobox(admsc,state='readonly',values=S_update)
t_up3.place(x=200,y=600)
#Updating items

x=620
y=200
Label(admsc,text='Update Items',bg='green',fg='white',
	font=("Cloture", 15),width=20,height=2).place(x=950,y=20)
for k in range(3):
	Label(admsc,text=UpdItmlab[k],font=("Cloture", 16)).place(x=x+250,y=y-80)
	Label(admsc,text="Item Name: ",font=("Cloture", 16),bg='light pink').place(x=x+250,y=y-30)
	y=y+200

#EDIT ITEMS
npedit=StringVar(admsc)
apadd=StringVar(admsc)
Label(admsc,text="New Name: ",font=("Cloture", 16),bg='light pink').place(x=x+250,y=220)
Label(admsc,text="New Price: ",font=("Cloture", 16),bg='light pink').place(x=x+250,y=270)
New_price=Spinbox(admsc,bd=2,width=26,from_=0,to=1000,state='readonly',textvariable=npedit)
New_price.place(x=x+370,y=220)
edit_combo=ttk.Combobox(admsc,state='readonly',values=menu,width=25)
edit_combo.place(x=x+370,y=175)

#DEL ITEM
delete_combo=ttk.Combobox(admsc,state='readonly',values=menu,width=25)
delete_combo.place(x=x+370,y=575)

#ADD ITEM
Label(admsc,text="Price: ",font=("Cloture", 16),bg='light pink').place(x=x+250,y=420)
add_name=Entry(admsc,width=27,bd=2)
add_name.place(x=x+370,y=370)
add_price=Spinbox(admsc,bd=2,width=27,from_=0,to=1000,state='readonly',textvariable=apadd)
add_price.place(x=x+370,y=420)


cussc.mainloop()
admsc.mainloop()
top.mainloop()

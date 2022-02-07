from tkinter import *
from tkinter import messagebox
import sqlite3

variable=""

#Funciones y logica de la interfece
#Crear la base de datos con la funcion conexion

def conexion():
    conectar=sqlite3.connect("base.db")
    datos=conectar.cursor()
    datos.execute('''CREATE TABLE INVENTARIO(Id INTEGER, Producto text,Nombre text,Existencia INTEGER) ''')
    messagebox.showinfo("base","La base de datos fue creada con exito")
#Eliminar los campos de las entradas de texto

def eliminar():
    user.set("")
    producto.set("")
    nombre.set("")
    cantidad.set("")

#Insertar los valores a la tabla ya creada

def crear():
    conectar=sqlite3.connect("base.db")
    datos=conectar.cursor()
    lista=[(user.get()),(producto.get()),(nombre.get()),(cantidad.get())]
    datos.execute("INSERT INTO INVENTARIO VALUES(?,?,?,?)",lista)
    conectar.commit()
    messagebox.showinfo("base","Se Insertaron los valores con exito")

def leer():
    conectar=sqlite3.connect("base.db")
    datos=conectar.cursor()
    datos.execute("SELECT * FROM INVENTARIO WHERE ID=" + user.get())
    leer=datos.fetchall()
    for i in leer:
        user.set(i[0])
        producto.set(i[1])
        nombre.set(i[2])
        cantidad.set(i[3])
    conectar.commit()

def ingresar():
    conectar=sqlite3.connect('base.db')
    datos=conectar.cursor()
    lista=[(user.get()),(producto.get()),(nombre.get()),(cantidad.get())]
    #producto.get()
    datos.execute("UPDATE INVENTARIO SET Producto='"+producto.get()+
            "',Nombre='"+nombre.get()+
            "',Existencia='"+cantidad.get()+
            "' WHERE ID="+user.get())
    conectar.commit()
        



#Raiz de la interfece 
raiz=Tk()
raiz.title("Base de datos")
#configuracion de la raiz 
raiz.config(bg="black")
raiz.geometry("450x500")
#configuracion del frame en la raiz
frame=Frame(raiz)

frame.pack()
frame.config(bg="silver",height=200,width=350)


frame2=Frame(raiz)
frame2.pack()
frame2.config(bg="black",height=200,width=300)

frame3=Frame(raiz)
frame3.pack()

#Caja de texto

#texto=Text(frame3)
#texto.pack()

#Variables de tipo texto para los entradas de texto
user=StringVar()
producto=StringVar()
nombre=StringVar()
cantidad=StringVar()


#label=Label(raiz,text="alex-stone-666")
#label.pack()
#Botones y entradas de texto
var1=Entry(frame,textvariable=user)
var1.grid(row=0,column=1,padx=15,pady=15)

var2=Entry(frame,textvariable=producto)
var2.grid(row=1,column=1,padx=15,pady=15)

var3=Entry(frame,textvariable=nombre)
var3.grid(row=2,column=1,padx=15,pady=15)

var4=Entry(frame,textvariable=cantidad)
var4.grid(row=3,column=1,padx=15,pady=15)

#Etiquetas de la interface
etiqueta1=Label(frame,text="Id")
etiqueta1.grid(row=0,column=0,sticky="e",padx=15,pady=15)

etiqueta2=Label(frame,text="Tipo de producto")
etiqueta2.grid(row=1,column=0,sticky="e",padx=15,pady=15)

etiqueta3=Label(frame,text="Nombre de producto")
etiqueta3.grid(row=2,column=0,sticky="e",padx=15,pady=15)

etiqueta4=Label(frame,text="Cantidad")
etiqueta4.grid(row=3,column=0,sticky="e",padx=15,pady=15)

#Los botones de la interface

boton1=Button(frame2,text="Crear",command=crear)
boton1.grid(row=0,column=0,sticky="s",padx=10,pady=10)
boton1.config(bg="orange")

boton2=Button(frame2,text="Leer",command=leer)
boton2.grid(row=0,column=1,sticky="s",padx=10,pady=10)
boton2.config(bg="orange")

boton3=Button(frame2,text="Actualizar",command=ingresar)
boton3.grid(row=0,column=2,sticky="s",padx=10,pady=10)
boton3.config(bg="orange")

boton4=Button(frame2,text="Eliminar",command=eliminar)
boton4.grid(row=0,column=3,sticky="s",padx=10,pady=10)
boton4.config(bg="orange")

boton5=Button(frame2,text="Conexion",command=conexion)
boton5.grid(row=1,column=1,padx=10,pady=10)
boton5.config(bg='green')

boton6=Button(frame2,text="Salir",command=raiz.destroy)
boton6.grid(row=1,column=2,padx=10,pady=10)
boton6.config(bg="red")

#boton1=Button(frame)
#boton1.pack()
#boton1.config(text="Insertete la.informacion",bg="orange")




raiz.mainloop()

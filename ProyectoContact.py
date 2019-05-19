import os.path as path
import time

#variables para texto de menu principal
textoTitulo = " Proyecto Contact Manager App "
textoOpcion = "\n Selecciona una opcion \n"
opcion1 = " 1. Agregar contacto  \n"
opcion2 = " 2. Lista de contactos  \n"
opcion3 = " 3. Eliminar contacto  \n"
opcion4 = " 4. Carga desde archivo local \n"
opcion5 = " 5. Carga desde archivo externo \n"
opcion6 = " 6. Interaccion contactos  \n"
opcion7 = " 7. Obtener Contactos Web  \n"
opcion8 = " 8. Cargar Contactos Web  \n"
opcionExit = "9. Exit \n"

#se imprimen las variables del menu principal en la consola
print(textoTitulo.center(100, "-"))
print(textoOpcion)
print(opcion1)
print(opcion2)
print(opcion3)
print(opcion4)
print(opcion5)
print(opcion6)
print(opcion7)
print(opcion8)
print(opcionExit)


#variable listaVacia principal, contactoNuevo para datos de contacto, Golbales para que intractuen en todos metodos 
listaVacia = []
contactoNuevo = []
listaFavoritos = []

#Metodo que parte el texto de listaVacia y devuelve el elemento de la lista de apellido (posicion 2) y cuando no encuentra apellido
#devuelve nombre (posicion 1)
def ordenarContacto(elem):
    arregloContacto = elem.split(",")
    if(arregloContacto[2] != ""):
        return arregloContacto[2]
    else:
        return arregloContacto[1]

#metodo para agregar contactos
def addContact(nombre, apellido, telefono, contadorContactos): 
        
    listaVacia.append(str(contadorContactos) + "," + nombre.strip() + "," + apellido.strip() + "," + telefono.strip())




#metodo para ordenar y mostrar tabla "pretty" de contactos
def listContacts(): 
   
    snombre = "Nombre"
    sapellido = "Apellido"
    sContactID = "ContactID"
    sTel = "Telefono"
    print("\n{0:10} {1:10} {2:10} {3:10} \n" .format(sContactID, snombre, sapellido, sTel)) 
   
    listaVacia.sort(key=ordenarContacto)
    for contacto in listaVacia:
        arregloContactos = contacto.split(",")
        IDcontacto = arregloContactos[0]
        nombre = arregloContactos[1]
        apellido = arregloContactos[2]
        tel = arregloContactos[3]           
        print("{0:10} {1:10} {2:10} {3:10}" .format(IDcontacto, nombre, apellido, tel))



#ciclo de menu principal que permite navegar entre todas las opciones de la app
while exitSeleccion == False:
    seleccion = input("\n ¿Que opcion deseas? : ")
    terminado1 = False

#condicionales if de menu principal, son 7 opciones

    if seleccion == "1": # 1. Agregar contacto
        contadorContactos = 0
        for filas in listaVacia:
                contadorContactos += 1
        while terminado1 == False:			
            nombrein = input("\n Nombre: ")
            apellidoin = input("\n Apellido: ")
            telefonoin = input("\n Telefono: ")
            contadorContactos = contadorContactos + 1;
            addContact(nombrein,apellidoin,telefonoin, contadorContactos)
            continuar = input("\n Escribe 1 si deseas agregar mas contactos, 0 si has terminado: ")
            if(continuar == "0"):
                terminado1 = True
                
    elif seleccion == "2":  # Lista de contactos
        listContacts() 


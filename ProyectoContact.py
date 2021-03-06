import time 
import os.path as path
import requests
import json

def menu():


    # variables para texto de menu principal
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

    # se imprimen las variables del menu principal en la consola
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

menu()

#variables para texto de sub menu (fase 3)
fase3Opcion1 = "\n 1. Llamar Contacto  \n"
fase3Opcion2 = " 2. Mensaje Contactos  \n"
fase3Opcion3 = " 3. Agregar Contacto Favoritos  \n"
fase3Opcion4 = " 4. Lista Favoritos  \n"
fase3Opcion5 = " 5. Eliminar Contacto Favorito  \n"
fase3Opcion6 = " 6. Exit sub menu  \n"

#variable listaVacia principal, contactoNuevo para datos de contacto, Golbales para que intractuen en todos metodos 
listaVacia = []
contactoNuevo = []
listaFavoritos = []

#variables para fase 6 (web apis) 
rutaWeb = 'https://tinyurl.com/yygujcbg/contacts?gid=1000'



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

#metodo para eliminar un contacto buscandolo con nombre y apellido
def removeContact(nombre,apellido):
    
    for contacto in listaVacia:
        arregloContacto = contacto.split(",") 
        nombreContactoLista = arregloContacto[1]
        apellidoContactoLista = arregloContacto[2]
        if str(nombreContactoLista).upper() == nombre.strip().upper() and str(apellidoContactoLista).upper() == apellido.strip().upper():
            listaVacia.remove(contacto)
            print("\n Contacto eliminado")

#metodo para cargar archivo local en la lista de contactos
def loadLocalFile():
    dirFichero ='InitialContacts.txt'
    if(path.exists(dirFichero)):
        with open(dirFichero, 'r',1, 'cp1252') as reader:
            cantidadID = 0
            for filas in listaVacia:
                    cantidadID += 1

            for linea in reader: 
                cantidadID = cantidadID + 1
                arregloContactoLocal = linea.split(",")
                nombreLocal = arregloContactoLocal[0]
                apellidoLocal = arregloContactoLocal[1]
                telefonoLocal = arregloContactoLocal[2]
            
                addContact(nombreLocal, apellidoLocal, telefonoLocal, cantidadID)

            print("\n Archivo cargado exitosamente.")
    else:
        print("\n El archivo " + dirFichero + " no existe en la carpeta local.")

#metodo para cargar archivo de carpeta externa en la lista de contactos
#puede recibir .txt separados por "," o .csv separados por ";" u otros archivos de texto separados por ","
def loadFromFile(externalFile):

    if(path.exists(externalFile)):
        with open(externalFile, 'r', 1, 'cp1252') as reader:

            cantidadID = 0
            for filas in listaVacia:
                cantidadID += 1
            
            if path.splitext(externalFile)[1] == ".txt":
                for linea in reader:
                    cantidadID = cantidadID + 1
                    arregloContactoLocal = linea.split(",")
                    nombreLocal = arregloContactoLocal[0]
                    apellidoLocal = arregloContactoLocal[1]
                    telefonoLocal = arregloContactoLocal[2]
                    addContact(nombreLocal, apellidoLocal, telefonoLocal, cantidadID)
            elif path.splitext(externalFile)[1] == ".csv":
                for linea in reader:
                    cantidadID = cantidadID + 1
                    arregloContactoLocal = linea.split(";")
                    nombreLocal = arregloContactoLocal[0]
                    apellidoLocal = arregloContactoLocal[1]
                    telefonoLocal = arregloContactoLocal[2]
                    addContact(nombreLocal, apellidoLocal, telefonoLocal, cantidadID)
            else:
                for linea in reader:
                    cantidadID = cantidadID + 1
                    arregloContactoLocal = linea.split(",")
                    nombreLocal = arregloContactoLocal[0]
                    apellidoLocal = arregloContactoLocal[1]
                    telefonoLocal = arregloContactoLocal[2]
                    addContact(nombreLocal, apellidoLocal, telefonoLocal, cantidadID)

            print("\n Archivo cargado exitosamente.")
    
    else:
        print("\n El archivo de contactos en la ruta " + externalFile + " no existe.")

#metodo que muestra mensaje de llamando contacto (si existe) por 60 segundos
def callContact(IDcontacto):
    
    if datosContactoID(IDcontacto):
        print("\n Llamando a : " + datosContactoID(IDcontacto)[1] + " " + datosContactoID(IDcontacto)[2] )
        print(" Telefono : " + str(datosContactoID(IDcontacto)[3]))
        tiempoTranscurrido = 0

        while tiempoTranscurrido < 15:
            tiempoInicial = time.time()       
            tiempoFinal = time.time()
            tiempoTranscurrido = tiempoTranscurrido + (tiempoFinal - tiempoInicial)

                  
        print("\n Llamada finalizada")
    else:
         print("\n ContactoID no existe")


#metodo que devuelve los datos de un contacto (ID, nombre, apellido, telefono) en un arreglo (lista)
def datosContactoID(IDcontacto):
    arregloContactoID = []
    contactoExiste = False
    for fila in listaVacia:
        arregloContactoID = fila.split(",")
        contactoID = arregloContactoID[0]
        if contactoID == str(IDcontacto):
            contactoExiste = True
            break

    if contactoExiste == False:
        arregloContactoID = []


    return arregloContactoID

#metodo que carga a lista con contactos para enviar mensaje
def msgContacts(IDcontacto):
    
    infoContacto = datosContactoID(IDcontacto)
    if infoContacto:
        listaContactosMsj.append(infoContacto[1] + " " + infoContacto[2] + " ( " + infoContacto[3] + " ) ")
    else:
        print("\n ContactoID no existe")

#metodo que devuelve el texto de los contactos concatenados para mensaje            
def listamsjContactos():
    listaContactos = ""
    contadorContacts = 1
    for linea in listaContactosMsj:
        
        if contadorContacts == 1:
            listaContactos = "\n To: " + linea
            contadorContacts = contadorContacts + 1
        else:            
            listaContactos = listaContactos + ", " + linea

    return listaContactos

#metodo que agrega un contacto existente a la lista de favoritos
def addToFavorite(IDcontacto): 
    
    if datosContactoID(IDcontacto):
        listaFavoritos.append(datosContactoID(IDcontacto)[0] + "," + datosContactoID(IDcontacto)[1] + "," + datosContactoID(IDcontacto)[2] + "," + datosContactoID(IDcontacto)[3]) 
    else:
        print("\n ContactoID no existe")

#metodo que devuelve la lista de contactos favoritos con todos sus datos y ordenados por apellido y nombre    
def getFavoriteList(): 

    snombre = "Nombre"
    sapellido = "Apellido"
    sContactID = "ContactID"
    sTel = "Telefono"
    print("\n{0:10} {1:10} {2:10} {3:10} \n" .format(sContactID, snombre, sapellido, sTel))    
    listaFavoritos.sort(key=ordenarContacto)

    for contacto in listaFavoritos:
        arregloContactos = contacto.split(",")
        IDcontacto = arregloContactos[0]
        nombre = arregloContactos[1]
        apellido = arregloContactos[2]
        tel = arregloContactos[3]           
        print("{0:10} {1:10} {2:10} {3:10}" .format(IDcontacto, nombre, apellido, tel))

#metodo que elimina un contacto recibiendo nombre y apellido de la lista de favoritos
def removeFromFavorite(nombre,apellido):
    
    for contactofav in listaFavoritos:
        arregloContactofav = contactofav.split(",") 
        nombreContactoListafav = arregloContactofav[1]
        apellidoContactoListafav = arregloContactofav[2]
        if str(nombreContactoListafav).upper() == nombre.strip().upper() and str(apellidoContactoListafav).upper() == apellido.strip().upper():
            listaFavoritos.remove(contactofav)
            print("\n Contacto eliminado de favoritos")

#metodo que utiliza el GET (lee) de la api dada para obtener los datos de los contactos y guardarlos en la lista
def GETcontactosAPI():
    req = requests.get(rutaWeb)

    contadorContactos = 0
    for filas in listaVacia:
        contadorContactos += 1

    for contacto in req.json():
        #print(usuario['FirstName'])
        contadorContactos = contadorContactos + 1;
        nombreweb = contacto['FirstName']
        apellidoweb = contacto['LastName']
        telefonoweb = contacto['Phone']
        addContact(nombreweb,apellidoweb,telefonoweb, contadorContactos)

    print("\n Contactos web obtenidos exitosamente")

#metodo que hace POST (inserta) en la api con los contactos en la lista actual
def POSTcontactoAPI():
  
    contadorContactsWeb = 0
    jsonContactos = ''
    for filas in listaVacia:
        arregloContactoPost = filas.split(",")
        if contadorContactsWeb == 0:
            jsonContactos =  ' { ' + '"FirstName":' + '"' + arregloContactoPost[1] + '"' + ',' + '"LastName":' + '"' + arregloContactoPost[2] + '"' + ',' + '"Phone":' + '"' + arregloContactoPost[3] + '"' +  ' } '
            contadorContactsWeb = 1;
        else:
            jsonContactos = jsonContactos + ', ' + ' { ' + '"FirstName":' + '"' + arregloContactoPost[1] + '"' + ',' + '"LastName":' + '"' + arregloContactoPost[2] + '"' + ',' + '"Phone":' + '"' + arregloContactoPost[3] + '"' +  ' } '
    
    #string con formato json de los datos de la lista
    jsonContactosListo = '[ ' + jsonContactos + ' ]'    
    # convertir cadena en JSON:
    dataPost = json.loads(jsonContactosListo)
    req = requests.post(rutaWeb, json = dataPost )
    print("\n Contactos web cargados exitosamente")



#variable para ciclo de menu principal, es la que condiciona que no termine el programa hasta que se elija la opcion exit
exitSeleccion = False

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
        menu()

    elif seleccion == "2":  # Lista de contactos
        listContacts()
        menu()
    elif seleccion == "3":  # 3. Eliminar contacto
        nombreDel = input("\n Nombre: ") 
        apellidoDel = input("\n Apellido: ")
        removeContact(nombreDel,apellidoDel)
        menu()
    elif seleccion == "4":  # 4. Carga desde archivo local
        loadLocalFile()
        menu()
    elif seleccion == "5":  # 5. Carga desde archivo externo
        ruta = input("\n Ingresa la ruta del archivo de contactos: ")
        loadFromFile(ruta)
        menu()
    elif seleccion == "6":  # 6. Interaccion contactos (sub menu - fase 3)
        print("\n Sub menu Interaccion Contactos \n".center(100, "-"))
        print(fase3Opcion1)
        print(fase3Opcion2)
        print(fase3Opcion3)
        print(fase3Opcion4)
        print(fase3Opcion5)
        print(fase3Opcion6)
        
        #variable que permite el ciclo de sub menu y hasta que cambie saldra al menu principal
        terminosubMenu = False

        #ciclo que se mantiene en las opciones de sub menu fase 3
        while terminosubMenu == False:
            opcionInteraccion = input("\n Ejecutar opcion : ")
        
            if opcionInteraccion == "1":  # 1. Llamar Contacto
                xcontactID = input("\n Ingresa el contactcID : ")
                callContact(xcontactID)
            elif opcionInteraccion == "2":  # 2. Mensaje Contactos
                listaContactosMsj = []
                terminadoMsjContacto = False
                while terminadoMsjContacto == False:			
                    msjContactID = input("\n ContactID : ")
                    msgContacts(msjContactID)
                    continuar = input("\n Escribe 1 si deseas agregar mas contactos, 0 si has terminado: ")
                    if(continuar == "0"):
                        terminadoMsjContacto = True
                        contactosSeleccionados = listamsjContactos()
                        mensaje = input("\n Escribe tu mensaje : ")
                        print(contactosSeleccionados)
                        print("\n Msj: " + mensaje)
                                  
            elif opcionInteraccion == "3":  # 3. Agregar Contacto Favoritos 

                contadorFavoritos = 0
                terminadoAddFavoritos = False
                while terminadoAddFavoritos == False:			
                    IDcontactofav = input("\n ContactID: ")               
                    addToFavorite(IDcontactofav)
            
                    continuar = input("\n Escribe 1 si deseas agregar mas contactos, 0 si has terminado: ")
                    if(continuar == "0"):
                        terminadoAddFavoritos = True

            elif opcionInteraccion == "4":  # 4. Lista Favoritos
                getFavoriteList()
            elif opcionInteraccion == "5":  # 5. Eliminar Contacto Favorito
                nombreDelfav = input("\n Nombre: ") 
                apellidoDelfav = input("\n Apellido: ")
                removeFromFavorite(nombreDelfav,apellidoDelfav)
            elif opcionInteraccion == "6":  # 6. Exit sub menu
                terminosubMenu = True
                menu()
     
    elif seleccion == "7":  # 7. Obtener Contactos Web
        GETcontactosAPI()
        menu()
    elif seleccion == "8":  # 8. Cargar Contactos Web
        POSTcontactoAPI()
        menu()
        
    elif seleccion == "9":  # 9. Exit
        exitSeleccion = True

print(" \n Termino")

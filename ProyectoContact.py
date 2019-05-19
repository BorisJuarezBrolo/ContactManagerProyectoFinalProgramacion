

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

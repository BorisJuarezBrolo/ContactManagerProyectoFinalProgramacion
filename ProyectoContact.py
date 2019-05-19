

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


while exitSeleccion == False:
    seleccion = input("¿Que opcion deseas? : ")
    terminado1 = False
   
    if seleccion == "1": 
        contadorContactos = 0
        for filas in listaVacia:
                contadorContactos += 1

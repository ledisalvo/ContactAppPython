def Menu():
    print("      AGENDA DE CONTACTOS       ")
    print('--------------------------------')
    print('1 - Ingresar nuevo contacto')
    print('2 - Modificar contacto')
    print('3 - Eliminar contacto')
    print('4 - Mostrar todos los contactos')
    opcion = int(input('Por favor seleccione una opción: '))
    print('Su opción elegida es: ' + str(opcion))   #   me devuelve algo <-- nombre_funcion(recibe_algo)
    return input('¿Es esto correcto? S/N: ')[0]

def Handle_selection(confirmation):
    if (confirmacion == 'S') :
        if (opcion == 1):
            #Ingresa un nuevo contacto
            print('Ingresando nuevo contacto...')
        elif (opcion == 2):
            #Modificame el contacto papá
            print('Modificando el contacto...')
        elif (opcion == 3):
            #Elimina el contacto
            print('Eliminando el contacto...')
        elif (opcion == 4):
            #Mostrame todos los contactos
            print('Mostrando los contactos...')
        else:
            #Mostrar error:
            print('Por favor ingrese una opción entre 1 y 4')

def Main():
    global confirmation
    confirmation = Menu()
    Handle_selection(confirmation)

Main()
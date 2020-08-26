# El nombre de las funciones se recomienda que sean escritas de forma expeditiva y en inglés
# Ejemplo --> dame_los_contactos() --> (osea) --> get_contacts()
# Las variables también recomiendo que se escriban en inglés, de hecho, lo único que puede
# estar en español son los comentarios --> ( PONELE, yo los escribo en inglés)
from os import system

#En plural porque va a ser una lista de contactoSSS
contacts = []

def clear():
    system('cls')

#------------------- MENU -----------------------------

def menu():
    clear()
    print("      AGENDA DE CONTACTOS       ")
    print('--------------------------------')
    print('1 - Ingresar nuevo contacto') #OK
    print('2 - Modificar contacto')
    print('3 - Eliminar contacto')
    print('4 - Mostrar todos los contactos') #OK
    print('5 - Salir de la agenda') #OK
    return int(input('Por favor seleccione una opción: '))


    #print('Su opción elegida es: ' + str(opcion))   #   me devuelve algo <-- nombre_funcion(recibe_algo)
    #return input('¿Es esto correcto? S/N: ')[0]

#----------------- CREAR UN CONTACTO -------------------
def create_contact():
    name = input('Nombre: ')
    last_name = input('Apellido: ')
    phone = input('Teléfono: ')
    mail = input('E-mail: ')
    birthdate = input('Fecha de nacimiento: ')

    #Creamos un diccionario para especificar una lista con elementos tipo clave-valor
    #En donde la clave es el campo y el valor lo que ingresa el usuario

    contact = {'name': name, 'last_name': last_name, 'phone': phone, 'mail': mail, 'birthdate': birthdate}

    #Para agregar un item a una lista utilizar la función append().
    contacts.append(contact)

#----------------- LISTAR TODOS LOS CONTACTOS -------------------
def read_contacts():
    if (len(contacts) > 0):
        for contact in contacts:
            print('------------------------------------')
            print('Nombre: ' + contact['name'])
            print('Apellido: ' + contact['last_name'])
            print('Teléfono: ' + contact['phone'])
            print('Mail: ' + contact['mail'])
            print('Cumpleaños: ' + contact['birthdate'])
            print('------------------------------------')
    else:
        clear()
        print('No hay contactos para mostrar')
        input('Presione cualquier tecla para continuar...')

#----------------- MODIFICAR UN CONTACTO -------------------
def update(index, key, label):
    new_name = input(label)
    if len(new_name) > 0:
        contacts[index][key] = new_name

def update_contact():
    # Buscar el contacto a actualizar y tomar la posición (index) en la que se encuentra ese diccionario
    # [{Diccionario 1}, {Diccionario 2}, {Diccionario 3}]
    #        0                  1                2

    contact_mail = input('Ingrese el mail del contacto: ')

    # La función next lleva 2 parametros (iterador, valor por default)
    # Que es el iterador? --> Es un ciclo for que itera la colección (contactos) y en caso de que se de
    # la condición, devuelve ese contacto, si no devuelve un valor por default (2do parámetro)
    #
    # La función Index lo que hace es devolver el index según lo que le pasemos por parámetro
    # (en este caso estamos pasando el resultado de lal función next)

    contact_searched = contacts.index(next((contact for contact in contacts if contact['mail'] == contact_mail), None))

    # tenemos que acceder a ese diccionario en particular
    # Tenemos que preguntarle al usuario QUE campo quiere modificar
    # Actualizar el contacto

    print('Si no quiere modificar un campo, aprete Enter')
    update(contact_searched, 'name', 'Nombre: ')
    update(contact_searched, 'last_name', 'Apellido: ')
    update(contact_searched, 'phone', 'Teléfono: ')
    update(contact_searched, 'mail', 'Mail: ')
    update(contact_searched, 'birthdate', 'Cumpleaños: ')

#----------------- BORRAR UN CONTACTO -------------------
def delete_contact():
    contact_mail = input('Ingrese el mail del contacto: ')
    contact_searched = next((contact for contact in contacts if contact['mail'] == contact_mail), None)
    response = input('¿Está seguro que desea eliminar este contacto?')[0]
    if (response == 's'):
        contacts.remove(contact_searched)
        print('Contacto eliminado')
    else:
        print('Ok..entonces aquí no ha pasado nada!')

def handle_selection(option):
        if option == 1:
            #Ingresa un nuevo contacto
            create_contact()
        elif option == 2:
            #Modificame el contacto papá
            update_contact()
        elif option == 3:
            #Elimina el contacto
            delete_contact()
        elif option == 4:
            #Mostrame todos los contactos
            read_contacts()
        elif option == 5:
            # Despedir al usuario
            clear()
            print('Gracias por utilizar nuestra agenda')
        else:
            #Mostrar error:
            print('Por favor ingrese una opción entre 1 y 4')

def Main():
    option_selected = menu()
    handle_selection(option_selected)
    while option_selected != 5:
        option_selected = menu()
        handle_selection(option_selected)

Main()
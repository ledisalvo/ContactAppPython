from os import system

contacts = []

#--------------- COMMON ----------------#
def clear():
    #print('\n' * 20)
    system('cls')

def init_section(title):
    clear()
    title_operation(title)

#--------------- MENU SECTION ----------------#
def menu():
    clear()
    option = show_menu()
    while not selected_option_ok(option):
        clear()
        option = show_menu()
    return option

def left_top_corner():
    return '╔'

def right_top_corner():
    return '╗'

def horizontal_line_bold(quantity):
    result = ''
    for x in range(quantity):
        result += '═'
    return result

def horizontal_line(quantity):
    result = ''
    for x in range(quantity):
        result += '-'
    return result

def left_bottom_corner():
    return '╚'

def right_bottom_corner():
    return '╝'

def show_menu():
    WIDTH = 32
    print(left_top_corner() + horizontal_line_bold(WIDTH) + right_top_corner())
    print('║      AGENDA DE CONTACTOS       ║')
    print('║--------------------------------║')
    print('║ 1 - Ingresar nuevo contacto    ║')
    print('║ 2 - Modificar contacto         ║')
    print('║ 3 - Eliminar contacto          ║')
    print('║ 4 - Mostrar todos los contactos║')
    print('║ 5 - Salir                      ║')
    print(left_bottom_corner() + horizontal_line_bold(WIDTH) + right_bottom_corner())
    return select_option()

def select_option():
    return int(input('Por favor seleccione una opción: '))

def selected_option_ok(option):
    #print('Su opción elegida es: ' + str(option))
    response = input('Su opción elegida es: ' + str(option) + ' - ¿Es esto correcto? S/N: ')[0]
    if response.upper() == 'S':
        return True
    else:
        return False

#---------------OPERATIONS-------------------#

def title_operation(title):
    line_open = '__.::'
    line_close = '::.__'
    print(horizontal_line_bold(30))
    print(line_open + title + line_close)
    print(horizontal_line_bold(30))

def back_to_menu_message():
    input('Presione cualquier tecla para volver al menú...')

def create_contact():
    name = input('Nombre: ')
    last_name = input('Apellido: ')
    email = input('E-mail: ')
    phone = input('Teléfono: ')
    return {'name': name, 'last_name': last_name, 'email': email, 'phone': phone}

def create_contact_section():
    init_section('CREAR CONTACTO')
    data = create_contact()
    contacts.append(data)

    horizontal_line_bold(20)
    print('¡Contacto agregado!')
    print('\n')
    back_to_menu_message()

def read_contacts():
    init_section('MOSTRAR CONTACTOS')
    if (len(contacts) > 0):
        for contact in contacts:
            print(horizontal_line(20))
            print('Nombre: ' + contact['name'])
            print('Apellido: ' + contact['last_name'])
            print('E-mail: ' + contact['email'])
            print('Teléfono: ' + contact['phone'])
            print(horizontal_line(20))
    else:
        print('No hay contactos en la agenda.')
        print('\n')
    back_to_menu_message()

def search_contact():
    email = input('Ingrese el mail de la persona: ')
    return contacts.index(next((sub for sub in contacts if sub['email'] == email), None))

def modify_contact(field_name, index, key_name):
    new_value = input(field_name + ' actual: ' + contacts[index][key_name] + ' nuevo: ')
    if len(new_value) > 0:
        contacts[index][key_name] = new_value

def modify_contact_section():
    init_section('EDITAR CONTACTO')
    searched_contact_index = search_contact()
    print('Presione la tecla "Enter" para omitir cambios en ese campo.')
    modify_contact("Nombre", searched_contact_index, 'name')
    modify_contact("Apellido", searched_contact_index, 'last_name')
    modify_contact("E-Mail", searched_contact_index, 'email')
    modify_contact("Teléfono", searched_contact_index, 'phone')
    back_to_menu_message()

#---------------OPERATIONS-------------------#

def handle_selection(option):
    if (option == 1):
        create_contact_section()
    elif (option == 2):
        modify_contact_section()
    elif (option == 3):
        #Elimina el contacto
        print('Eliminando el contacto...')
    elif (option == 4):
        read_contacts()
    elif (option == 5):
        clear()
    else:
        #Mostrar error:
        print('Por favor ingrese una opción entre 1 y 5')

def Main():
    option = 0
    while option != 5:
        option = menu()
        handle_selection(option)
    print('Gracias por usar la agenda de contactos')
Main()
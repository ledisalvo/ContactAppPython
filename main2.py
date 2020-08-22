def menu():
    global opcion
    print("-----------CONTACTOS APP-----------")
    print("1 - Crear nuevo contacto")
    print("2 - Modificar contacto")
    print("3 - Eliminar contacto")
    print("4 - Salir")
    opcion = input("Ingrese la opción deseada: ")

def crear_contacto():
    

def main():
    menu()
    if (opcion > 0 and opcion < 5):
        switcher = {
            1: crear_contacto()
            2: modificar_contacto()
            3: eliminar_contacto()
            4: salir()
        }










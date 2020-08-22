def main():
    global opcion
    pedido_ingreso_datos()
    opcion = menu()
    manejador_opciones(opcion)


def sumar_dos_numeros(primer_numero, segundo_numero):
    return primer_numero + segundo_numero

def multiplicar_dos_numeros(primer_numero, segundo_numero):
    return primer_numero * segundo_numero

def dividir_dos_numeros(primer_numero, segundo_numero):
    return primer_numero / segundo_numero

def restar_dos_numeros(primer_numero, segundo_numero):
    return primer_numero - segundo_numero

def mostrar_resultado(texto, resultado):
    return 'El resultado de la ' + texto + ' es: ' + str(resultado)

def pedido_ingreso_datos():
    global numero_uno
    global numero_dos
    numero_uno = int(input('Ingrese el primer número: '))
    numero_dos = int(input('Ingrese el segundo número: '))

def menu():
    print("      OPERACIONES MATEMATICAS       ")
    print('--------------------------------')
    print('1 - SUMAR')
    print('2 - RESTAR')
    print('3 - MULTIPLICAR')
    print('4 - DIVIDIR')
    return int(input('Por favor seleccione una opción: '))


def manejador_opciones(opcion):
    global resultado
    if (opcion == 1):
            resultado = sumar_dos_numeros(numero_uno, numero_dos)
            print(mostrar_resultado('suma', resultado))
    elif (opcion == 2):
            resultado = restar_dos_numeros(numero_uno, numero_dos)
            print(mostrar_resultado('resta', resultado))
    elif (opcion == 3):
            resultado = multiplicar_dos_numeros(numero_uno, numero_dos)
            print(mostrar_resultado('multiplicacion', resultado))
    elif (opcion == 4):
            resultado = dividir_dos_numeros((numero_uno, numero_dos))
            print(mostrar_resultado('division', resultado))
    else:
        #Mostrar error:
        print('Por favor ingrese una opción entre 1 y 4')


main()
import numpy

def mostrarArreglo(p_array):
    lista_impares = [9,7,5,3,1,-1,-3,-5,-7,-9]
    print("                ________")
    for x in range(10):
        if x == 0:
            print(f"Piso numero {lista_impares[x]+(x+1)} |",end="")
        else:
            print(f"Piso numero {lista_impares[x]+(x+1)}  |",end="")
        for i in range(4):
            print(p_array[x][i], end=" ")
        if x == 9:
            print(f"| 150$ Millones",end="")
        if x == 2:
            print(f"| 200$ Millones",end="")
        print("|")
    print("Columna         1 2 3 4")
array = numpy.zeros((10,7), int)
array_invertido = numpy.flipud(array)

def solicitarPago(p_subtotal):
    total = p_subtotal
    return total

def menu():
    print("""Sistema de compra de departamentos
          1. Ver departamentos disponibles
          2. Comprar departamento
          3. Buscar dueño
          4. Total ganancias
          5. Salir
          """)
    
def uRur():
    while True:
        try:
            rut = int(input("Ingrese su rut(sin pintos ni digito verificador): "))
            if rut > 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! debe ingresar un rut valido(sin pintos ni digito verificador)")
        except:
            print("ERROR! debe ingresar un rut valido(sin pintos ni digito verificador)")

def validarNombre():
    while True:
        nombre = input("Escriba su nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! Debe ingresar un nombre valido")

def userOption():
    while True:
        try:
            userOption = int(input("Seleccione una opcion: "))
            if userOption in (1,2,3,4,5):
                return userOption
            else:
                print("ERROR! debe seleccionar una opcion valida")
        except:
            print("ERROR! debe seleccionar una opcion valida con un NUMERO")
            
def ValidarAsiento(p_str, p_num):
    while True:
        try: 
            dev = int(input(f"Ingrese la {p_str} que desea: "))
            if dev > 0 and dev <= p_num:
                return dev
            else:
                print(f"ERROR! debe ingrsar una cantidad de {p_str} valida")
        except:
                print(f"ERROR! debe ingrsar una cantidad de {p_str} valida")
lista_ruts = []
lista_nombres = []
lista_filas = []
lista_columnas = []
subtotal = 0
totalGanancias = 0

while True:
    menu()
    op = userOption()
    if op == 1:
        mostrarArreglo(array_invertido)
    elif op == 2:
        rut = uRur()
        if rut in lista_ruts:
            print("Usted ya a efectuado la compra, volvera al menu principal")
            continue
        nombre = validarNombre()
        mostrarArreglo(array_invertido)
        fila = ValidarAsiento("fila", 10)
        columna = ValidarAsiento("columna", 7)
        lista_nombres.append(nombre)
        lista_ruts.append(rut)
        posicion = lista_ruts.index(rut)
        lista_filas.append(fila)
        lista_columnas.append(columna)
        if fila >= 8 and fila <= 10:
            subtotal += 200000000
            totalPagar = solicitarPago(subtotal)
            totalGanancias += subtotal
        else:
            subtotal += 150000000
            totalPagar = solicitarPago(subtotal)
            totalGanancias += subtotal
        print(f"""

        Total ---------{totalPagar}
        IVA -----------{totalPagar * 0.19}
        Descuento ----- No tiene
        _____________________________
        
        """)
        array[fila-1][columna-1] = 1
    elif op == 3:
        rut = uRur()
        if rut not in lista_ruts:
            print("El cliente aun no compra ningun departamento")
            continue
        posicion = lista_ruts.index(rut)
        print(f"""
El señor {lista_nombres[posicion]} Tiene a su nombre
el departamento del piso {lista_filas[posicion]}, en la columna {lista_columnas[posicion]}.
        """)
    elif op == 4:
        print(f"""El total de las ventas de los departamentos del edificio "Martina" es {totalGanancias}""")
    else:
        break
print("Gracias por ocupar el sistema de ventas")
    
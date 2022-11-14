import random

MAX_Lineas = 3
MAX_Apuestas = 200
MIN_Apuestas = 1

FILAS = 3
COLUMNAS = 3

contador_simbolos = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
simbolos_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_victorias(columnas, lineas, apuesta, values):
    victorias = 0
    victorias_en_linea = []
    for linea in range(lineas):
        simbolo = columnas[0][linea]
        for columna in columnas:
            simbolo_to_check = columna[linea]
            if simbolo != simbolo_to_check:
                break
        else:
            victorias += values [simbolo]*apuesta
            victorias_en_linea.append(linea+1)
    
    return victorias, victorias_en_linea


def obtener_slot_machine_giro(filas,columnas,simbolos):
    todos_simbolos = []
    for simbolo, contador_simbolos in simbolos.items():
        for _ in range (contador_simbolos):
            todos_simbolos.append(simbolo)

    columnass = []
    for _ in range(columnas):
        columna = []
        actual_simbolos = todos_simbolos[:]
        for _ in range(filas):
            value = random.choice(actual_simbolos)
            actual_simbolos.remove(value)
            columna.append(value)

        columnass.append(columna)

    return columnass

def print_slot_machine(columnass):
    for fila in range(len(columnass[0])):
        for i,columna in enumerate (columnass):
            if i != len(columnass) -1:
                print(columna[fila],end=" | " )
            else:
                print(columna[fila],end="") 

        print()
    


def deposito():
    while True:
        monto = input("¿Cuanto le gustaria depositar? $")
        if monto.isdigit():
            monto = int(monto)
            if monto > 0:
                break
            else:
                print("La cantidad debe ser mayor a 0")
        else:
            print("Por favor ingrese un número")

    return monto

def  obtener_numero_lineas():
    while True:
            lineas = input("Ingrese el numero de lineas para apostar (1-" + str(MAX_Lineas)+ ")?")
            if lineas.isdigit():
                lineas = int(lineas)
                if 1 <= lineas <= MAX_Lineas:
                    break
                else:
                    print("Ingrese un número valido de lineas")
            else:
                print("Por favor ingrese un número")

    return lineas

def obtener_apuesta():
    while True:
        monto = input("¿Cuanto le gustaria apostar en cada linea? $")
        if monto.isdigit():
            monto = int(monto)
            if MIN_Apuestas <= monto <= MAX_Apuestas:
                break
            else:
                print(f"La cantidad debe ser mayor a ${MIN_Apuestas}-{MAX_Apuestas}.")
        else:
            print("Por favor ingrese un número")

    return monto
def giro(balance):
        lineas = obtener_numero_lineas()
        while True:
            apuesta = obtener_apuesta()
            total_apuesta = apuesta*lineas

            if total_apuesta > balance:
                print(
                    f"Tu no tienes suficientes recursos, tu actual balance es: ${balance} ")

            else:
                break        

        print(f"Tu estas apostando ${apuesta} en {lineas} lineas. el Total de la puesta es igual a: ${total_apuesta}")

        apuestas = obtener_slot_machine_giro(FILAS,COLUMNAS,contador_simbolos)
        print_slot_machine(apuestas)
        victorias, victorias_en_linea = check_victorias(apuestas,lineas,apuesta,simbolos_values)
        print(f"Tu ganaste ${victorias} !!!.")
        print(f"Tu ganaste en", *victorias_en_linea)
        return victorias - total_apuesta


def main():
    balance = deposito()
    while True:
        print(f"Su actual balance es ${balance}")
        respuesta = input("Presione play para girar  (q para salir).")
        if respuesta == "q":
            break
        balance += giro(balance) 
    
    print(f"Acabas de salir con ${balance}")

main()
import csv

#Leer empleados
with open("empleados.csv") as f: #guarda el archivo en variable f
    empleados = list(csv.DictReader(f, delimiter=";")) #crea diccionario

#Leer vacaciones
with open("vacaciones.csv") as f:
    vacaciones = list(csv.DictReader(f, delimiter=";"))

#Funcion para buscar empleado

def buscar_empleado(id_buscar, lista):
    for e in lista: #recorre los empleados
        if e["id_empleado"].strip() == id_buscar.strip(): #compara los id
            return e #si lo encuentra, lo devuelve
    return None

#Funcion calcular dias

def calcular_dias(antiguedad):
    antiguedad = int(antiguedad)
    if antiguedad <= 1:
        return 14
    elif antiguedad <= 3:
        return 21
    else:
        return 28
    
#Funcion guardar

def guardar(datos):
    with open("vacaciones.csv", "w", encoding="utf-8") as f:
        f.write("id_empleado;mes_inicio;dia_inicio;dia_fin;estado\n")
        for v in datos:
            linea = (
                v["id_empleado"] + ";" +
                v["mes_inicio"] + ";" +
                v["dia_inicio"] + ";" +
                v["dia_fin"] + ";" +
                v["estado"] + "\n" 
             )
            f.write(linea)
        


#Chatbot parte principal

print("Bienvenido a la gestion de vacaciones de Leimi!")
print("Soy ChatBot, ingresa tu ID para identificarte")

intentos_id = 0
max_intentos = 3

empleado = None

while intentos_id < max_intentos and empleado is None:
    id_emp = input("ID: ")
    empleado = buscar_empleado(id_emp, empleados) #busca el empleado en la lista

    if empleado is None:
        intentos_id += 1
        print("ID incorrecto. Intentos", intentos_id)

if empleado is None:
    print("Derivado a Recursos Humanos por multiples intentos de identificacion")
    print("NOTIFICACION RRHH: empleado no identificado tras tres intentos")
    break

else:
    print("Hola", empleado["nombre"])

    dias = calcular_dias(empleado["antiguedad"])
    print("Te corresponden", dias, "dias de vacaciones")

    mes = int(input("Ingrese el mes (1-12): "))
    dia_inicio = int(input("Ingrese el dia de inicio: "))

    dia_fin = dia_inicio + dias
    
    if dia_fin > 30:
        print("No se puede cruzar de mes")
    else:
        for v in vacaciones: #si esta todo ok se recorren todas las solicitudes
            if v["id_empleado"].strip() == id_emp.strip(): #busca la fila del empleado
                v["mes_inicio"] = str(mes)
                v["dia_inicio"] = str(dia_inicio)
                v["dia_fin"] = str(dia_fin)
                v["estado"] = "confirmado"   #actualiza la solicitud
        guardar(vacaciones)
        print("Vacaciones guardadas correctamente! ")


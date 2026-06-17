import csv

#Leer empleados
with open("empleados.csv") as f: #guarda el archivo en variable f
    empleados = list(csv.DictReader(f, delimiter=";")) #crea diccionario

#Leer vacaciones
with open("vacaciones.csv") as f:
    vacaciones = list(csv.DictReader(f, delimiter=";"))

#Funcion para buscar empleado

def buscar_empleado(id_buscar, lista):
    for e in lista:
        if e["id_empleado"] == id_buscar:
            return e
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
    with open("vacaciones.csv", "w", newline="") as f:
        campos = ["id_empleado","mes_inicio","dia_inicio","dia_fin","estado"]
        writer = csv.DictWriter(f, fieldnames=campos, delimiter=";")

        writer.writeheader()
        writer.writerows(datos)


#Chatbot parte principal

print("Bienvenido a la gestion de vacaciones de Leimi!")
print("Soy ChatBot, ingresa tu ID para identificarte")

id_emp = input("ID: ")

empleado = buscar_empleado(id_emp, empleados)

if empleado is None:
    print("Empleado no encontrado")
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
        for v in vacaciones:
            if v["id_empleado"] == id_emp:
                v["mes_inicio"] = str(mes)
                v["dia_inicio"] = str(dia_inicio)
                v["dia_fin"] = str(dia_fin)
                v["estado"] = "confirmado"
        guardar(vacaciones)
print("Vacaciones guardadas correctamente! ")


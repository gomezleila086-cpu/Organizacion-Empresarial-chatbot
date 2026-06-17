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

#Control de ID y fechas
intentos_id = 0
max_intentos = 3
empleado = None


while intentos_id < max_intentos and empleado is None:
    id_emp = input("Ingrese su ID: ")
    empleado = buscar_empleado(id_emp, empleados) #busca el empleado en la lista

    if empleado is None:
        intentos_id += 1
        print("ID incorrecto. Intentos", intentos_id)

if empleado is None:
    print("Derivado a Recursos Humanos por multiples intentos de identificacion")
    print("NOTIFICACION RRHH: empleado no identificado tras tres intentos")
    exit()

else:
    print("Hola", empleado["nombre"])

    dias = calcular_dias(empleado["antiguedad"])
    print("Te corresponden", dias, "dias de vacaciones")


#Control de fechas 
intentos_fecha = 0
max_intentos = 3
valido = False

while intentos_fecha < max_intentos and not valido:

    mes = int(input("Ingrese el mes (1-12): "))
    dia_inicio = int(input("Ingrese el dia de inicio: "))

    dia_fin = dia_inicio + dias
    
    if dia_fin > 30:
        intentos_fecha += 1
        print("Fecha no valida. No puede cruzar de mes")
        print("Intentos:", intentos_fecha)
    else:
        valido = True
    

#Derivacion a RRHH Si falla fecha
if not valido:
    print("Derivado a RRHH por intentos fallidos de fechas")
    print("NOTIFICACION RRHH: solicitud de vacaciones rechazada por errores de fecha")

#Guardar vacaciones 
for v in vacaciones:
    if v["id_empleado"].strip() == id_emp.strip():
        v["mes_inicio"] = str(mes)
        v["dia_inicio"] = str(dia_inicio)
        v["dia_fin"] = str(dia_fin)
        v["estado"] = "confirmado"

guardar(vacaciones)

print("Vacaciones guardadas correctamente!")

#Notificacion RRHH FINAL
print("NOTIFICACION RRHH: solicitud de vacaciones procesada")

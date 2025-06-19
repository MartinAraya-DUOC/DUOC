turistas = {
    "001": ["John Doe", "Estados Unidos", "12-01-2024"],
    "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
    "012": ["Julian Martinez", "Argentina", "19-09-2023"],
    "014": ["Agustin Morales", "Argentina", "28-03-2024"],
    "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
    "006": ["Maria Lopez", "Mexico", "08-12-2023"],
    "007": ["Joao Silva", "Brasil", "20-06-2024"],
    "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
    "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
    "008": ["Ana Santos", "Brasil", "03-10-2023"],
    "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
    "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
}

def turistas_por_pais(pais):
    lista = []
    for datos in turistas.values():
        if datos[1].lower() == pais.lower():
            lista.append(datos[0])
    if lista:
        print(lista)
    else:
        print("No hay turistas de ese pais.")

def turistas_por_mes(mes):
    total = len(turistas)
    contador = 0
    for datos in turistas.values():
        fecha = datos[2]
        mes_turista = int(fecha.split("-")[1])
        if mes_turista == mes:
            contador += 1
    porcentaje = round((contador / total) * 100, 1)
    return porcentaje

def eliminar_turista():
    nombre = input("Ingrese nombre del turista a eliminar: ").lower()
    for clave in list(turistas):
        if turistas[clave][0].lower() == nombre:
            del turistas[clave]
            print("Turista eliminado con exito.")
            return
    print("Turista no encontrado. No se pudo eliminar.")
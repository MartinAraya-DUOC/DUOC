import examenformativo4

def main():
    while True:
        print("\nMENU PRINCIPAL")
        print("1.- Turistas por pais.")
        print("2.- Turista por mes.")
        print("3.- Eliminar turista.")
        print("4.- Salir.")
        opcion = input("Ingrese opción: ")

        if opcion == "1":
            pais = input("Ingrese pais a buscar: ")
            examenformativo4.turistas_por_pais(pais)
        elif opcion == "2":
            mes = int(input("Ingrese mes a buscar: "))
            while mes < 1 or mes > 12:
                print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
                mes = int(input("Ingrese mes a buscar: "))
            porcentaje = examenformativo4.turistas_por_mes(mes)
            print(f"El número de turistas equivale al {porcentaje} % del total.")
        elif opcion == "3":
            examenformativo4.eliminar_turista()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")


# building a habit tracker


# definición de función que añadé hábitos a la lista
def add_habit(habits):
    habito = input("\nIngrese el \"hábito\" a añadir: ")

    if habito == "":
        print("Es necesario ingresar un hábito, inténtelo de nuevo")
    else:
        habits.append(habito)
        print("El \"hábito\" fue agregado con éxito\n")

# definición de función que muestra los hábitos
def show_habits(habits):
    if not habits:
        print("No hay hábitos registrados\n")
    else:
        print("\nHábitos registrados: ")
        for indice, habit in enumerate(habits, start=1):
            print(f"{indice}. {habit}")
    print()

# definición de función que elimina hábitos de la lista
def remove_habit(habits):

    if not habits:
        print("No hay hábitos para eliminar\n")
        return 
    
    show_habits(habits)
    option = int(input("Indique el índice del \"hábito\" a eliminar: "))
    
    if option > len(habits) or option <= 0:
        print("Índice inválido. Intente de nuevo")
        return
    
    habits.pop(option - 1)
    print("El \"hábito\" fue eliminado con éxito\n")

#==================================================================================

# definición función main
def main():
    
    habits = []

    while True:
        
        print("===== HABIT TRACKER =====")
        print("1. Agregar hábito") 
        print("2. Mostrar hábitos")
        print("3. Eliminar hábito")
        print("4. Salir")

        option = int(input("Selecciona una opción: "))

        if option == 1:
            add_habit(habits)
        elif option == 2:
            show_habits(habits)
        elif option == 3:
            remove_habit(habits)
        elif option == 4:
            break
        else:
            print("Opción incorrecta, inténtelo de nuevo")
main()
    

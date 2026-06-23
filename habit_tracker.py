import json 

# building a habit tracker

# definición de una función que guarda la lista de hábitos en un archivo json
def save_habits(habits):
    with open("habits.json", "w") as file:
        json.dump(habits, file)

# definición de una función que carga la lista de hábitos desde un archivo json
def load_habits():
    try:
        with open("habits.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []   

# definición de función que añadé hábitos a la lista
def add_habit(habits):
    habito = input("\nIngrese el \"hábito\" a añadir: ")

    if habito == "":
        print("Es necesario ingresar un hábito, inténtelo de nuevo")
    else:
        habits.append(habito)
        print("El \"hábito\" fue agregado con éxito\n")

        save_habits(habits)  # Guardar la lista de hábitos después de agregar uno nuevo

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

    try:
        option = int(input("Indique el índice del \"hábito\" a eliminar: "))
    except ValueError:
        print("Índice inválido. Intente de nuevo")
        return
    
    if option > len(habits) or option <= 0:
        print("Índice inválido. Intente de nuevo")
        return
    
    habits.pop(option - 1)
    print("El \"hábito\" fue eliminado con éxito\n")

    save_habits(habits)  # Guardar la lista de hábitos después de eliminar uno
#==================================================================================

# definición función main
def main():
    
    habits = load_habits()

    while True:
        
        print("===== HABIT TRACKER =====")
        print("1. Agregar hábito") 
        print("2. Mostrar hábitos")
        print("3. Eliminar hábito")
        print("4. Salir")

        try:
            option = int(input("Selecciona una opción: "))
        except ValueError:  
            print("Opción inválida, por favor ingrese un número")
            continue

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
    

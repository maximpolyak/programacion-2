from robot import RobotCocina;

def menu():
    robot = RobotCocina()
    while True:
        print("\nMenú de Robot de Cocina")
        print("1. Encender")
        print("2. Apagar")
        print("3. Programar función")
        print("4. Recetas")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            robot.encender()
        elif opcion == "2":
            robot.apagar()
        elif opcion == "3":
            programa = input("Ingrese el programa (triturar, batir, calentar, freír, amasar, autolimpieza): ")
            ingredientes = input("Ingrese los ingredientes separados por comas: ").split(",")
            robot.programar(programa, [i.strip() for i in ingredientes if i.strip()])
        elif opcion == "4":
            robot.mostrar_recetas()
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
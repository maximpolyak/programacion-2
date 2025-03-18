def menu(robot):
    while True:
        print("\nMenú Robot Cocina:")
        if robot.encendido:
            print("1. Encender (Ya está encendido)")
            print("2. Apagar")
            print("3. Programar función")
            print("4. Mostrar recetas disponibles")
            print("5. Cocinar receta")
        else:
            print("1. Encender")
            print("2. Apagar (Robot apagado)")
            print("3. Programar función (Encender primero)")
            print("4. Mostrar recetas disponibles (Encender primero)")
            print("5. Cocinar receta (Encender primero)")

        print("6. Salir")

        opcion = input("Seleccione opción: ")

        if opcion == "1":
            robot.encender()

        elif opcion == "2":
            robot.apagar()

        elif opcion in ["3", "4", "5"]:
            if not robot.encendido:
                print("⚠️  Debes encender primero el robot.")
                continue

            if opcion == "3":
                prog = input("Función (batir, bañar, calentar, freir, amasar): ")
                ingredientes = input("Ingredientes separados por comas: ").split(",")
                robot.programar(prog, [i.strip() for i in ingredientes])

            elif opcion == "4":
                robot.mostrar_recetas()

            elif opcion == "5":
                nombre_receta = input("Introduce el nombre de la receta a cocinar: ")
                robot.cocinar_receta(nombre_receta)

        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida.")
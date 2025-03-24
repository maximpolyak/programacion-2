def calculadora():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        operacion = input("Introduce la operación (+, -, *, /): ")

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero.")
            resultado = num1 / num2
        else:
            raise ValueError("Operación no válida. Debe ser +, -, * o /")

        print(f"Resultado: {resultado}")

    except ZeroDivisionError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Se ha producido un error inesperado:", type(e), "-", e)
    finally:
        print("Fin de la operación.")

calculadora()

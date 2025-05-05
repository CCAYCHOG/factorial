# Este programa calcula el factorial de un número entero no negativo ingresado por el usuario.
def factorial(numero):
    #Si el número es 0 o 1, el factorial es 1.
    if numero == 0 or numero == 1:
        return 1
    # Si el número es mayor que 1, se calcula el factorial de forma recursiva.
    else:
        return numero * factorial(numero - 1)

try: 
    while True:
        numero = int(input("Ingrese un número entero no negativo: "))
        if numero < 0:
            print("El número debe ser no negativo.")
        else:
            resultado = factorial(numero)
            print(f"El factorial de {numero} es: {resultado}")

except ValueError:
    print("Por favor, ingrese un número entero válido.")
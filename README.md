
# 📘 Programa para Calcular el Factorial de un Número

Este programa en Python permite calcular el **factorial de un número entero no negativo** ingresado por el usuario. Utiliza una función recursiva y validación de entrada para asegurar que el valor sea adecuado.

---

## 🔢 ¿Qué es el factorial?

El **factorial** de un número entero no negativo `n`, denotado como `n!`, es el producto de todos los enteros positivos desde `1` hasta `n`.

Por definición:
```
0! = 1
n! = n × (n - 1) × (n - 2) × ... × 2 × 1
```

---

## 🧠 Descripción del programa

- Solicita al usuario que ingrese un número entero no negativo.
- Si el número es `0` o `1`, retorna `1` como resultado.
- Si es mayor que `1`, calcula el factorial usando recursividad.
- Repite la solicitud indefinidamente hasta que el usuario detenga el programa manualmente.
- Maneja errores de entrada usando `try-except`.

---

## 💻 Código fuente

```python
# Este programa calcula el factorial de un número entero no negativo ingresado por el usuario.
def factorial(numero):
    # Si el número es 0 o 1, el factorial es 1.
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
```

---

## ▶️ Ejemplo de uso

```
Ingrese un número entero no negativo: 5
El factorial de 5 es: 120
```

---

## ✅ Requisitos

- Python 3.x instalado.

---

## 📌 Autor

**Julio César Caycho García**  
📧 ing@cesarcaycho.com  
📍 Chilca, Perú

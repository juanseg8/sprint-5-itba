try:
    numero = int(input("Ingrese un numero: "))
    resultado= 10/numero 
    print("El resultado es: ", resultado)
except ValueError:
    print("Error: Ingrese un numero valido")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")

try:
    numero2 = int(input("Ingrese un numero: "))
    resultado= 10/numero 
    
except ValueError:
    print("Error: Ingrese otro numero valido")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
else:
    print("El resultado es: ", resultado)
finally:
    print("Termino")

def dividir(a,b):
    if b==0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a/b

try:
    resultado = dividir(10,2)
    print(resultado)
except ZeroDivisionError as e:
    print("Error:", str(e))


numero1 = input("ingrese un numero ")
numero1 = int(numero1)
numero2 = input ("ingrese un segundo numero ")
numero2 = int(numero2)
opcionCalculo = input("ingrese si desea restar(-) o sumar(+) esos numeros ")
if opcionCalculo == "+":
    r = numero1 + numero2
elif opcionCalculo == "-":
    r = numero1 - numero2
else:
    print("no toco ninguna dee las opciones")
print("su resultado es ", r)


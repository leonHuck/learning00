# Calcular el sueldo a cobrar teniendo en cuenta que  los empleados que no han faltado y  cuya antigüedad es superior
# a 5 años, tienen un adicional del 30% sobre el sueldo básico ($47.000). Pedir la cantidad de días no 
# trabajados y año de ingreso en la empresa.
nombre = input("ingrese su nombre ")
year = int(input("Ingrese hace cuantos años trabaja dentro de la empresa "))
noTrabajo = int(input("explicite cuantos dias falto este mes de trabajo "))
sueldo = 47_000
adicionalSueldo = sueldo * 1.30 
if year >= 5 and noTrabajo == 0:
    print(nombre, "su pago por este mes de trabajo es de ",adicionalSueldo)
else:
    print(nombre, "el pago por su mes de trabaj0 es de ",sueldo)


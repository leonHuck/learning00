nombre = str(input("Ingrese su nombre completo "))
carrera = int(input("Indique la carrera a la que desea inscribirse: Electromecánica (1), Turismo (2), Desarrollo de Software (3)" ))
ciudad = int(input("¿Vive usted en rio cuarto? SI(1) NO(2)" ))
cuota = 7000
cuota = int(cuota)

if carrera == 1 and ciudad == 2:
    descuento = cuota - cuota * 0.15
    print(nombre , "usted debe pagar $", descuento,)
else:
    print(nombre, "debe pagar $",cuota,)

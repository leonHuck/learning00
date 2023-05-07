# El costo del pasaje a Córdoba es de $2000. La empresa realiza un descuento de un 40 % sobre el costo 
# del boleto a los niños que tienen entre 5 y 10 años y a los jubilados\
# mayores de 65). Pedir nombre y edad y mostrar el nombre y el valor final del pasaje.
nombre = str(input('ingrese su nombre completo '))
edad = int(input("ingrese su edad "))
valorBoleto = 2_000 
descuento = valorBoleto - valorBoleto * 0.40 
if  edad >= 5 and edad <=10 or edad >=65 :
    print(nombre, 'usted debe abonar ',descuento)
else:
    print(nombre, 'usted debe abonar', valorBoleto)

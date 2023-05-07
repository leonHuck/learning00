totalSegundos = int(input("ingrese los segundos que desea calcular "))


segXdia = 24 * 60 * 60
dias = totalSegundos // segXdia
resto = totalSegundos - (dias * segXdia)
segXhora = 60 * 60
horas = resto // segXhora
resto = resto - (horas * segXhora )
segXmin = 60
minutos = resto // segXmin 
segundos = resto - (minutos * segXmin )

print(totalSegundos, 'segundos equivalen a', dias, "dias", horas,"horas", minutos,"minutos", segundos,"segundos.")



import math
import random
import itertools

def comb(n,r):
    'calcula el numero combinatorio de N tomados de R'
    return math.factorial(n) / (math.factorial(n-r) * math.factorial(r))

nro_cartones = int(input("Ingrese el nro de cartones aprox.: "))
nros_serie = 15
cont = 0
cartones = list()

while cont < nro_cartones:
    cont+=1
    #elegimos los numeros que pertencen a la serie
    numeros = random.sample(range(0,100),nros_serie)
    list.sort(numeros)

    #armamos los cartones de la serie
    cartones.append(numeros)
    print(numeros)

list.sort(cartones)
print(cartones)

sorteos = 0
conts = 0

sorteos = int(input("Ingrese sorteos: "))

while conts < sorteos:
	winners = list()
	cont = 0
	len1 = len(cartones)

	while cont < len1:
		cont += 1
		winners.append(0)

	# print(winners)
	
	conts += 1
	
	print("SORTEO NRO " + str(conts))
	
	list_sorteo = list()
	list2 = list()
	cont = 0
	correcto = 0
	win = 0

	while win == 0:
	
		if list_sorteo == []:
			nro_cartones = int(input("Ingrese el numero sorteado: "))
			while nro_cartones > 99 or nro_cartones < 0:
				nro_cartones = int(input("Solo de 0 a 99, cargue uno nuevo a continuacion: "))
						
		
		else:
			nro_cartones = int(input("Ingrese el numero sorteado: "))
			while correcto == 0: 
				while nro_cartones > 99 or nro_cartones < 0:
					nro_cartones = int(input("Solo Numeros de 0 a 99, cargue nuevamente a continuacion: "))
				
				if list_sorteo.count(nro_cartones) == 1:
					nro_cartones = int(input("El Numero ya fue sorteado!! Revise e ingrese nuevamente"))
					correcto = 0
					continue
					
				correcto = 1
					
		list_sorteo.append(nro_cartones)
		print(len(list_sorteo))	
		
		correcto = 0
		
		while cont < len1: 
		
			list2 = cartones[cont]
		#print(list2)
		
			if list2.count(nro_cartones) == 1:
				winners[cont]+=1
			
			cont += 1
			del list2
			list2 = list()
	
		cont = 0
	
		if winners.count(15)>0:
			win = 1
			print(winners.index(15))

	print("El ganador es .... ")

	print(cartones[winners.index(15)])
	
	print("GANOOOOOOOOOO ")
	print("GANOOOOOOOOOO ")	
	print("GANOOOOOOOOOO ")	
	print("GANOOOOOOOOOO ")
	
	
	list.sort(winners)
	print(winners)
	
	del winners
	del list_sorteo

print("GRACIAS POR PARTICIPAR")

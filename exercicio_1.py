numero = int (input ("Digite um número: "))

fatorial = 1

for i in range (1, numero + 1):
    fatorial = fatorial * i


print (f"O fatorial de {numero} é {fatorial}") 

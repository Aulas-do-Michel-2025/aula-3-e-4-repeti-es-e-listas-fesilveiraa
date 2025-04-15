lista = [*map(int, input("Digite a sua lista (separando os números por vírgula): ").split(","))] 
 
nova_lista = []

for numero in lista:
    if numero % 2 != 0:
        nova_lista.append (numero)

print (f"Os números ímpares são: {nova_lista} ") 

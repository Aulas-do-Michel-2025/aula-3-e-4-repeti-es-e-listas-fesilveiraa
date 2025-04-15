primeira_lista = [*map(int, input("Digite a sua primeira lista (separando os números por vírgula): ").split(","))]
segunda_lista = [*map(int, input("Digite a sua segunda lista (separando os números por vírgula): ").split(","))]


max_primeira_lista = max (primeira_lista)
max_segunda_lista = max (segunda_lista)

if max_primeira_lista > max_segunda_lista:
    print ("Primeira")
elif max_segunda_lista > max_primeira_lista:
    print ("Segunda")
elif max_primeira_lista == max_segunda_lista:
    print ("Ambas") 

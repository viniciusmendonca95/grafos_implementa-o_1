# Função de tratamento de erro do menu
def tratarMenu(msg):
    try:
        opcao = int(input(msg))
        if opcao > 0 and opcao <= 9:
            return opcao
        else:
            print("Informação invalida, digite uma opção entre 1 e 9")
            return tratarMenu(msg)
    except:
        print("Informação invalida, digite uma opção entre 1 e 9")
        return tratarMenu(msg)


# Função de tratamento de erro do menu de Dijkstra
def tratarDijkstra(msg2):
    try:
        opcao2 = int(input(msg2))
        if opcao2 > 0 and opcao2 <= 3:
            return opcao2
        else:
            print("Informação invalida, digite uma opção entre 1 e 3")
            return tratarDijkstra(msg2)
    except:
        print("Informação invalida, digite uma opção entre 1 e 3")
        return tratarDijkstra(msg2)
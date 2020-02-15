import util as ut
import erros as e

#Função para gerar o menu principal
def menuPrincipal():
    print("===== IMPLEMENTAÇÃO GRAFOS =====")
    print("1- Representação do grafo")
    print("2- Método getAdjacentes")
    print("3- Método ehRegular")
    print("4- Método ehCompleto")
    print("5- Método ehConexo")
    print("6- Método do algoritimo do menor caminho (Dijkstra)")
    print("7- Finalizar o programa")
    print()

    while True:
        msg = "Informe uma opção: "
        op = e.tratarMenu(msg)
        if op == 1:
            grafo = ut.lerGrafo()
            print(f"Representação do grafo com seus adjacentes e pesos de arestas:\n{grafo}")
            print()
        if op == 2:
            print("Está opção ainda será implementada")
            print()
        if op == 3:
            print("Está opção ainda será implementada")
            print()
        if op == 4:
            print("Está opção ainda será implementada")
            print()
        if op == 5:
            print("Está opção ainda será implementada")
            print()
        if op == 6:
            print("Está opção ainda será implementada")
            print()
        if op == 7:
            print()
            print("FINALIZANDO")
            break

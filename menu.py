import util as ut
import erros as e
import metodos as met

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
            print(f"Representação do grafo dos seus vértices com seus adjacentes e pesos de arestas:\n{grafo}")
            print()
        if op == 2:
            grafo = ut.lerGrafo()
            vertice = input("Informe o vértice: ").upper()
            if vertice not in grafo:
                print("Vértice não encontrado no grafo")
            else:
                adjacentes = met.getAdjacentes(vertice)
                print(f"Os adjacentes ao vértice {vertice}: {adjacentes}")
            print()
        if op == 3:
            print(f"Verificação se o grafo é regular: {met.ehRegular()}")
            print()
        if op == 4:
            print(f"Verificação se o grafo é completo: {met.ehCompleto()}")
            print()
        if op == 5:
            grafo = ut.lerGrafo()
            raiz = input("Informe o vértice raiz: ").upper()
            if raiz not in grafo:
                print("Vértice não encontrado no grafo")
            else:
                print(f"Verificação se o grafo é conexo: {met.ehConexo(raiz)}")
            print()
        if op == 6:
            print("Está opção ainda será implementada")
            print()
        if op == 7:
            print()
            print("FINALIZANDO")
            break

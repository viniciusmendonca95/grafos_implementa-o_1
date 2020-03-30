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
            while True:
                grafo = ut.lerGrafo()
                print()
                print("1- Menor caminho  de um vértice para todos os outros e o caminho")
                print("2- Menor caminho entre dois vértices e o caminho")
                print("3- Voltar ao menu")
                print()
                msg2 = "Informe uma opção de Dijkstra: "
                op2 = e.tratarDijkstra(msg2)
                if op2 == 1:
                    vert = input("Informe o vértice raiz: ").upper()
                    if vert not in grafo:
                        print()
                        print("Vértice não encontrado no grafo")
                        print()
                    else:
                        print()
                        met.Djikstra1(vert)
                        break
                elif op2 == 2:
                    vert = input("Informe o 1º vértice: ").upper()
                    if vert not in grafo:
                        print()
                        print("Vértice não encontrado no grafo")
                        print()
                    else:
                        vert2 = input("Informe o 2º vértice: ").upper()
                        if vert2 not in grafo:
                            print()
                            print("Vértice não encontrado no grafo")
                            print()
                        else:
                            print()
                            met.Djikstra2(vert, vert2)
                            break
                elif op2 == 3:
                    print("===== IMPLEMENTAÇÃO GRAFOS =====")
                    print("1- Representação do grafo")
                    print("2- Método getAdjacentes")
                    print("3- Método ehRegular")
                    print("4- Método ehCompleto")
                    print("5- Método ehConexo")
                    print("6- Método do algoritimo do menor caminho (Dijkstra)")
                    print("7- Finalizar o programa")
                    print()
                    break
            print()
        if op == 7:
            print()
            print("FINALIZANDO")
            break

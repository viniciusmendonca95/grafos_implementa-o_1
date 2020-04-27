import util as ut

#Retorna os vértices adjacentes de um vértice passado por parâmetro
def getAdjacentes(vertice):
    grafo = ut.lerGrafo()
    listaAdj = []
    for x in range(0, len(grafo[vertice])):
        aux = list(grafo[vertice][x].keys())
        listaAdj.append(aux[0])
    return listaAdj


#Retorna True se o grafo for regular e false se não for
def ehRegular():
    grafo = ut.lerGrafo()
    qntdAdj = []
    for x in grafo:
        qntdAdj.append(len(grafo[x]))
    for x in range(0, len(qntdAdj)-1):
        if qntdAdj[x] != qntdAdj[x+1]:
            regular = False
            return regular
        else:
            regular = True
    return regular


#Retorna True se o grafo for completo e false se não for
def ehCompleto():
    grafo = ut.lerGrafo()
    vertices = []
    for x in grafo:
        vertices.append(x)
    for x in grafo:
        if len(grafo[x]) != len(vertices) -1:
            completo = False
            return completo
        else:
            completo = True
    return completo


#Retorna uma lista de vetores visitados por uma busca em largura após passado um vetor inicial (raiz) por parâmetro
def buscaLargura(raiz):
    fila = []
    vetMarcados = []
    vetMarcados.append(raiz)
    fila.append(raiz)
    while (len(fila) > 0):
        vert1 = fila[0]
        listaAdj = getAdjacentes(vert1)
        for i in listaAdj:
            if (i not in vetMarcados):
                vetMarcados.append(i)
                fila.append(i)
        fila.pop(0)
    return vetMarcados


#Retorna true se o grafo for conexo e false se o grafo for desconexo
def ehConexo(raiz):
    grafo = ut.lerGrafo()
    vetMarcados = buscaLargura(raiz)
    if len(vetMarcados) != len(grafo):
        return False
    else:
        return True


#Algoritimo de Djikstra que retorna os menor caminho entre um vértice passado por parâmetro e todos os vértices do grafo
def Djikstra1 (vert):
    grafo = ut.lerGrafo()
    raiz = vert
    vertices = []
    s = []
    dist = []
    path1 = []
    path2 = []
    caminho = []
    
    # Adiciona os vértices do grafo em uma lista
    for x in grafo:
        vertices.append(x)

    # Adiciona valores a lista S
    for k in range(0, len(grafo)-1):
        s.insert(k, "não")
    s.insert(vertices.index(vert), "sim")

    # Adiciona valores a lista dist
    for z in range(0, len(grafo)-1):
        dist.insert(z, float("inf"))
    dist.insert(vertices.index(vert), 0)

    # Adiciona valores a lista path
    for y in range(0, len(grafo)):
        if y == vertices.index(vert):
            path1.append("-")
            path2.append("-")
        else:
            path1.append(0)
            path2.append(0)

    # Pega os adjacentes e calcula os caminhos
    while s.count("não") != 0:
        for x in range(0, len(grafo[vert])):
            a = list(grafo[vert][x].keys())
            peso = list(grafo[vert][x].values())
            z = vertices.index(a[0])
            t = vertices.index(vert)

            if dist[z] > dist[t] + peso[0]:
                dist[z] = dist[t] + peso[0]
                path1[z] = t

        listaMenor = []

        #Lista os caminhos em busca do menor caminho
        for k in range(0, len(grafo)):
            if s[k] != "sim":
                listaMenor.append(dist[k])

        #Adiciona "sim" a lista S quando for o menor caminho
        for j in range(0, len(grafo)):
            if s[j] != "sim" and dist[j] == min(listaMenor):
                vert = vertices[j]
                s[j] = "sim"

        #Pega os valores de path1 e transforma em vértices no path2
        for p in range(0, len(path1)):
            if path2[p] == "-":
                path2[p] = "-"
            else:
                path2[p] = vertices[path1[p]]

    # Faz a sequência e printa o menor caminho de um vértice a todos os outros vértices do grafo
    for l in range(0, len(grafo)):
        vertFinal = vertices[l]
        caminho.append(vertFinal)
        while "-" not in caminho:
            caminho.append(path2[vertices.index(vertFinal)])
            vertFinal = path2[vertices.index(vertFinal)]
        caminho.pop(-1)
        caminho.reverse()

        print(f"Distância minima de {raiz} para {vertices[l]}: {dist[l]}      O caminho: {caminho}")
        caminho = []
        

#Algoritimo de Djikstra que retorna os menor caminho entre dois vértices passados por parâmetro
def Djikstra2(vert, vert2):
    grafo = ut.lerGrafo()
    raiz = vert
    vertices = []
    s = []
    dist = []
    path1 = []
    path2 = []
    caminho = []

    # Adiciona os vértices do grafo em uma lista
    for x in grafo:
        vertices.append(x)

    # Adiciona valores a lista S
    for k in range(0, len(grafo) - 1):
        s.insert(k, "não")
    s.insert(vertices.index(vert), "sim")

    # Adiciona valores a lista dist
    for z in range(0, len(grafo) - 1):
        dist.insert(z, float("inf"))
    dist.insert(vertices.index(vert), 0)

    # Adiciona valores a lista path
    for y in range(0, len(grafo)):
        if y == vertices.index(vert):
            path1.append("-")
            path2.append("-")
        else:
            path1.append(0)
            path2.append(0)

    # Pega os adjacentes e calcula os caminhos
    while s[vertices.index(vert2)] != "sim":
        for x in range(0, len(grafo[vert])):
            a = list(grafo[vert][x].keys())
            peso = list(grafo[vert][x].values())
            z = vertices.index(a[0])
            t = vertices.index(vert)

            if dist[z] > dist[t] + peso[0]:
                dist[z] = dist[t] + peso[0]
                path1[z] = t

        listaMenor = []

        #Lista os caminhos em busca do menor caminho
        for k in range(0, len(grafo)):
            if s[k] != "sim":
                listaMenor.append(dist[k])

        #Adiciona "sim" a lista S quando for o menor caminho
        for j in range(0, len(grafo)):
            if s[j] != "sim" and dist[j] == min(listaMenor):
                vert = vertices[j]
                s[j] = "sim"

         #Pega os valores de path1 e transforma em vértices no path2
        for p in range(0, len(path1)):
            if path2[p] == "-":
                path2[p] = "-"
            else:
                path2[p] = vertices[path1[p]]

    #Faz a sequência do menor caminho
    vertFinal = vert2
    caminho.append(vertFinal)
    while "-" not in caminho:
        caminho.append(path2[vertices.index(vertFinal)])
        vertFinal = path2[vertices.index(vertFinal)]
    caminho.pop(-1)
    caminho.reverse()

    # Printa o menor caminho de um vértice a outro vértice
    print(f"Distância minima de {raiz} para {vert2}: {dist[vertices.index(vert2)]}     O caminho: {caminho}")


def ordenacaoTopologica():
    #declaração de variaveis
    grafo = ut.lerGrafo()
    grauEntrada = []
    listaOrdenada = []
    listAdj = []
    vert = list(grafo.keys())
    values = list(grafo.values())

    while True:
        #criação da lista com todos os adjacentes
        for x in range(0, len(values)):
            for y in range(0, len(values[x])):
                listAdj.append(list(values[x][y])[0])

        #criação da lista com o valor do grau de entrada dos vértices
        for x in range(0, len(grafo)):
            grauEntrada.append(listAdj.count(list(grafo.keys())[x]))

        #criação da lista de ordenação topológica
        for x in range(0,len(grauEntrada)):
            if grauEntrada[x] == 0 and vert[x] not in listaOrdenada:
                listaOrdenada.append(vert[x])
                values[x] = list(["Vazio"])
                grauEntrada[x] = None

        #limpeza das listas
        grauEntrada.clear()
        listAdj.clear()

        #condição de parada e impressão dos valores
        if len(listaOrdenada) == len(vert):
            return listaOrdenada
            break

        
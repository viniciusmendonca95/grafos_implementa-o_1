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

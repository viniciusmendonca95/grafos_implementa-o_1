import json

#Função para ler o grafo
def lerGrafo():
    with open("grafo.json") as grf:
        arq = json.load(grf)
        vertices = arq["vertices"]
        dic = {}
        for v in vertices:
            dic[v] = arq[v]
        return dic


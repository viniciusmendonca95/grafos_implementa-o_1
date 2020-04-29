# Implementação grafos
Implementação do algoritmo de grafos para matéria Teoria dos Grafos ministrada pelo professor Adolfo Guimarães na Universidade Tiradentes - UNIT

Alunos: Vinícius Mendonça e Leonardo Teles

## Inicialização
  
Para a inicialização do algoritimo, é necessário configurar um arquivo "grafo.json" demonstrado no tópico abaixo. Após a configuração, execute o arquivo "main.py"

## Configuração do arquivo grafo.json
  
O arquivo "grafo.json" será configurado informando seus vértices, dentro dos seus vértices uma listas com objetos que contém seus adjacentes e seus respectivos pesos.
  
Exemplo da representação de grafos com seu .json que podem ser utilizados para testes no algoritmo:

<b>Grafo valorado:</b>

![Grafo valorado](https://i.imgur.com/dh3NqNV.jpg)

```
{
    "vertices" : [ "T", "U", "X", "V", "Y"],
    "T": [{"U":10}, {"X": 5}],
    "U": [{"X":2}, {"V": 1}],
    "X": [{"U":3}, {"V": 9}, {"Y": 2}],
    "V": [{"Y":4}],
    "Y": [{"V":6}, {"T": 7}]
}


```

<b>Grafo direcionado:</b>

![Grafo direcionado](https://i.imgur.com/qQ7bwjc.jpg)

```
{
    "vertices" : [ "A", "B", "C", "D", "E", "F", "G", "H"],
    "A": [{"C":0}, {"D": 0}],
    "B": [{"D":0}, {"G": 0}],
    "C": [{"E":0}, {"F": 0}],
    "D": [{"F":0}],
    "E": [],
    "F": [{"H":0}],
    "G": [{"H":0}],
    "H": []
}


```

<b>Grafo desconexo:</b>

![Grafo desconexo](https://i.imgur.com/R8VcGNL.jpg)

```
{
    "vertices" : [ "A", "B", "C", "D", "E", "F"],
    "A": [{"B":0}, {"D": 0}],
    "B": [{"A":0}, {"C": 0}],
    "C": [{"B":0}],
    "D": [{"A":0}],
    "E": [{"F":6}],
    "F": [{"E":6}]
}


```

<b>Grafo completo:</b>

![Grafo completo](https://i.imgur.com/sIcHkDf.jpg)

```
{
    "vertices" : [ "A", "B", "C", "D"],
    "A": [{"B":0}, {"C": 0},  {"D": 0}],
    "B": [{"A":0}, {"C": 0},  {"D": 0}],
    "C": [{"A":0}, {"B": 0},  {"D": 0}],
    "D": [{"A":0}, {"B": 0},  {"C": 0}],
}


```

<b>Grafo regular:</b>

![Grafo regular](https://i.imgur.com/zYIc1fj.jpg)

```
{
    "vertices" : [ "A", "B", "C", "D", "E", "F"],
    "A": [{"B":0}, {"C": 0}],
    "B": [{"A":0}, {"D": 0}],
    "C": [{"A":0}, {"E": 0}],
    "D": [{"B":0}, {"F": 0}],
    "E": [{"C":0}, {"F": 0}],
    "F": [{"E":0}, {"D": 0}]
}


```

<b>Grafo colorido:</b>

![Grafo colorido](https://i.imgur.com/KFw9a7i.jpg)

```
{
    "vertices" : [ "A", "B", "C", "D", "E", "F", "G"],
    "A": [{"B":0}, {"D": 0}],
    "B": [{"A":0}, {"C": 0}, {"D": 0}, {"E": 0}, {"F": 0}],
    "C": [{"B":0}, {"F": 0}],
    "D": [{"A":0}, {"B":0}, {"E":0}, {"G":0}],
    "E": [{"B":0}, {"D": 0}, {"F": 0}, {"G": 0}],
    "F": [{"B":0}, {"C":0}, {"E":0}, {"G":0}],
    "G": [{"D":0}, {"E":0}, {"F":0}]

}


```




## Métodos

Os seguintes métodos básicos foram implementados: 

  * <p><b>Representação do grafo:</b> Através de uma lista de adjacentes, configurada no "grafo.json", retorna um dicionário contendo todo o grafo, seus vértices, seus respectivos adjacentes e pesos.</p>
  * <p><b>getAdjacentes:</b> Retorna a lista de adjacentes de um vértice passado como parâmetro.</p>
  * <p><b>ehRegular:</b> Verifica se um determinado grafo é regular ou não. Retorna True ou False a depender do grafo.</p>
  * <p><b>ehCompleto:</b> Verifica se um determinado grafo é completo ou não. Retorna True ou False a depender do grafo.</p> 
  * <p><b>ehConexo:</b> Verifica se um determinado grafo é conexo ou não. Retorna True ou False a depender do grafo. Utiliza o algoritimo de busca em largura.</p>

<p><b>Algoritmo de Ordenação Topológica:</b> 

  * <p>Retorna a ordenação topológica do grafo.</p>


<p><b>Algoritmo de Coloração:</b> 

  * <p>Retorna a um valor referente a uma cor de um vértice.</p>


Duas versões do algoritmo de Dijkstra foram implementados:

<p><b>Algoritmo de Menor Caminho (Dijkstra):</b> 
  
  * <p>A primeira versão recebe como parâmetro um vértice e o algoritmo retorna o menor caminho deste para todos os demais vértices.</p>
  * <p>A segunda versão recebe como parâmetro dois vértices e o algoritmo retorna o menor caminho somente entre estes dois vértices.</p>
  

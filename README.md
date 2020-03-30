# Implementação grafos
Implementação do algoritmo de grafos para matéria Teoria dos Grafos ministrada pelo professor Adolfo Guimarães na Universidade Tiradentes - UNIT

Alunos: Vinícius Mendonça e Leonardo Teles

## Inicialização
  
Para a inicialização do algoritimo, é necessário configurar um arquivo "grafo.json" demonstrado no tópico abaixo. Após a configuração, execute o arquivo "main.py"

## Configuração do arquivo grafo.json
  
O arquivo "grafo.json" será configurado informando seus vértices, dentro dos seus vértices uma listas com objetos que contém seus adjacentes e seus respectivos pesos.
  
Exemplo da representação de um grafo com seu .json:

![Exemplo do grafo](https://i.imgur.com/dh3NqNV.jpg)

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

## Métodos

Os seguintes métodos básicos foram implementados: 

  * <p><b>Representação do grafo:</b> Através de uma lista de adjacentes, configurada no "grafo.json", retorna um dicionário contendo todo o grafo, seus vértices, seus respectivos adjacentes e pesos.</p>
  * <p><b>getAdjacentes:</b> Retorna a lista de adjacentes de um vértice passado como parâmetro.</p>
  * <p><b>ehRegular:</b> Verifica se um determinado grafo é regular ou não. Retorna True ou False a depender do grafo.</p>
  * <p><b>ehCompleto:</b> Verifica se um determinado grafo é completo ou não. Retorna True ou False a depender do grafo.</p> 
  * <p><b>ehConexo:</b> Verifica se um determinado grafo é conexo ou não. Retorna True ou False a depender do grafo. Utiliza o algoritimo de busca em largura.</p>
 
Duas versões do algoritmo de Dijkstra foram implementados:

<p><b>Algoritmo de Menor Caminho (Dijkstra):</b> 
  
  * <p>A primeira versão recebe como parâmetro um vértice e o algoritmo retorna o menor caminho deste para todos os demais vértices.</p>
  * <p>A segunda versão recebe como parâmetro dois vértices e o algoritmo retorna o menor caminho somente entre estes dois vértices.</p>
  

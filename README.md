# Implementação grafos
Implementação do algoritmo para matéria Teoria dos Grafos 
Alunos: Vinícius Mendonça e Leonardo Teles

## Inicialização
  
Para a inicialização do algoritimo, é necessário configurar um arquivo "grafo.json" demonstrado no tópico abaixo. Após a configuração, execute o arquivo "main.py"

## Configuração do arquivo grafo.json
  
O arquivo "grafo.json" será configurado informando seus vértices, dentro dos seus vértices uma listas com objetos que contém seus adjacentes e seus respectivos pesos.
  
Exemplo da representação de um grafo com seu .json:

![Exemplo do grafo](https://i.imgur.com/ennmXs1.png)

```
{
    "vertices" : [ "A", "B", "C", "D", "E", "F", "G", "H"],
    "A": [{"B":1}, {"C": 2}],
    "B": [{"A":1}, {"D": 2}, {"E": 3}],
    "C": [{"A":1}, {"D": 2}],
    "D": [{"B":1}, {"C": 2}, {"E": 3}, {"F": 4}],
    "E": [{"B":1}, {"D": 2}],
    "F": [{"D":1}, {"G": 2}, {"H": 3}],
    "G": [{"F":1}, {"H": 2}],
    "H": [{"F":1}, {"G": 2}]
}

```

## Métodos

Os seguintes métodos básicos foram implementados: 

  * <p><b>Representação do grafo:</b> Através de uma lista de adjacentes, configurada no "grafo.json", retorna um dicionário contendo todo o grafo, seus vértices, seus respectivos adjacentes e pesos.</p>
  
Os seguintes métodos básicos serão ser implementados: 

  * <p><b>getAdjacentes:</b> Retorna a lista de adjacentes de um vértice passado como parâmetro.</p>
  * <p><b>ehRegular:</b> Verifica se um determinado grafo é regular ou não. Retorna True ou False a depender do grafo.</p>
  * <p><b>ehCompleto:</b> Verifica se um determinado grafo é completo ou não. Retorna True ou False a depender do grafo.</p> 
  * <p><b>ehConexo:</b> Verifica se um determinado grafo é conexo ou não. Retorna True ou False a depender do grafo. Utiliza o algoritimo de busca em largura.</p>
  
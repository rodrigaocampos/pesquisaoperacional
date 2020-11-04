
grafo = {}
linhas = None

try:
    arquivo = open("arquivo.txt")
    linhas = arquivo.readlines()
except Exception:
    arquivo.close()


lista = linhas[0].split(",")
vertices = []
for i in lista:
    vertices.append(int(i))


lista = linhas[1].split(",")
arestas = []
for i in lista:
    arestas.append(int(i))


for i in vertices:
    grafo[i] = []


grafo[0] = [arestas[1], arestas[3], arestas[7]]
grafo[1] = [arestas[2], arestas[3], arestas[5], arestas[8]]
grafo[2] = [arestas[0], arestas[6]]
grafo[3] = [arestas[4], arestas[5], arestas[6]]
grafo[4] = [arestas[0], arestas[7], arestas[8]]
grafo[5] = [arestas[1], arestas[2], arestas[4]]

print("Grafo: ")
print(grafo)

print("\nMatriz adjacente\n")

matriz = []

def adjacente(v1, v2):
    for i in v1:
        for j in v2:
            if i == j:
                return 1
    return 0

for i in grafo:
    linha = []
    for j in grafo:
        if i != j:
            linha.append(adjacente(grafo[i], grafo[j]))
    matriz.append(linha)



for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(str(matriz[i][j]) + "\t", end="")
    print()

print("\n")

for i in grafo:
    print(f"vertice {i}: grau {len(grafo[i])}")


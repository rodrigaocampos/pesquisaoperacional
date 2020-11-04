matriz1 = []
matriz2 = []

with open("meu_arquivo.txt") as arquivo:
	for linha in arquivo:
		dados = linha.split("\t") # linha em string
		conversao = list(map(int, dados)) # converte a linha em uma lista de inteiros

		matriz1.append(conversao)

with open("meu_arquivo2.txt") as arquivo:
	for linha in arquivo:
		dados = linha.split("\t") # linha em string
		conversao = list(map(int, dados)) # converte a linha em uma lista de inteiros

		matriz2.append(conversao)

matriz_soma = []

for i in range(10):
	linha = []
	for j in range(10):
		linha.append(matriz1[i][j] * matriz2[i][j]) #multiplica matrizes

	matriz_soma.append(linha)

print(matriz_soma)



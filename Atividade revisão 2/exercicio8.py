
meu_vetor = [] 
for i in range(10): 
	numero = input(" Informe um número: ")
	meu_vetor.append(int(numero)) 


def soma_vetor(meu_vetor):
    if len(meu_vetor) == 1:
        return meu_vetor[0]
    else:
        return meu_vetor[0] + soma_vetor(meu_vetor[1:]) 
   

print(soma_vetor(meu_vetor))


#recebe um vetor de inteiros por parametro
def bubbleSort(v):
        for i in range(len(v)):
            for atual in range(len(v)-1): #realiza for encadeado e compara elemento n com todos os outros do vetor
                if(v[atual]>v[atual+1]):#compara se o elemento da posição atual é maior que o próximo
                    v[atual],v[atual+1]=v[atual+1],v[atual]#realiza a troca

        return v #retorna vetor ordenado            

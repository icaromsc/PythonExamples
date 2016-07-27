#cria objeto node que vai encapsular referencia para o filho da direita,esquerda e o valor dentro do Nó
class Node(object):
    def __init__(self,dado):
            self.dado=dado
            self.direita=None
            self.esquerda=None


class ArvoreBinaria(object):
    
    def __init__(self,dado): #ao instanciar objeto ArvoreBinaria chama método construtor
        self.raiz=Node(dado) 

        
    def inserir(self,raiz,item):
        #percorre esquerda
        if (item<raiz.dado) :
            if(raiz.esquerda is  None): # se o filho da esquerda estiver vazio , cria um novo nodo encapsulando valor do item
                    no= Node(item) 
                    raiz.esquerda=no
            else:
                    self.inserir(raiz.esquerda,item) #caso contrário chama recursivamente método inserir usando o filho da esquerda como raiz
        else:
        #percorre direita
            if(raiz.direita is None): # se o filho da direita estiver vazio , cria um novo nodo encapsulando valor do item
                    no=Node(item)
                    raiz.direita=no
            else:
                    self.inserir(raiz.direita,item) #caso contrário chama recursivamente método inserir usando o filho da direita como raiz

    def mostrar(self,raiz): #metodo que realiza caminhamento pre ordenado utilizando recursao
            if(raiz != None): 
                    print raiz.dado
                    self.mostrar(raiz.esquerda)
                    self.mostrar(raiz.direita)

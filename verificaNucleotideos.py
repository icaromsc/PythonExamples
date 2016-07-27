def verificar(sequencia):
    if(isRna(sequencia)):
        print "eh um RNA"
    elif(isDna(sequencia)):
        print "eh um DNA"
    else:
        print "ha um erro na sequencia!"

def isDna(sequencia):
    return sequencia.find("T")!=-1 and true

def isRna(sequencia):
    return sequencia.find("U")!=-1
        
def purinas(sequencia):
    return sequencia.count('A') + sequencia.count('G')

def piridimas(sequencia):
    return sequencia.count('T') + sequencia.count('C')

def pareamento(sequencia):
    if(isRna(sequencia)):
        return sequencia.replace('U','T')
    elif(isDna(sequencia)):
        return sequencia.replace('T','U')
    else:
        print "ha um erro na sequencia de rna ou dna"

sequencia=raw_input("informe a sequencia genetica:")
verificar(sequencia)
print "numero de pridimas:",piridimas(sequencia)
print "numero de purinas:",purinas(sequencia)
print "pareamento:",pareamento(sequencia)

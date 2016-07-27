def pareator(sequencia):
    
    def AtoT():
        return "T"

    def TtoA():
        return "A"

    def CtoG():
        return "G"

    def GtoC():
        return"C"
    
    change= { "A" : AtoT() , "T" : TtoA() , "C" : CtoG(), "G" : GtoC() } 
    pareada=""
    
    for nucleotide in sequencia:
        pareada+=change[nucleotide]
   
    print "sequencia original: ",sequencia
    print "sequencia pareada: ",pareada

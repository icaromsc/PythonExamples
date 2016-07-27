def selectionSort(v):
	  for i in range( len(v) ):
		menor = i
		for k in range( i + 1 , len(v) ):
		      if v[k] < v[menor]:
			menor = k
		v[menor],v[i]=v[i],v[menor]
	  return v

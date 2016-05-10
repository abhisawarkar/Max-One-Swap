L=[10,20,60,40,50,30]
temp=list()

def swap(i,j):
	L[i],L[j] = L[j],L[i]
for i in xrange(len(L)-1,0,-1):
	if L[i] < L[i-1]:
		j=i-1
		while j>=0 and L[i]<L[j]:
			j-=1
		swap(i,j+1)
print L 
	


def swap(i,j):
	L[i],L[j] = L[j],L[i]

def sort(L):
	for i in xrange(len(L)-1,0,-1):
		if L[i] < L[i-1]:  # If first unordered element found
			j=i-1
			while j>=0 and L[i]<L[j]:	# Check elements before the previous index to find second unordered element 
				j-=1
			swap(i,j+1)	# swap both elements
	return L
	

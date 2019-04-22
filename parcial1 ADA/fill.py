from sys import stdin

"""Nombre: Brayan David Vera Leyton
fecha: 22/feb/2019
codigo: 8918691"""

def llenar(mid,M,A):
	capmax=mid
	cont=1
	i=0
	while i!= len(A):
		if A[i]>mid:
			return False
		if A[i]>capmax:
			if cont==M:
				return False
			cont+=1
			capmax=mid
		else:
			capmax=capmax-A[i]
			i+=1
	return True



def solve(M,A):
	ans =0
	N = len(A)
	if(N>0):
		low,hi = 1,1000000
		while low<=hi:
			mid = low+((hi-low)//2)
			if (llenar(mid,M,A)):
				ans = mid
				hi = mid-1
			else:
				low = mid+1
		return ans

def main():
  line = stdin.readline()
  while len(line)!=0:
    n,M = [ int(x) for x in line.split() ]
    A = [ int(x) for x in stdin.readline().split() ]
    print(M,A,n)
    line = stdin.readline()

main()



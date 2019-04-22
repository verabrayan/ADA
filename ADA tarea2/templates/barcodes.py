from sys import stdin
"""Nombre: Brayan David Vera Leyton
fecha: 22/feb/2019
codigo: 8918691
colaboradores:yan carlos certuche,juan miguel cardona,jeison santacruz,antonio yu
"""
def codes(N,K,M):
  tab=[[0 for _ in range(K+1)]for _ in range(N+1)]
  tab[0][0]=1
  n,k=0,0
  while n!=N+1:
    if k==K+1:
      n,k=n+1,1
    else:
    	if n==k:
    		tab[n][k]=1
    	else:
    		for i in range(1,M+1):
    			if n-i>=0:
    				tab[n][k]+=tab[n-i][k-1]
    	k+=1
  return tab[N][K]



def main():
  line = stdin.readline()
  N=len(line)
  while N!=0:
    A = [ int(x) for x in line.split() ]
    print(codes(A[0],A[1],A[2]))
    line = stdin.readline()
    N=len(line)
main()

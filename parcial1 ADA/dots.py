from sys import stdin
"""Nombre: Brayan David Vera Leyton
fecha: 25/feb/2019
codigo: 8918691
"""
def solve(B,W,M,N):
	tab=[[0 for _ in range(M+1)]for _ in range(N+1)]
	n,m=1,0
	while n!=N+1:
		if m==M+1:
			n,m=n+1,0
		else:
			tab[n][m]=tab[n-1][m]
			if W[n-1]<=m:
				tab[n][m]=max(tab[n][m],B[n-1]+tab[n-1][m-W[n-1]])
			elif  M-m+W[n-1]>2000:
				if W[n-1]<=m+200:
					tab[n][m]=max(tab[n][m],B[n-1]+tab[n-1][m-W[n-1]+200])
			
			m+=1
	return tab[N][M]

def main():
	inp=stdin
	line=stdin.readline()
	while len(line)!=0:
		pocket_money,items = [ int(x) for x in line.split() ]
		#print(pocket_money,items)
		price,favour=[0 for i in range(items)],[0 for i in range(items)]
		for j in range(items):
			tok=inp.readline().split()
			price[j]=int(tok[0])
			favour[j]=int(tok[1])
		print(solve(favour,price,pocket_money,items))
		line=stdin.readline()
main()

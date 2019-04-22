from sys import stdin
from collections import deque
INF = float('inf')
"""
Nombre: Brayan David Vera Leyton
fecha: 26/marzo/2019
codigo: 8918691
Recursos: #Codigo como se discutio en clase con pequeñas modificaciones
Discutido con: Anderson Laverde, Ruben Vargas, Yan Certuche, 
Stiven Santacruz,Santiago coca,Antonio yu
"""
kill=[(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
rey=[(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
def bfs(G,s,t,N,M):
	dist = [[INF for _ in range(M)]for _ in range(N)] ; dist[s[0]][s[1]] = 0
	visited = [[0 for _ in range(M)]for _ in range(N)] ; visited[s[0]][s[1]] = 1
	queue = deque()
	queue.append(s)
	while len(queue)!=0:
		u = queue.popleft()
		for x,y in rey:
			if ((0<=u[0]+x<N and 0<=u[1]+y<M) and (visited[u[0]+x][u[1]+y]==0)):
				if ((G[u[0]+x][u[1]+y]==1) or (G[u[0]+x][u[1]+y]==3)):
					dist[u[0]+x][u[1]+y]=dist[u[0]][u[1]]+1
					queue.append((u[0]+x,u[1]+y))
					visited[u[0]+x][u[1]+y]=1
					if G[u[0]+x][u[1]+y]==3:
						return dist[t[0]][t[1]]
		visited[u[0]][u[1]]=2


def solve(G,N,M):
	tab=[[0 for _ in range(M)]for _ in range(N)]
	pos=[]
	for i in range(N):
		for j in range(M):
			if tab[i][j]==0:
				if G[i][j]==".":
					tab[i][j]=1
				elif G[i][j]=="A":
					pos_i=(i,j)
					tab[i][j]=2
				elif G[i][j]=="B":
					pos_f=(i,j)
					tab[i][j]=3
				elif G[i][j]=="Z":
					tab[i][j]=-1
					for x,y in kill:
						if (0<=i+x<N and 0<=j+y<M):
							if(G[i+x][j+y]=="."):
								tab[i+x][j+y]=-1
	return bfs(tab,pos_i,pos_f,N,M)



def main():
	global kill,rey
	line=stdin.readline().strip()
	cases=int(line)
	while cases != 0:
		G=[]
		M,N=[int(y) for y in stdin.readline().split()]
		for j in range(M):
			line=stdin.readline().strip()
			A=[]
			for k in line:
				A.append(k)
			G.append(A)
		ans=solve(G,M,N)
		if ans!=None:
			print("Minimal possible length of a trip is {}".format(ans))
		else:
			print("King Peter, you can't go now!")
		cases-=1
		
main()


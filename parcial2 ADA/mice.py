from sys import stdin
from heapq import heappop,heappush

"""Nombre: Brayan David Vera Leyton
fecha: 30/marzo/2019
codigo: 8918691
Recursos: #Codigo sssp tomado de la pagina del profesor Camilo Rocha, 
como se discutio en clase https://drive.google.com/file/d/0B-Bk1ixpbgwJb0JiN1BiYWszWFU/view

"""

INF = float('inf')
def sssp(G,source,t):
  """G is a graph representation in adjacency list format with vertices
     in the set { 0, ..., |V|-1 } and source a vertex in G"""
  # dist[u] : "minimum distance detected from source to u
  dist = [ INF for i in range(len(G)) ] ; dist[source] = 0
  visited = [ False for i in range(len(G)) ]
  heap = [ (0,source) ]
  while len(heap)!=0:
    d,u = heappop(heap)
    if not(visited[u]):
      visited[u] = True
      for v,w in G[u]:
        if dist[v]>d+w:
          dist[v] = d+w
          heappush(heap,(dist[v],v))
  return dist

def main():
	line = stdin.readline().strip()
	cases = int(line)
	for i in range(cases):
		line=stdin.readline()
		n = int(stdin.readline().strip())
		e = int(stdin.readline().strip())
		t = int(stdin.readline().strip())
		m = int(stdin.readline().strip())
		G = [[] for _ in range(n)]
		cont=0
		for i in range(m):
			line = stdin.readline().strip()
			u,v,w = line.split()
			G[int(v)-1].append((int(u)-1,int(w)))
		#print(G)
		ans=sssp(G,e-1,n)
		for j in ans:
			if j<= t:
				cont+=1
		print(str(cont)+'\n')



main()
from sys import stdin

from collections import deque

"""
Nombre: Brayan David Vera Leyton
fecha: 25/marzo/2019
codigo: 8918691
Recursos: #Codigo como se discutio en clase con pequeñas modificaciones
Discutido con: Anderson Laverde, Ruben Vargas, Yan Certuche, 
Stiven Santacruz,Santiago coca
"""
INF = float('inf')

def bfs(G,s,t):
  """G : lista de adyacencia ; s : nodo inicial"""
  dist = [ INF for i in range(len(G)) ] ; dist[s] = 0
  visited = [0 for _ in range(len(G))] ; visited[s] = 1
  queue = deque()
  queue.append(s)
  while len(queue)!=0:
    u = queue.popleft()
    for v in G[u]:
      if visited[v]==0:
        dist[v]=dist[u]+1
        queue.append(v) ; visited[v] = 1
    visited[u] = 2
  return dist[t]-1



def main():
  line = stdin.readline().strip()
  cases = int(line)
  for i in range(cases):
    line=stdin.readline()
    vertex = int(stdin.readline().strip())
    G = [INF for _ in range(vertex)]
    for i in range(vertex):
      line = stdin.readline().strip()
      conexiones = [int(i) for i in line.split()]
      A = []
      for i in range(2, len(conexiones)):
        A.append(conexiones[i])
      G[conexiones[0]] = A
    s,t=[int(y) for y in stdin.readline().split()]
    if s==t:
      print(s,t,str(-1)+'\n')
    else:
      print(s,t,str(bfs(G,s,t))+'\n')

main()





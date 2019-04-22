from sys import stdin
"""Nombre: Brayan David Vera Leyton
fecha: 23/marzo/2019
codigo: 8918691
Recursos: #Codigo como se discutio en clase con pequeñas modificaciones
https://drive.google.com/file/d/1paBCNXbl6AV4zzP0AyYvGBujl82taocz/view
#impresion en una sola linea
https://stackoverrun.com/es/q/2972630
Discutido con: santiago coca,ruben vargas
"""

class dforest(object):
  """Disjoint-Union implementation with disjoint forests using path
  compression and ranking"""

  def __init__(self, size=100):
    """create an empty disjoint forest"""
    self.__parent = [ i for i in range(size) ]
    self.__rank = [ 0 for _ in range(size) ]

  def __str__(self):
    """return the string representation"""
    return str(self.__parent)
  
  def find(self, x):
    """return the representative of x"""
    if self.__parent[x]!=x: self.__parent[x] = self.find(self.__parent[x])
    return self.__parent[x]

  def union(self, x, y):
    """perform the union of the collections where x and y belong"""
    rx,ry = self.find(x),self.find(y)
    if rx!=ry:
      krx,kry = self.__rank[rx],self.__rank[ry]
      if krx>=kry:
        self.__parent[ry] = rx
        if krx==kry: self.__rank[rx] += 1
      else:
        self.__parent[rx] = ry

def kruskal(G, lenv):
  ans = list()
  G.sort(key=lambda x: x[2])
  df = dforest(lenv)
  c=list()
  for u,v,w in G:
  	if df.find(u)!=df.find(v):
  		ans.append((u, v, w))
  		df.union(u, v)
  	else:
  		c.append(w)
  return c


def main():
	inp=stdin
	line=stdin.readline()
	while line!='0 0\n':
		nodos,arcos = [ int(x) for x in line.split() ]
		a=list()
		for j in range(arcos):
			tmp=inp.readline().strip()
			u,v,w=[int(x) for x in tmp.split()]
			a.append((u,v,w))
		ans=(kruskal(a,nodos))
		if len(ans)!=0:
			print(*ans)
		else:
			print("forest")
		line=stdin.readline()
main()
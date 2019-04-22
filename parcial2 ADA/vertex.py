from sys import stdin
"""Nombre: Brayan David Vera Leyton
fecha: 1/abril/2019
codigo: 8918691
Recursos: #Codigo bfs discutido en clase.

"""
def dfs(G, start):
	visited=[False for i in range(len(G))]
	stack = []
	stack.append(start)
	isSon=False
	a=[]
	while stack:
		v = stack.pop()
		if not visited[v]:
			visited[v]=True
		for w in G[v]:
			if w==start:
				isSon=True
			if not visited[w] and not w in stack:
				stack.append(w)
	if not isSon:
		visited[start]=False
	for i in range(len(visited)):
		if not visited[i]:
			a.append(i+1)
	return a
def main():
	inp=stdin
	line=stdin.readline().strip()
	while line!='0':
		N=int(line)
		G = [[] for _ in range(N)]
		fin=stdin.readline().strip()
		while fin !='0':
			tok=[int(i) for i in fin.split()]
			for i in range(1, len(tok)-1):
				G[tok[0]-1].append(tok[i]-1)
			fin=stdin.readline().strip()
		tok2=[int(i)-1 for i in stdin.readline().strip().split()]
		tok2.pop(0)
		for j in tok2:
			ans=dfs(G, j)
			if len(ans)==0:
				print (0)
			else:
				print(len(ans),*ans)
		line=stdin.readline().strip()


main()


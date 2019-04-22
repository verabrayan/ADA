from sys import stdin
"""Nombre: Brayan David Vera Leyton
fecha: 8/marzo/2019
codigo: 8918691
Recursos: #Codigo mic tomado de la pagina del profesor Camilo Rocha, 
como se discutio en clase https://bitbucket.org/snippets/hquilo/b6n5e

"""
def mic(L,H,a):
  ans,low,n,ok,N = list(),L,0,True,len(a)
  while ok and low<H and n!=N:
    ok = a[n][0]<=low
    best,n = n,n+1
    while ok and n!=N and a[n][0]<=low:
      if a[n][1]>a[best][1]:
        best = n
      n += 1
    ans.append(best)
    low = a[best][1]
  ok = ok and low>=H
  if ok==False:
    ans = list()
  return ans


def main():
	inp=stdin
	line=stdin.readline()
	while line!='0 0\n':
		road,gas = [ int(x) for x in line.split() ]
		a=[]
		for j in range(gas):
			tmp=inp.readline().strip()
			location,rad=[int(x) for x in tmp.split()]
			a.append([location-rad,location+rad])
		a.sort()
		ans=mic(0,road,a)
		if len(ans)!=0:
			print(gas-len(ans))
		else:
			print(-1)
		line=stdin.readline()
main()

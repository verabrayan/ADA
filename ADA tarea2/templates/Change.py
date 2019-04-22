from sys import stdin


"""Nombre: Brayan David Vera Leyton
fecha: 20/feb/2019
codigo: 8918691
colaboradores:yan carlos certuche,stiven santa cruz,anderson laverde,santiago coca
"""
Den=[5,10,20,50,100,200]
inf=100000

def coin(X):
  N=len(Den)
  tab=[inf for _ in range(X+1)]
  tab[0]=0
  n,x=1,0
  while n!=N+1:
    if x==X+1:
      n,x=n+1,0
    else:
      if Den[n-1]<=x:
        tab[x]=min(tab[x],1+tab[x-Den[n-1]])
      x+=1
  return tab[X]


def making(c,x):
  D=[int(c[x]) for x in range(len(c)-1)]
  N=len(D)
  cont=0
  for i in reversed(range(N)):
    c=min(D[i],(x//Den[i]))
    if Den[i]<=x:
      x=x-Den[i]*c
      cont+=c
  if x!=0:
    return inf
  else:
    return cont

def main():
  global Den,inf
  A={}
  C = [float(x) for x in stdin.readline().split()]
  end= [0,0,0,0,0,0]
  for i in range(5,205,5):
    A[i]=coin(i)
  while C!= end:
    X=round(C[-1]*100)
    val=making(C,X)
    for i in range(5,205,5):
      val=min(val,(making(C,X+i)+A[i]))
    print("{:3d}".format(val))
    C= [float(x) for x in stdin.readline().split()]

main()





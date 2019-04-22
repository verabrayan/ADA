from sys import stdin

"""Nombre: Brayan David Vera Leyton
fecha: 20/feb/2019
codigo: 8918691
colaboradores:yan carlos certuche,stiven santa cruz
"""
entero=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
def solve(S):
  ans=0
  n=len(S)
  tab=[[0 for _ in range(n)]for _ in range(n)]
  x=1
  i=0
  if n==1:
    return 1
  if S[0]=='?':
    while i!= n:
      tab[i][0]=1
      i+=1
  else:
    tab[S[0]-1][0]=1
  while x!=n:
    if S[x] in entero :
      if S[x]>n and S[x]==0:
        return 0
      if S[x]!='?':
        tab[S[x]-1][x]=1
        if(S[x])== 1:
          tab[S[x]-1][x]=sum_colum(tab,x-1,n)-tab[S[x]-1][x-1]-tab[(S[x]-1)+1][x-1]
        if(S[x]) == n:
          tab[S[x]-1][x]=sum_colum(tab,x-1,n)-tab[S[x]-1][x-1]-tab[(S[x]-1)-1][x-1]
        if (S[x]) != n and (S[x]) != 1:
          tab[S[x]-1][x]=sum_colum(tab,x-1,n)-tab[S[x]-1][x-1]-tab[(S[x]-1)+1][x-1] -tab[(S[x]-1)-1][x-1]
      x+=1
    else:
      for p in range(n):   
          if p==0:
            tab[p][x]=sum_colum(tab,x-1,n)-tab[p][x-1]-tab[p+1][x-1]  
            
          elif p == n-1:
             tab[p][x]=sum_colum(tab,x-1,n)-tab[p][x-1]-tab[p-1][x-1]
            
          else:
            tab[p][x]=sum_colum(tab,x-1,n)-tab[p][x-1]-tab[p+1][x-1] -tab[p-1][x-1]

      x+=1       
  return(sum_colum(tab,n-1,n))

def sum_colum(tab,m,n):
    suma=0
    for j in range(n):

      suma +=tab[j][m]

    return suma
 
def main():
  global entero
  inp = stdin
  ans=0
  arr = [ str(x) for x in inp.readline() ]
  while len(arr) != 0:
    arr.pop()
    salida=[]
    for x in arr:
      if(ord(x)>=48 and ord(x)<=57) or (ord(x)>=65 and ord(x)<=70):
        x=int(x,16)
      salida.append(x)
    for k in range(len(salida)-1):
      if type(salida[k])==int and type(salida[k+1])==int:
        if salida[k+1]!='?':
          kill=salida[k]-salida[k+1]
          if kill==0 or kill==1 or kill==-1:
            ans=0
        else:
          ans=solve(salida)
    ans=solve(salida)
    print(ans)
    inp = stdin
    arr = [ str(x) for x in inp.readline() ]
    

main()



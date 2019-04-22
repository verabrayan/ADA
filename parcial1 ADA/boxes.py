from sys import stdin


"""Nombre: Brayan David Vera Leyton
fecha: 22/feb/2019
codigo: 8918691
"""

def tab(p,r,M):
        N=len(p)
        tab=[[0 for _ in range(M+1)]for _ in range(N+1)]
        n,m=1,0
        while n!=N+1:
                if m==M+1:
                        n,m=n+1,0
                else:
                        tab[n][m]=tab[n-1][m]
                        if p[n-1]<=m:
                                tab[n][m]=max(tab[n][m],1+tab[n-1][min(m-p[n-1],r[n-1])])
                        m+=1
        return tab[N][M]

def main():
        n=int(stdin.readline().strip())
        M=0
        while n!=0:
                p=[0 for i in range(n)]
                r=[0 for i in range(n)]
                for i in range(0,n):
                        tok = stdin.readline().strip().split()
                        x=int(tok[0])
                        y=int(tok[1])
                        p[i]=x
                        r[i]=y
                        M=max(M,x+y)
                p.reverse()
                r.reverse()
                print(tab(p,r,M))
                n=int(stdin.readline().strip())
main()









from sys import stdin
from math import *

"""Nombre: Brayan David Vera Leyton
fecha: 23/marzo/2019
codigo: 8918691
discutido con: antonio yu,anderson laverde
"""

dic={}


def hanoi(N):
	balls=0
	for i in range(N):
		maxbol=N*N
		cont=0
		for j in range(maxbol):
			if j<=N:
				sqr=int(sqrt(cont+j))
				tmp=sqr*sqr
				if tmp==cont+j:
					cont+=j
					balls+=1
	if N%2==0:
		balls-=1
	else:
		balls-=((N+1)//2)

	return balls

def solve(N):
	if N not in dic.keys():
		dic[N]=hanoi(N)
	return dic[N]

def main():
	global dic
	for j in range(1,51):
		dic[j]=hanoi(j)
	line=stdin.readline().strip()
	case=int(line)
	for i in range(case):
		tmp=stdin.readline().strip()
		N=int(tmp)
		ans=solve(N)
		if ans!=0:
			print(ans)
		else:
			print(1)


main()
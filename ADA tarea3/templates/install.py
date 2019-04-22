from sys import stdin
import math
"""Nombre: Brayan David Vera Leyton
fecha: 11/marzo/2019
codigo: 8918691
Recursos: #Codigo como se discutio en clase con pequeñas modificaciones
 https://bitbucket.org/snippets/hquilo/b6n5e
Discutido con: nicolas ortiz,nicolas alvarez
"""

def mic(a):
	ans,best,N = 1,0,len(a)
	for n in range(1,N):
		if a[best][1]<=a[n][0]:
			ans+=1
			best=n
	return ans


def main():
	inp=stdin
	case=1
	line=stdin.readline().strip()
	while line!='0 0':
		if len(line)!=0:
			islands,coverage = [ int(x) for x in line.split() ]
			a=[]
			flag=0
			for j in range(islands):
				tmp=inp.readline().strip()
				x,y=[int(x) for x in tmp.split()]
				if y<=coverage:
					hip=math.sqrt((coverage*coverage)-(y*y))
					L=x-hip
					R=x+hip
					a.append([L,R])
				else:
					flag=1
			a.sort(key=lambda s:s[1])
			if flag == 0:		
				print("Case {}: {}".format(case,mic(a)))
			else:
				print("Case {}: {}".format(case,-1))
			case+=1
		line=stdin.readline().strip()
main()
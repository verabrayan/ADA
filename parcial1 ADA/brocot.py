from sys import stdin
from fractions import Fraction

"""Nombre: Brayan David Vera Leyton
fecha: 22/feb/2019
codigo: 8918691
Recursos:https://en.wikipedia.org/wiki/Mediant_(mathematics)
		Mediants and binary search
"""
def bin(M,N):
	ans= ""
	mid=[1,1]
	low=[0,1]
	hi=[1,0]
	while (mid[0] != M and mid[1]!= N):# con and hay casos que no los hace, mejor con or
		if M*mid[1]>N*mid[0] :
			low=mid
			m,n=low[0]+hi[0],low[1]+hi[1]
			mid=[m,n]
			ans+="R"
		else:
			if M*mid[1]<N*mid[0] :
				hi=mid
				m,n=(low[0]+hi[0]),(low[1]+hi[1])
				mid=[m,n]
				ans+="L"
	return ans

def main():
	C = [int(x) for x in stdin.readline().split()]
	end= [1,1]
	while C!= end:
		print(bin(C[0],C[1]))
		C = [int(x) for x in stdin.readline().split()]
main()

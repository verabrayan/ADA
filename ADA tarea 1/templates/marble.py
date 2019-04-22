from sys import stdin
"""Nombre: Brayan David Vera Leyton
fecha: 5/feb/2019
codigo: 8918691
colaboradores: Antonio Yu"""

marble,lenm = None,None

def solve(x):
  N, ans= len(marble),-1
  if N >= 1:
    low, hi = 0,N
    if marble[0]==x:
      return 0
    while low+1 != hi :
      mid =low +((hi-low)>>1)
      if marble[mid] == x :
        hi= mid
        ans=mid
      elif marble[mid]<x:
        low=mid
      else:
        hi=mid
    return ans

def main():
  global marble,lenm
  case = 1
  lenm,lenq = [ int(x) for x in stdin.readline().split() ]
  while lenm+lenq!=0:
    marble = [ int(stdin.readline()) for i in range(lenm) ]
    marble.sort()
    print('CASE# {0}:'.format(case))
    for q in range(lenq):
      x = int(stdin.readline())
      ans = solve(x)
      if ans==-1 or marble[ans]!=x:
        print('{0} not found'.format(x))
      else:
        print('{0} found at {1}'.format(x,ans+1))
    lenm,lenq = [ int(x) for x in stdin.readline().split() ]
    case += 1

main()

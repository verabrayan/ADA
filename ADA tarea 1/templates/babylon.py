from sys import stdin
from itertools import *

MAX = 35
blocks = [None for i in range(MAX)]

 def solve():
  b=[]
  for i in (blocks):
    a=[blocks[0],blocks[2],blocks[1]]
    b=[blocks[2],blocks[0],blocks[1]]
    c=[blocks[2],blocks[1],blocks[0]]
    d=[blocks[1],blocks[0],blocks[2]]
    e=[blocks[1],blocks[2],blocks[0]]

def main():
  n = int(stdin.readline().strip())
  case = 1
  while n!=0:
    for i in range(n):
      x, y, z = map(int, stdin.readline().strip().split())
      blocks.append((x, y, z))
    #ans = solve()
    print('Case {0}: maximum height = {1}'.format(case, ans))
    n = int(stdin.readline().strip())
    case += 1

main()

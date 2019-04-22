from sys import stdin

def solve(a):
  tmp=[]
  tmp.append(a[0])
  for i in range(1,len(a)):
    ans=max(a[i],(tmp[i-1]+a[i]),0)
    tmp.append(ans)
  return max(tmp)


def main():
  global bet
  inp = stdin
  n = int(inp.readline().strip())
  while n!=0:
    tok = inp.readline().strip().split()
    for i in range(n): tok[i] = int(tok[i])
    ans = solve(tok)
    if ans<=0: print('Losing streak.')
    else: print('The maximum winning streak is {0}.'.format(ans))
    n = int(inp.readline().strip())

main()
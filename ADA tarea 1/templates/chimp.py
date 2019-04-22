from sys import stdin

def solve1(ladies, x):
  ans=0
  if len(ladies) >= 1:
    low, hi = 0,len(ladies)
    while ladies[low] != x and low+1 != hi :
      mid =low +((hi-low)//2)
      if ladies[mid] < x :
        low = mid
      else:
        hi=mid
    ans= ladies[low]
    if x< ans:
      ans="X"
      return ans
    else:
      return ans
  

def solve2(ladies, x):
  ans=0
  if len(ladies) >= 1:
    low, hi = 0,len(ladies)-1
    while ladies[hi] != x and low+1 != hi :
      mid =low +((hi-low)//2)
      if ladies[mid] > x :
        hi = mid
      else:
        low=mid
    ans= ladies[hi]
    if x> ans:
      ans="X"
      return ans
    else:
      return ans
      

def main():
  inp = stdin
  inp.readline()
  ladies = [ int(x) for x in inp.readline().split() ]
  inp.readline()
  queries = [ int(x) for x in inp.readline().split() ]
  for x in queries:
    max_inf=solve1(ladies, x)
    min_sup=solve2(ladies,x)
    print("{0} {1}".format(max_inf,min_sup))

main()

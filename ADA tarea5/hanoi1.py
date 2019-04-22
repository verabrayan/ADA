dic={}


def hanoi(N):
	palos=[0 for _ in range(N)]
	palos[0]=1
	balls,i=1,0
	flag1=False
	while not flag1:
		balls+=1
		flag=False
		j=0
		while not flag and j!=i+1:
			sqr=int(sqrt(palos[j]+balls))
			tmp=sqr*sqr
			if tmp==palos[j]+balls:
				palos[j]=balls
				flag=True
			j+=1
		if not flag:
			i+=1
			if i!=N:
				palos[i]=balls
			else:
				flag1=True
	return balls-1


def solve(N):
	if N not in dic.keys():
		dic[N]=hanoi(N)
	return dic[N]


def main():
	global dic
	line=stdin.readline().strip()
	case=int(line)
	for j in range(1,51):
		dic[j]=hanoi(j)
	for i in range(case):
		tmp=stdin.readline().strip()
		N=int(tmp)
		print(solve(N))

main()
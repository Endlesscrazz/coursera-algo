#python 3

def max_revenue(n):

	
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]
	a.sort()
	b.sort()
	ans = sum([a[i]*b[i] for i in range(n)])
	print(ans)

n = int(input())
max_revenue(n)
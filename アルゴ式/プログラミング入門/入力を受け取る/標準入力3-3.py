N = int(input())

l = list(map(int, input().split()))

for i in range(N):
	ans = l[i]%10
	print(ans)
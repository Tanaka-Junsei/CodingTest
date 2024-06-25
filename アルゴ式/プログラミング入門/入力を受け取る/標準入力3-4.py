N = int(input())

l = list(map(int, input().split()))

for i in range(N):
	if l[i]%3 == 0:
		print("{}".format(l[i]))
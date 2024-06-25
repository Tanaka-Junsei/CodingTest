N = int(input())

l = list(map(int, input().split()))

l_reversed = list(reversed(l))

for i in range(N):
	print("{}".format(l_reversed[i]))
	
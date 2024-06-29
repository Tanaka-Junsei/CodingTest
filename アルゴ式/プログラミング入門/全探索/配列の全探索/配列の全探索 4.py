N, V = map(int, input().split())

A_list = list(map(int, input().split()))

ans = -1

for i in range(N):
	if A_list[i] == V:
		ans = i

print(ans)
N = int(input())

A = [""]*N

for i in range(N):
	A.append(input())

right_nums = 0
left_nums = 0


for i in range(N):
	if A[i] == 'right':
		right_nums += 1
	else:
		left_nums += 1

ans = ''

if right_nums > left_nums:
	ans = 'right'
elif right_nums < left_nums:
	ans = 'left'
else:
	ans = 'same'

print(ans)
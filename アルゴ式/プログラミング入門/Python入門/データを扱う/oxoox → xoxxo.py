S = input()

S_list = list(S)

for i in range(len(S_list)):
	if S_list[i] == 'o':
		S_list[i] = 'x'
	else:
		S_list[i] = 'o'

S = str(S_list)

print(S)
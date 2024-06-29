N = int(input())

A = list(map(int, input().split()))

nums_dic = { 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}

for i in range(N):
    nums_dic[A[i]] += 1

for i in range(1, 10):  # 1から9までの数値でループする
    print(nums_dic[i])

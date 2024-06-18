N = int(input())

A = list(map(int, input().split()))

Q = int(input())

B = list(map(int, input().split()))

for i in range(Q):
    print(A[B[i] -1])



# 1, 2, 3, 4, s
# 0, 1, 2, 3

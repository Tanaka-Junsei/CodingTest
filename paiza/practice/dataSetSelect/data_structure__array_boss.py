N, Q = map(int, input().split())

A = list(map(int, input().split()))

QueryList = []

for _ in range(Q):
    QueryList.append(list(map(int, input().split())))


for i in range(Q):
    if QueryList[i[0]] == 0:
        A.append(QueryList[i[1]])
    elif QueryList[i[0]] == 1:
        A = A[:N-1]
    else:
        for j in range(A):
            print("{} ".format(A[j]))
            
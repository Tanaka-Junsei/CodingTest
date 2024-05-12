N = int(input())

S_1 = input()
S_2 = input()

def rotate(s1, s2, N):
    
    for i in range(N):
        if s1 == s2:
            return "Yes"
    
        s2 = s2[-1] + s2[:-1]
    
    return "No"

print(rotate(S_1, S_2, N))





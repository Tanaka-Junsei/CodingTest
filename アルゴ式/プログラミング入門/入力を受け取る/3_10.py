S = input()
N, M = map(int, input().split())

S = list(S) # Pythonの文字列はイミュータブルだから配列操作でいじることはできないため、リストに変換

word_N = S[N-1]
word_M = S[M-1]

S[N-1] = word_M
S[M-1] = word_N

print("".join(S)) # ここでリストを文字列に変換

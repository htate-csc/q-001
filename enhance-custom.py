S = input()
N = int(input())
ps = list(input().split())

for p in ps:
    S += ' '
    for i in range(int(p)):
        S += 'a'
print(S)

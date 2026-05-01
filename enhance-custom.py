S = input()
N = int(input())
p = list(input().split())

for i in range(N):
    S += ' '
    for v in range(int(p[i])):
        S += 'a'
print(S)

# 別解
# S = input()
# N = int(input())
# ps = list(input().split())
# for p in ps:
#     S += ' '
#     for i in range(int(p)):
#         S += 'a'
# print(S)

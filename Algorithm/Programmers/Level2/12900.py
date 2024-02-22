import sys
sys.setrecursionlimit(10 ** 6)

global dp
dp = [0] + [-1] * 60000

def recursion(n):
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = recursion(n-1) + recursion(n-2)
    
    return dp[n] % 1000000007
    

def solution(n):
    dp[1] = 1
    dp[2] = 2
    answer = recursion(n)
    return answer

from itertools import permutations

# 주어진 두 리스트
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 결과를 저장할 리스트
result = []

# list1의 원소를 기준으로 모든 순열을 생성
print(list(permutations(list2)))
# for perm in permutations(list2):
#     case = []
#     # 각 순열에 대해 list1의 원소와 짝을 지어 새로운 쌍을 생성
#     for i in range(len(list1)):
#         case.append([list1[i], perm[i]])
#     result.append(case)

# # 생성된 모든 경우의 수 출력
# for r in result:
#     print(r)
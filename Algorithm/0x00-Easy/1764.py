import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 듣도 못한 사람의 명단과 보도 못한 사람의 명단을 집합으로 저장
not_heard = set(input().strip() for _ in range(N))
not_seen = set(input().strip() for _ in range(M))

# 듣도 보도 못한 사람의 명단은 두 집합의 교집합
not_heard_and_seen = not_heard & not_seen

# 듣도 보도 못한 사람의 수와 명단을 출력
print(len(not_heard_and_seen))
for person in sorted(not_heard_and_seen):
    print(person)
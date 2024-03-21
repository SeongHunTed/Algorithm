def solution(A, B):
    answer = 0
    i = 0
    A.sort()
    B.sort()
    
    for k in range(len(A)):
        while i < len(B) and A[k] >= B[i]:
            i += 1
        if i < len(B):
            if A[k] < B[i]:
                answer += 1
            i += 1
    
    return answer
                

# 시간 초과
# import heapq as hq

# def solution(A, B):
#     answer = 0
#     q = []
#     for item in B:        
#         hq.heappush(q, item)
    
#     for i in range(len(A)):
#         targetNumber = A[i]
#         popped = []
        
#         while q:
#             if q[0] > targetNumber:
#                 hq.heappop(q)
#                 answer += 1
#                 break
#             else:
#                 popped.append(hq.heappop(q))
        
#         for item in popped:
#             hq.heappush(q, item)
    
    
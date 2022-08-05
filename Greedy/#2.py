n, m, k = map(int, input().split())

list1 = list(map(int, input().split()))
list1.sort()

#1번째정답
#
# first_num = list1[n-1]
# second_num = list1[n-2]
#
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first_num
#         m -= 1
#
#     if m == 0:
#         break
#     result += second_num
#     m -= 1
#
# print(result)

# 두번째 답

first = list1[n-1]
second = list1[n-2]

count = m // (k+1) * k
count += m % (k+1)

result = 0
result += count * first
result += (m - count) * second

print(result)


# 내가 푼 답
# sum_ = 0
# count = 0
# max_num = max(list1)
#
# for i in range(m):
#     if max_num <= max(list1):
#         max_num = max(list1)
#     if count == k:
#         max_num = list1[n-2]
#         count = 0
#
#     sum_ += max_num
#     count += 1
#
# print(sum_)




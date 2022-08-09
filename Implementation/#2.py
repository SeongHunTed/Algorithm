user_hour = int(input())

hour = 0
minute = 0
second = 0
count = 0

while True:
    if hour == user_hour and minute == 59 and second == 59:
        break
    if hour % 10 == 3 or minute % 10 == 3 or second % 10 == 3:
        count += 1
    elif minute // 10 == 3 or second // 10 == 3:
        count += 1

    second += 1

    if second == 60:
        minute += 1
        second = 0
    if minute == 60:
        hour += 1
        minute = 0


print(count)



pay, money = map(int, input().split())

count = 0
change = money - pay
coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += change // coin
    change %= coin

print(count)



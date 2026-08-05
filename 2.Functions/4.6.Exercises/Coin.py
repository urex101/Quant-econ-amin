import numpy as np


rng = np.random.default_rng()
k = 3
heads = 0
tails = 0
money = 0
coin_list = []
for _ in range(10):
    coin = rng.choice([-1, 1], p=[0.5, 0.5])
    coin_list.append(coin)
    if coin == 1:
        heads += 1
    if coin == -1:
        tails += 1
print("Flips:", coin_list)


for coin in range(len(coin_list)):
    if coin_list[coin] == 1 and coin_list[coin:coin+k] == [1]*k:
        money += 1
    if coin_list[coin] == -1 and coin_list[coin:coin+k] == [-1]*k:
        money += 1

print("money:", money)
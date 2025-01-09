def new_secret_number(secret_number, n_steps):
    bananas_prev = secret_number % 10
    change = [0, 0, 0, 0]
    sell_price = {}
    for n in range(n_steps):
        secret_number = ((secret_number * 64) ^ secret_number) % 16777216
        secret_number = ((secret_number // 32) ^ secret_number) % 16777216
        secret_number = ((secret_number * 2048) ^ secret_number) % 16777216
        bananas = secret_number % 10
        ch = bananas - bananas_prev
        if n <= 3:
            change[n] = ch
            if n == 3:
                sell_price[str(change)] = bananas
        else:
            change[:3] = change[1:]
            change[3] = ch
            if str(change) not in sell_price.keys():
                sell_price[str(change)] = bananas
        bananas_prev = bananas
    return sell_price

f = open("input22.txt", "r")
sell_price_tot = {}
for line in f:
    secret_number = int(line.strip())
    sell_price = new_secret_number(secret_number, 2000)
    for key in sell_price.keys():
        sell_price_tot[key] = sell_price_tot.get(key, 0) + sell_price[key]

print(max(sell_price_tot.values()))
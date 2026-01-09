def choose_coins(coins:[list[int]], target:[int]) -> str:
    coins.sort(reverse=True)

    used_coins = {}
    index = 0
    while target != 0 and index < len(coins):
        count_coins = target // coins[index]
        target %= coins[index]

        if count_coins > 0:
            used_coins[coins[index]] = count_coins
        index += 1

    if target != 0:
        return 'Error'

    result = f'Number of coins to take: {sum(used_coins.values())}\n'
    for key, value in used_coins.items():
        result += f'{value} coin(s) with value {key}\n'

    return result

coins = [int(el) for el in input().split(', ')]
target = int(input())

print(choose_coins(coins,target))
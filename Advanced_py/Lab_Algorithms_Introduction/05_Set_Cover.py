def set_cover(universe, sets):
    universe_set = set(universe)
    chosen_sets = []
    remaining_sets = sets.copy()

    while universe_set and remaining_sets:
        best_set = max(remaining_sets, key=lambda s: universe_set.intersection(s))
        if not universe_set.intersection(best_set):
            break

        chosen_sets.append(best_set)
        universe_set -= set(best_set)
        remaining_sets.remove(best_set)

    if universe_set:
        return
    return chosen_sets

universe = list(map(int, input().split(', ')))
n = int(input())
sets = []

for _ in range(n):
    set_elements = list(map(int, input().split(', ')))
    sets.append(set_elements)

result = set_cover(universe,sets)
if result is None:
    print("No solution exists")
else:
    result.sort(key=len, reverse=True)
    for i in range(len(result)):
        result[i] = sorted(result[i])

    print(f'\nSets to take ({len(result)}):')
    for s in result:
        print("{", ", ".join(map(str,s)), "}")
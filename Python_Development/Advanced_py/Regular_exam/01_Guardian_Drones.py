from collections import deque

mecha_parts = [int(el) for el in input().split()]
energy_levels = deque(int(el) for el in input().split())

drones = {
    100: "Sentinel-X",
    85: "Viper-MKII",
    75: "Aegis-7",
    65: "Striker-R",
    55: "Titan-Core",
}

successfully_assembled = []

while mecha_parts and energy_levels and len(successfully_assembled) < 5:
    part = mecha_parts.pop()

    while energy_levels and energy_levels[0] <= 0:
        energy_levels.popleft()
    if not energy_levels:
        break

    power_cell = energy_levels.popleft()
    total_power = part + power_cell

    if total_power in drones and drones[total_power] not in successfully_assembled:
        successfully_assembled.append(drones[total_power])
        continue

    for drone_power in sorted(drones.keys(), reverse=True):
        if total_power > drone_power and drones[drone_power] not in successfully_assembled:
            successfully_assembled.append(drones[drone_power])
            power_cell -= 30
            if power_cell > 0:
                energy_levels.append(power_cell)
            break
    else:
        power_cell -= 1
        if power_cell > 0:
            energy_levels.append(power_cell)

if len(successfully_assembled) == 5:
    print("Mission Accomplished! All Guardian Drones activated!")
else:
    print("Mission Failed! Some drones were not built.")

if successfully_assembled:
    print(f"Assembled Drones: {', '.join(successfully_assembled)}")

if mecha_parts:
    print(f"Mechanical Parts: {', '.join(str(x) for x in reversed(mecha_parts))}")
if energy_levels:
    print(f"Power Cells: {', '.join(str(x) for x in energy_levels if x > 0)}")

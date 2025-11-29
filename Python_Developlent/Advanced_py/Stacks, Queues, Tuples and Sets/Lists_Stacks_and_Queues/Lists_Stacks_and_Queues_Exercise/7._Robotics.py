from collections import deque


def time_to_seconds(time_str):
    parts = time_str.split(":")
    h = int(parts[0])
    m = int(parts[1])
    s = int(parts[2])
    return h * 3600 + m * 60 + s

def seconds_to_time(total_seconds):
    total_seconds = total_seconds % (24 * 3600)
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60

    if h < 10:
        hh = "0" + str(h)
    else:
        hh = str(h)

    if m < 10:
        mm = "0" + str(m)
    else:
        mm = str(m)

    if s < 10:
        ss = "0" + str(s)
    else:
        ss = str(s)

    return hh + ":" + mm + ":" + ss

all_robots = input().split(';')
timestr = input()

products_queue = deque()
robots_queue = deque()

while True:
    command = input()
    if command == 'End':
        break

    products_queue.append(command)

for robot_data in all_robots:
    robot_parts = robot_data.split("-")
    name = robot_parts[0]
    proc_time = int(robot_parts[1])
    robot = {
        "name": name,
        "proc_time": proc_time,
        "available_in": 0
    }
    robots_queue.append(robot)

current_time = time_to_seconds(timestr)

while len(products_queue) > 0:
    current_time+=1
    product = products_queue.popleft()
    assigned = False
    for robot in robots_queue:
        if robot["available_in"] == 0:
            print(robot["name"] + " - " + product + " [" + seconds_to_time(current_time) + "]")
            assigned = True
            robot["available_in"] = robot["proc_time"]
            break
    if not assigned:
        products_queue.append(product)

    for robot in robots_queue:
        if robot["available_in"] > 0:
            robot["available_in"] -= 1
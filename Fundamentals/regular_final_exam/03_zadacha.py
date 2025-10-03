record = {}

while True:
    inpt = input().split(': ')
    if inpt[0] == 'Log out':
        break

    command = inpt[0]

    if command == 'New follower':
        username = inpt[1]
        if username not in record:
            record[username] = {"likes": 0, "comments": 0}

    elif command == 'Like':
        username = inpt[1]
        count = int(inpt[2])
        if username not in record:
            record[username] = {"likes": count, "comments": 0}
        else:
            record[username]["likes"] += count

    elif command == 'Comment':
        username = inpt[1]
        if username not in record:
            record[username] = {"likes": 0, "comments": 1}
        else:
            record[username]["comments"] += 1

    elif command == 'Blocked':
        username = inpt[1]
        if username not in record:
            print(f"{username} doesn't exist.")
        else:
            del record[username]

print(f"{len(record)} followers")

for name, data in record.items():
    total = data["likes"] + data["comments"]
    print(f"{name}: {total}")

parking = {}
n = int(input())

for i in range(n):
    command = input().split()

    r_unr = command[0]
    username = command[1]



    if r_unr == 'register':
        license_plate = command[2]
        if username in parking.keys():
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")




    else:
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")
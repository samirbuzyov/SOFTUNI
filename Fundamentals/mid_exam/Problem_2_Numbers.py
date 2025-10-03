numbers = input().split()

while True:
    command = input().split()

    if command[0] == 'Finish':
        break

    elif command[0] == 'Add':
        numbers.append(command[1])

    elif command[0] == 'Remove':
        # Only remove the first occurrence of the value
        if command[1] in numbers:
            numbers.remove(command[1])

    elif command[0] == 'Replace':
        idx = numbers.index(command[1])
        numbers[idx] = command[2]


    elif command[0] == 'Collapse':
        value = command[1]
        i = 0
        while i < len(numbers):
            if int(numbers[i]) < int(value):
                numbers.pop(i)
            else:
                i += 1

# Print the final sequence
print(" ".join(numbers))

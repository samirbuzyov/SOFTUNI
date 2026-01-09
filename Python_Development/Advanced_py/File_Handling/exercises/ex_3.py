import os
while True:
    line = input()
    if line == 'End':
        break

    command, file_name, *args = line.split('-')
    path = os.path.join('..', 'files', f'{file_name}')

    if command == 'Create':
        open(path,'w').close()
    elif command == 'Add':
        with open(path, 'a') as f:
            f.write(f'{args[0]}\n')
    elif command == 'Replace':
        try:
            with open(path, 'r+') as f:
                content = f.read()
                f.seek(0)
                f.truncate(0)
                f.write(content.replace(args[0], args[1]))
        except FileNotFoundError:
            print("An error occurred")
    elif command == 'Delete':
        if os.path.exists(path):
            os.remove(path)
        else:
            print("An error occurred")


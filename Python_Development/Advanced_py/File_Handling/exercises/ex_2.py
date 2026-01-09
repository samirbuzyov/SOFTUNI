import os
from string import punctuation
path1 = os.path.join('..', 'files', 'text.txt')
path2 = os.path.join('..', 'files', 'output.txt')
with open(path1, 'r') as input_file, open(path2, 'w') as output_file:
    for row, line in enumerate(input_file.readlines()):
        letters_count = 0
        symbols_count = 0
        for char in line:
            if char.isalpha():
                letters_count+=1
            elif char in punctuation:
                symbols_count+=1
        output_file.write(f"Line {row + 1}: {line.strip()} ({letters_count})({symbols_count})\n")
        print(f"Line {row + 1}: {line.strip()} ({letters_count})({symbols_count})\n")

output_file.close()
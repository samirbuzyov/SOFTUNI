import os
import re

path = os.path.join('..', 'files', 'text.txt')
with open(path) as f:
    # for idx, line in enumerate(f):
    #     if idx % 2 == 0:
    #         for ch in {"-", ",", ".", "!", "?"}:
    #             line = line.replace(ch, '@')
    #
    #         print(' '.join(reversed(line.split())))

    lines = f.readlines()
    for i in range(0, len(lines), 2):
        line = reversed(re.sub("[-,.!?]", "@", lines[i]).split())
        print(*line)
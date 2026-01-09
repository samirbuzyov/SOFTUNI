import re

txt = input()
while txt:
    pattern = r'(\d+)'
    match = re.findall(pattern,txt)

    if match:
        print(' '.join(match), end=' ')

    txt = input()
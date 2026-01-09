from re import findall

txt = input()

pattern = r'\b_([A-Za-z0-9]+)\b'
match = findall(pattern,txt)
print(','.join(match))
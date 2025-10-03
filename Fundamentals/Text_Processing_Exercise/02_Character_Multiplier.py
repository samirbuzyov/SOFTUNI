line = input().split()

str1, str2 = line[0], line[1]
total_sum = 0

if len(str1) == len(str2):
    for i in range(len(str1)):
        n = 1
        n *= ord(str1[i])
        n *= ord(str2[i])
        total_sum += n

else:
    if len(str1) > len(str2):
        for i in range(len(str2)):
            n = 1
            n *= ord(str1[i])
            n *= ord(str2[i])
            total_sum += n

        for i in range(len(str2), len(str1)):
            total_sum += ord(str1[i])
    else:
        if len(str2) > len(str1):
            for i in range(len(str1)):
                n = 1
                n *= ord(str1[i])
                n *= ord(str2[i])
                total_sum += n

            for i in range(len(str1), len(str2)):
                total_sum += ord(str2[i])

print(total_sum)
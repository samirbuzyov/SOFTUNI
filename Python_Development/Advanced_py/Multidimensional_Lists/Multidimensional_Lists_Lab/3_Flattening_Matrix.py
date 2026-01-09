rows = int(input())
nums = []

for _ in range(rows):
    row_data = [int(el) for el in input().split(', ')]
    nums.extend(row_data)

print(nums)
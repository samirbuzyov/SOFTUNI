def binary_search(numbers: list[int], t: int) -> int:
    left, right = 0, len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == t:
            return mid
        elif t > numbers[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1



nums = list(map(int, input().split()))
target = int(input())
print(binary_search(nums, target))
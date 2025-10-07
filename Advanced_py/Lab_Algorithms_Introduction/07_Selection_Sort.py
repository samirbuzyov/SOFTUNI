def selection_sort(nums):
    for idx in range(len(nums)):
        min_idx = idx
        for curr_idx in range(idx + 1, len(nums)):
            if nums[min_idx] > nums[curr_idx]:
                min_idx = curr_idx

        nums[idx], nums[min_idx] = nums[min_idx], nums[idx]

    return nums
numbers = [int(el) for el in input().split()]

print(*selection_sort(numbers))
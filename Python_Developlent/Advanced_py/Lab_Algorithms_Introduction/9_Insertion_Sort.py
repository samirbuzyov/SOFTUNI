def insertion_sort(nums):
    for j in range(len(nums)):
        for i in range(j,0,-1):
            if nums[i] < nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
            else:
                break
    return nums



numbers = [int(el) for el in input().split()]

sorted_nums = insertion_sort(numbers)
print(*sorted_nums)
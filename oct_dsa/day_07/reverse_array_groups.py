def reverse_array_groups(nums, k):
    n = len(nums)
    start = 0
    while start < n:
        left = start
        right = min(start + k - 1, n - 1)
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        start += k
    return nums
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(reverse_array_groups(nums, k))
#time complexity-o(n)
#space complexity-o(1)
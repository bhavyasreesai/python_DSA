def rotate_array_ksteps(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
def rotate_array_in_place(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    k = k % n
    rotate_array_ksteps(nums, 0, n - 1)
    rotate_array_ksteps(nums, 0, k - 1)
    rotate_array_ksteps(nums, k, n - 1)
    return nums
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_array_in_place(nums, k))
#time complexity-o(n)
#space complexity-o(1)
def missing_number(nums):
    n = len(nums)
    for i in range(n + 1):
        found = False
        for j in range(n):
            if nums[j] == i:
                found = True
                break
        if not found:
            return i
nums = [3, 0, 1,2]
print(missing_number(nums))
#time complexity-o(n^2)
#space complexity-o(1)
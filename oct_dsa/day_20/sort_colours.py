def sort_colors(nums):
    count = [0, 0, 0]
    for i in range(len(nums)):
        count[nums[i]] += 1
    index = 0
    for i in range(3):
        while count[i] > 0:
            nums[index] = i
            index += 1
            count[i] -= 1
    return nums
nums = [2, 0, 2, 1, 1, 0]
print(sort_colors(nums))
#output-[0, 0, 1, 1, 2, 2]
#time complexity-o(n)
#space complexity-o(1)
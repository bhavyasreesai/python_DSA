def sort(nums):
    count = [0, 0]
    for i in range(len(nums)):
        count[nums[i]] += 1
    index = 0
    for i in range(2):
        while count[i] > 0:
            nums[index] = i
            index += 1
            count[i] -= 1
    return nums
nums = [1, 0, 1, 1, 0, 0, 1]
print(sort(nums))
#output-[0, 0, 0, 1, 1, 1, 1]
#time complexity-o(n)
#space complexity-o(1)
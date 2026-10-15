def sum_of_1d_array(nums):
    n= len(nums)
    summ=0
    for i in range(n):
        summ=nums[i]+summ
    return summ
nums=[1,2,3,4,5]
print(sum_of_1d_array(nums))
#time complexity-o(n)  the execution time of an algorithm grows as the input size n grows
#space complexity -o(1)  the memory required by an algorithm grows as the input size grows
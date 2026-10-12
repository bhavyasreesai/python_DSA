# 3 question
def single_number(nums):
    n=len(nums)
    result=0
    for i in range(n):
        result= result^nums[i]# ^ is for XOR
    return result
nums=[4,1,2,1,2]
print(single_number(nums))

#Time complexity - o(n)
#space complexity - o(1)
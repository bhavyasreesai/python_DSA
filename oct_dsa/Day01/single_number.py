# 3 question
def single_number(nums):
    n=len(nums)
    result=0
    for i in range(n):
        result= result^nums[i]# ^ is for XOR
    return result
nums=[4,1,2,1,2,4]
print(single_number(nums))

#Time complexity - o(n)
#space complexity - o(1)

#optimal solution
def num(nums):
    n=len(nums)
    dict={}
    for i in range(n):
        if nums[i] in dict:
            dict[nums[i]]+=1
        else:
            dict[nums[i]]=1
    for key in dict:
        if dict[key]==1:
            return key

nums=[4,1,2,1,2]
print(num(nums))
#output-4
#time complexity-o(n)
#space complexity-o(1)


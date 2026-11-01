def count_frequencies_of_array(nums):
    count={}
    n=len(nums)
    for i in range(n):
        if nums[i] in count:
            count[nums[i]]+=1
        else:
            count[nums[i]]=1
    return count
nums=[1,2,2,3,1,4,2,2]
result=count_frequencies_of_array(nums)
for i in result:
    print(i,"occurs",result[i],"times")
    #time complexity-o(n)
    #space complexity-o(n)
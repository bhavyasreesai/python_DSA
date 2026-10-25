def contains_duplicates(nums,k):
    n=len(nums)
    dicti={}
    for i in range(n):
        if nums[i] in dicti and i-dicti[nums[i]]<=k:
            return True
        dicti[nums[i]]=i

    return False
nums = [1, 2, 3, 1]
k = 3
print(contains_duplicates(nums,k))

#output-True
#time complexity-o(n)
#space complexity-o(n)


#########
#nums = [10, 20, 30]
#window = {10: 0, 20: 1, 30: 2}
#i = 1
#print(nums[i])
#print(window[nums[i]])
##########

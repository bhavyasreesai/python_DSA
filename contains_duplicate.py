# 2 question
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def contains_duplicate(nums):
    n=len(nums)
    for i in range(n) : #start 0, stop at n
        for j in range(i+1,n):# start at i+1, stop at n
           if nums[i]==nums[j] : #if element in index  i and j are same print true
            return True
    return False
nums=[1,2,3,3]
print(contains_duplicate(nums))

# time complexity-o(n^2) as only two loop
# space complexity - o(1) we have fixed variables only
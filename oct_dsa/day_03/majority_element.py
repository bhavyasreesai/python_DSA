#Given an array nums of size n, return the majority element.

#The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.
def majority_element(nums):
    n=len(nums)
    count={} #creating empty dictionary
    for num in nums:
        if num in count:
            count[num]+=1 #if number is already in dictionary,increase its count by 1
        else :
            count[num]=1 #otherwise , add to dictionary with a count of 1
        if count[num]>n//2: #number count should be half of length of array
            return num
nums=[2,2,1,1,1,2,2]
print(majority_element(nums))

#time complexity-o(n)
# space complexity=(n)
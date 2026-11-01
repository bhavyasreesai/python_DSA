def max_in_array(nums):
    n=len(nums) # length of array
    maxi=nums[0] # let's say 1st element (index 0 )is maximum element
    for i in range(1,n): # since index 0 is maximum we will start loop from 1 and end at n
            if nums[i]>maxi: #if the nums[i] is greater than the maxi
                 maxi=nums[i] #replace maxi with nums[i]
    return maxi                 # now return the maxi

nums=[10,73,23,89,100,102]
print(max_in_array(nums))

# here in loop - for i in range(1,n):
# if we remove 1 and write - for i in range(n):
# there will be no change because
# if we take 1 , it will start with 73 because 10 is in maxi
# if we not write 1 , it will start with 10 (index 0 , default)
# it will take iteration with 10, it will check 10 > 10(maxi) - false
# and continues normally
# complexity doesn't affect comparisons will be less
# slightly more efficient
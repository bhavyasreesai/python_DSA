


def move_zeros(nums,self):
    n=len(nums)
    self=0
    for i in range(n):
        if nums[i]!=0:
            nums[self]=nums[i]
            self+=1
    while self<n:
            nums[self]=0
            self+=1
    return nums
nums=[0,1,0,3,12]
print(move_zeros(nums,0))

#output:
#[1,3,12,0,0]

#time complexity-o(n)
#space complexity-o(1)


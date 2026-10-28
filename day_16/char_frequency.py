def sort(nums):
    n=len(nums)
    freq={}
    for i in range(n):
        ch=nums[i]
        if ch not in freq:
            freq[ch]=0
        freq[ch]+=1
        i+=1
    return freq
    keys=list(freq.keys())
    for i in range(len(keys)-1):
        max_pos=i
        for j in range(i+1,len(keys)):
            if freq[keys[j]]>freq[keys[max_pos]]:
                max_pos=j
        temp=keys[i]
        keys[i]=keys[max_pos]
        keys[max_pos]=temp
    return keys
nums=[2,5,3,6,3,2,6,1,5,1]
print (sort(nums))
#output-{2: 2, 5: 2, 3: 2, 6: 2, 1: 2}
#time complexity-o(n)
#space complexity-o(n)

#output-[2, 5, 3, 6, 1]
#time complexity-o(n^2)
#space complexity-o(n)
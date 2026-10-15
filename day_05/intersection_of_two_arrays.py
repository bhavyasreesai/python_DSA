def intersection_of_two_arrays(num1,num2):
    n=len(num1)
    m=len(num2)
    result=[]
    for i in range(n):
        for j in range(m):
            if num1[i]==num2[j]:
                if num1[i] not in result:
                    result = result+[num1[i]]
                break
    return result
num1=[1,2,2,3,4]
num2=[2,3,5,4]
print(intersection_of_two_arrays(num1,num2))
# time complexity-o(n*m*k)
# n = length of num1
# m = length of num2
#k = number of unique common elements in result

# space complexity-o(k)
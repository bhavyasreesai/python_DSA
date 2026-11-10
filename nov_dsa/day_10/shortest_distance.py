#brute force
def shortestToChar(s, c):
    result = []
    for i in range(len(s)):
        min_dist=len(s)
        for j in range(len(s)):
            if s[j]==c:
                dist=abs(i- j)
                if dist<min_dist:
                    min_dist=dist
        result.append(min_dist)
    return result
s = "loveleetcode"
c = "e"
print(shortestToChar(s, c))
#output-[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#time complexity-(n^2)
#space complexity-o(n)

#optimal
def shortestToChar(s, c):
    result = []
    prev = -len(s)

    for i in range(len(s)):
        if s[i]==c:
            prev=i
        result.append(i-prev)
    prev=2*len(s)
    for i in range(len(s)-1,-1,-1):
        if s[i]==c:
            prev=i
        if prev-i<result[i]:
            result[i]=prev-i
    return result
s = "loveleetcode"
c = "e"
print(shortestToChar(s, c))
#output-[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#time complexity-(n)
#space complexity-o(n)
#brute force
def code(s,goal):
    n=len(s)
    m=len(goal)
    if n!=m:
        return False
    for i in range(n):
        rotate=""
        for j in range(n):
            rotate+=s[(i+j)%n]
            if rotate==goal:
                return True
    return False
s="abcde"
goal="cdeab"
print(code(s,goal))
#output-True
#time complexity-o(n^2)
#space complexity-o(1)
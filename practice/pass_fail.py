def check(nums):

    if nums>=str(75):
        return "dis"
    elif nums >=str(50):
        return "pass"
    else:
        return "fail"
nums=(input("value"))
print(check(nums))
def count_inversions(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count
arr = [2, 4, 1, 3, 5]
print(count_inversions(arr))
#output-3
#time complexity-o(n^2)
#space complexity-o(1)
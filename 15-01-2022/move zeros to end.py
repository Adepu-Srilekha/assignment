'''n = nums.count(0)
for i in range(n):
    nums.remove(0)
    nums.append(0)
nums=[1,2,3,4,0,6,9]

'''
def pushZerosToEnd(arr, n):
    count = 0
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1



arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)
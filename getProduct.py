def multiplyList(arr, n):
 
    # Base case
    if(n == 1):
        print(0)
        return
 
    # Set a temporary memory space for the two arrays
    left = [0]*n
    right = [0]*n
 
    # Set a temporaru memory space for the two products
    prod = [0]*n
 
    # Left most element of left array is always 1
    left[0] = 1
 
    # Right most element of right array is always 1
    right[n - 1] = 1
 
    # Construct the left array
    for i in range(1, n):
        left[i] = arr[i - 1] * left[i - 1]
 
    # Construct the right array
    for j in range(n-2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]
 
    # Construct the product array using
    # left[] and right[]
    for i in range(n):
        prod[i] = left[i] * right[i]
 
    # print the constructed prod array
    for i in range(n):
        print(prod[i], end=' ')


list = [2, 4, 7, 8, 9]
n = len(list)
print("The product of the array is...")
multiplyList(list,n)

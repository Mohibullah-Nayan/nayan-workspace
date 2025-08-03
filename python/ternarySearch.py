def ternarySearch(arr, N, K):
    low = 0
    high = N - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if arr[mid1] == K:
            return 1
        if arr[mid2] == K:
            return 1

        if K < arr[mid1]:
            high = mid1 - 1
        elif K > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1

    return -1
print(ternarySearch([1,2,3,4,6], 5, 6))
print(ternarySearch([1,3,4,5,6], 5, 2))
print(ternarySearch([2, 8], 2, 1))



def getFloorAndCeil(a, n, x):

    def findFloor(arr, n, x):
        low = 0
        high = n - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            # maybe an answer
            if arr[mid] <= x:
                ans = arr[mid]
                # look for smaller index on the left
                low = mid + 1
            else:
                high = mid - 1  # look on the right

        return ans
    
    def findCeil(arr, n, x):
        low = 0
        high = n - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            # maybe an answer
            if arr[mid] >= x:
                ans = arr[mid]
                # look for smaller index on the left
                high = mid - 1
            else:
                low = mid + 1  # look on the right

        return ans
    
    f = findFloor(a, n, x)
    c = findCeil(a, n, x)
    return (f, c)



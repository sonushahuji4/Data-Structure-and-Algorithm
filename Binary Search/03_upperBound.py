def upperBound(arr: [int], x: int, n: int) -> int:
    
    def getUpperBound(low, high, target):
        low, high = 0, n-1
        index = n
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] > target:
                index = mid
                high = mid - 1
            else:
                low = mid + 1
        return index
    return getUpperBound(0, n, x)

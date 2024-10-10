def lowerBound(arr: [int], n: int, x: int) -> int:
    def getLowerBound(low,high,target,n):
        low, high = 0, n - 1
        index = n
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] >= target:
                index = mid
                high = mid - 1
            else:
                low = mid +  1
        return index
    return getLowerBound(0, n, x, n)


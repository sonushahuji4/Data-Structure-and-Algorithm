def NthRoot(n: int, m: int) -> int:
    low, high = 1, m
    while low <= high:
        mid = low + (high - low) // 2
        NthSqrRoot = mid ** n
        if NthSqrRoot == m: return mid
        if NthSqrRoot < m:
            low = mid + 1
        else:
            high = mid - 1
    return -1

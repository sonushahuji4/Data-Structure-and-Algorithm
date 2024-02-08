def floorSqrt(n):
  low, high = 1, n
  while low <= high:
    mid = low + (high - low) // 2
    sqrRoot = mid * mid
    if sqrRoot <= n:
        low = mid + 1
    else:
        high = mid - 1
  return high

n = int(input())
print(floorSqrt(n))

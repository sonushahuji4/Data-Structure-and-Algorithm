def count(arr: [int], n: int, x: int) -> int:
    def getFirstOccurs(low, high, target, nums):
        index = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return index
    
    def getLastOccurs(low, high, target, nums):
        index = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                hig = mid - 1
        return index
    
    ans1 = getFirstOccurs(0,n-1,x,arr)
    ans2 = getLastOccurs(0,n-1,x,arr)

    if ans1 == -1 or ans2 == -1: return 0
    return (ans2 - ans1) + 1

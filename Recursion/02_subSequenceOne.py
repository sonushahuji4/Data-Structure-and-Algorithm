nums = [3,1,2]
n = len(nums)
result = []

def subq(arr,i):
    if i >= n:
        result.append(arr)
        return 
    subq(arr + [nums[i]], i + 1)
    subq(arr, i + 1)
subq([], 0)
print(result)

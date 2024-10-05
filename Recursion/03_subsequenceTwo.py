# Print All subsquence while sum is equal to K

nums = [1,2,1]
n = len(nums)
result = []
def kSubqSum(arr,k,i):
    if i >= n:
        if k == 0:
            result.append(arr)
        return
    kSubqSum(arr + [nums[i]], k - nums[i], i + 1)
    kSubqSum(arr, k, i + 1)

k = 2
kSubqSum([],k,0)
print(result)
    

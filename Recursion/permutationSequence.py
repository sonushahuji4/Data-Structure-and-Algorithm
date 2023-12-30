nums = [1, 2, 3]
n = len(nums)
ans = []
freq = [False] * n

def getAllPermutationOfLenN(arr, freq):
    if len(arr) == n:
        ans.append(arr.copy())

    for i in range(n):
        if not freq[i]:
            freq[i] = True
            arr.append(nums[i])
            getAllPermutationOfLenN(arr, freq)
            freq[i] = False
            arr.pop()

getAllPermutationOfLenN([], freq)
return ans

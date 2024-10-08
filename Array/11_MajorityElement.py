# https://leetcode.com/problems/majority-element/description/

# Approach One

def majorityElement(arr):
    # Size of the given array
    n = len(arr)

    for i in range(n):
        # Selected element is arr[i]
        cnt = 0
        for j in range(n):
            # Counting the frequency of arr[i]
            if arr[j] == arr[i]:
                cnt += 1

        # Check if frequency is greater than n/2
        if cnt > (n // 2):
            return arr[i]

    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)

# Approach Two




from collections import Counter

def majorityElement(arr):
    # Size of the given array
    n = len(arr)

    # Count the occurrences of each element using Counter
    counter = Counter(arr)

    # Searching for the majority element
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
ans = majorityElement(arr)
print("The majority element is:", ans)


# Approach Three

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]

# Approach Four

from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        candidate = nums[0]
        for i in range(1,len(nums)):
            if count == 0:
                candidate = nums[i]
                
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1

        return candidate



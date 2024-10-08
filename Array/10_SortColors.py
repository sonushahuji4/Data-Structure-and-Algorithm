# https://leetcode.com/problems/sort-colors/description/

# Approach One

def sortColors(nums):
    count_0 = count_1 = count_2 = 0
    
    # Count the occurrences of 0, 1, and 2
    for num in nums:
        if num == 0:
            count_0 += 1
        elif num == 1:
            count_1 += 1
        else:
            count_2 += 1

    # Overwrite the array with the correct number of 0s, 1s, and 2s
    nums[:count_0] = [0] * count_0
    nums[count_0:count_0+count_1] = [1] * count_1
    nums[count_0+count_1:] = [2] * count_2

# Example usage
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]


# Approach Two

def sortColors(nums):
    n = len(nums)
    index = 0
    
    # First pass: move all 0's to the front
    for i in range(n):
        if nums[i] == 0:
            nums[i], nums[index] = nums[index], nums[i]
            index += 1
    
    # Second pass: move all 2's to the end
    index = n - 1
    for i in range(n - 1, -1, -1):
        if nums[i] == 2:
            nums[i], nums[index] = nums[index], nums[i]
            index -= 1

# Example usage
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]


# Approach Three

def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Example usage
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]


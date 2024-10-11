# https://leetcode.com/problems/3sum/description/

# Approach One
    n = len(nums)
    result = set()  # Using a set to avoid duplicates
    
    # Iterate through all triplet combinations
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    # Sort the triplet to avoid duplicates like [-1, 0, 1] and [0, -1, 1]
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)
    
    # Convert the set back to a list of lists
    return [list(triplet) for triplet in result]

# Approach Two

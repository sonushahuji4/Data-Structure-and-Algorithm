# https://leetcode.com/problems/longest-consecutive-sequence/description/

# Approach One

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def linearSearch(a, num):
            n = len(a)  # size of array
            for i in range(n):
                if a[i] == num:
                    return True
            return False

        def longestSuccessiveElements(a):
            n = len(a)  # size of array
            longest = 1
            # pick an element and search for its consecutive numbers
            for i in range(n):
                x = a[i]
                cnt = 1
                # search for consecutive numbers using linear search
                while linearSearch(a, x + 1):
                    x += 1
                    cnt += 1

                longest = max(longest, cnt)
            return longest
        
        if len(nums) == 0: return 0

        ans = longestSuccessiveElements(nums)
        return ans


# Approach Two

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Sort the array
        nums.sort()

        # Initialize the longest and current sequence lengths
        longest_sequence = 1
        current_sequence = 1

        # Traverse the sorted array
        for i in range(1, len(nums)):
            # If consecutive elements
            if nums[i] == nums[i - 1] + 1:
                current_sequence += 1
            # If the same element (ignore it)
            elif nums[i] != nums[i - 1]:
                # Update the longest sequence if needed
                longest_sequence = max(longest_sequence, current_sequence)
                current_sequence = 1

        # Final comparison to ensure the last sequence is considered
        longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence

# Approach Three

def longestConsecutive(nums):
    if not nums:
        return 0

    num_set = set(nums)  # Create a set for O(1) lookups
    longest_sequence = 0

    for num in num_set:
        # Only start counting if 'num' is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1

            # Continue the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1

            # Update the longest sequence found
            longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence

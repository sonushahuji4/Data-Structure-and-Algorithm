# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sLength = len(s)
        charTracker = defaultdict(int)
        lIndex = rIndex = longestSubstring = 0

        while rIndex < sLength:
            if s[rIndex] in charTracker and charTracker[s[rIndex]] >= lIndex:
                lIndex = charTracker[s[rIndex]] + 1
            longestSubstring = max(longestSubstring, rIndex - lIndex + 1)
            charTracker[s[rIndex]] = rIndex
            rIndex += 1

        return longestSubstring

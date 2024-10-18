# https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        # Approach One (Recursion)
        def isPredecessor(prevWord, currWord):
            lenPrev = len(prevWord)
            lenCurr = len(currWord)
            if lenPrev >= lenCurr or lenCurr - lenPrev != 1:
                return False

            # Check if prevWord can be formed by removing one character from currWord
            w1 = w2 = 0
            while w1 < lenPrev and w2 < lenCurr:
                if prevWord[w1] == currWord[w2]:
                    w1 += 1
                w2 += 1
            
            # If w1 reached the end of prevWord, that means currWord has one extra character
            return w1 == lenPrev

        def getLongestStrChain(index, prevIndex, n, sortedWords):
            if index == n:
                return 0

            pickWord = 0
            if prevIndex == -1 or isPredecessor(sortedWords[prevIndex], sortedWords[index]):
                pickWord = 1 + getLongestStrChain(index + 1, index, n, sortedWords)
            
            notPickWord = getLongestStrChain(index + 1, prevIndex, n, sortedWords)

            return max(pickWord, notPickWord)
        
        sortedWords = sorted(words, key=len)
        return getLongestStrChain(0, -1, len(sortedWords), sortedWords)

        # Approach Two (Recursion + Dp)
        sortedWords = sorted(words, key=len)
        n = len(sortedWords)
        dp = [[-1]*(n+1) for _ in range(n)]

        def isPredecessor(prevWord, currWord):
            lenPrev = len(prevWord)
            lenCurr = len(currWord)
            if lenPrev >= lenCurr or lenCurr - lenPrev != 1:
                return False

            # Check if prevWord can be formed by removing one character from currWord
            w1 = w2 = 0
            while w1 < lenPrev and w2 < lenCurr:
                if prevWord[w1] == currWord[w2]:
                    w1 += 1
                w2 += 1
            
            # If w1 reached the end of prevWord, that means currWord has one extra character
            return w1 == lenPrev


        def getLongestStrChain(index, prevIndex):
            if index == n: return 0

            if dp[index][prevIndex] != -1: return dp[index][prevIndex]
            pickWord = 0
            if prevIndex == -1 or isPredecessor(sortedWords[prevIndex], sortedWords[index]):
                pickWord = 1 + getLongestStrChain(index + 1, index)
            
            notPickWord = getLongestStrChain(index + 1, prevIndex)

            dp[index][prevIndex] = max(pickWord, notPickWord)
            return dp[index][prevIndex]
        

        return getLongestStrChain(0, -1)

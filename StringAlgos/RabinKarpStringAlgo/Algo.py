# Link : https://cp-algorithms.com/index.html

class RabinKarp:
    def __init__(self, pattern, text):
        self.pattern = pattern  # Stores the pattern string, to search for
        self.text = text  # Stores the text string, to search for the pattern
        self.lengthOfPattern = len(pattern)
        self.lengthOfText = len(text)
        self.primeBase = 31  # Represents the prime base used in hashing
        self.modulo = 10**9 + 9  # Represents the modulo value used in hashing
        self.primePowers = [1] * max(self.lengthOfPattern, self.lengthOfText)  # Precomputed powers of primeBase
        self.textHashes = [0] * (self.lengthOfText + 1)  # Hash values of prefixes of the text string
        self.patternHash = 0  # Hash value of the pattern string
        self.occurrences = []  # Stores the indices where matches are found

    def computePrimePowers(self):
        for i in range(1, len(self.primePowers)):
            self.primePowers[i] = (self.primePowers[i-1] * self.primeBase) % self.modulo
        
    def computeTextHashes(self):
        for i in range(self.lengthOfText):
            charIndex = ord(self.text[i]) - ord('a') + 1
            base = charIndex * self.primePowers[i]
            self.textHashes[i+1] = (self.textHashes[i] + base) % self.modulo

    def computePatternHash(self):
        for i in range(self.lengthOfPattern):
            charIndex = ord(self.pattern[i]) - ord('a') + 1
            base = charIndex * self.primePowers[i]
            self.patternHash = (self.patternHash + base) % self.modulo
        
    def checkMatch(self, i):
        currentTextHash = (self.textHashes[i + self.lengthOfPattern] + self.modulo - self.textHashes[i]) % self.modulo
        if currentTextHash == (self.patternHash * self.primePowers[i]) % self.modulo:
            return True
        return False
        
    def findOccurrences(self):
        self.computePrimePowers()
        self.computeTextHashes()
        self.computePatternHash()
        for i in range(self.lengthOfText - self.lengthOfPattern + 1):
            if self.checkMatch(i):
                self.occurrences.append(i)
        return self.occurrences

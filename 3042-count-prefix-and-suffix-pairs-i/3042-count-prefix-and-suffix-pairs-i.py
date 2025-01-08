class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            if str1 > str2:
                return False

            if str2[:len(str1)] == str1 and str2[-len(str1):] == str1:

                return True
            else:
                return False

        count = 0
        for i in range(len(words)):
            for j in range(len(words)):
                if i < j:
                    if isPrefixAndSuffix(words[i], words[j]):
                        count += 1
        
        return count
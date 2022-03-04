class Solution:
    def validPalindrome(self, s1: str) -> bool:
        if len(s1) == 0:
            return False
        if len(s1) == 1:
            return True

        if s1 == s1[::-1]:
            return True

        i = 0
        j = len(s1) - 1

        while (i < j):
            if (s1[i] == s1[j]):
                i += 1
                j -= 1
            else:
                str1 = s1[:i] + s1[i + 1:]
                if self.isPallindrome(str1):
                    return True

                str2 = s1[:j] + s1[j + 1:]
                if self.isPallindrome(str2):
                    return True

                return False

    def isPallindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            return False
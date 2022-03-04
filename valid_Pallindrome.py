class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True

        s1 = "".join(filter(str.isalnum, s)).lower()
        x = s1[::-1]

        if (s1 == x):
            return True
        else:
            return False


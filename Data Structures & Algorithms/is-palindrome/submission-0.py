class Solution:
    def isPalindrome(self, s: str) -> bool:
        p= ''.join(c.lower() for c in s if c.isalnum())
        return p==p[::-1]
        
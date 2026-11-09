class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        h=len(s)-1
        def palindrome(l,r):
            while l<r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True
        while l<h:
            if s[l]==s[h]:
                l+=1
                h-=1
            else:
                return palindrome(l+1,h) or palindrome(l,h-1)
        return True
        
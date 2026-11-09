class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in s:
            i=i.lower()
            if i.isalnum():
                l.append(i)
        # print(l)
        return l==l[::-1]
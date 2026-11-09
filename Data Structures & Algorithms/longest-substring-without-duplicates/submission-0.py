class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ma=0
        left=0
        curr=0
        visited=set()
        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[left])
                left+=1
                curr-=1
            curr+=1
            visited.add(s[i])
            ma=max(ma,curr)
        return ma
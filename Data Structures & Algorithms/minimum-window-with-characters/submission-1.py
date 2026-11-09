from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s==t:
            return s
        elif len(s)<len(t):
            return ""
        else:
            need=Counter(t)
            left=0
            need_len=len(need)
            res=[]
            res_len=float('inf')
            window={}
            have=0
            for right in range(len(s)):
                char=s[right]
                window[char]=window.get(char,0)+1
                if char in need and window[char]==need[char]:
                    have+=1
                while have==need_len:
                    if right-left+1<res_len:
                        res=[left,right]
                        res_len=right-left+1
                    x=s[left]
                    window[x]-=1
                    if x in need and window[x]<need[x]:
                        have-=1
                    left+=1
            if res_len!=float('inf'):
                left,right=res
                return s[left:right+1]
            else:
                return ""
                    
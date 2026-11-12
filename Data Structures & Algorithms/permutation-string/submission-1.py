from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x=Counter(s1)
        window={}
        need=len(x)
        have=0
        res_len=len(s1)
        left=0
        for right in range(len(s2)):
            char=s2[right]
            window[char]=window.get(char,0)+1
            if char in x and window[char]==x[char]:
                have+=1
            while have==need:
                print(x,window)
                if right-left+1==len(s1):
                    return True
                y=s2[left]
                window[y]-=1
                if y in x and window[y]<x[y]:
                    have-=1
                left+=1
        return False

        
        
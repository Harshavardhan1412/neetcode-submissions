class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        maxlen=0
        maxf=0
        hashmap={}
        while r<len(s):
            if s[r] in hashmap:
                hashmap[s[r]]+=1
            else:
                hashmap[s[r]]=1
            maxf=max(maxf,hashmap[s[r]])
            if ((r-l+1)-maxf)>k:
                hashmap[s[l]]-=1
                maxf=0
                l+=1
            if ((r-l+1)-maxf)<=k:
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=""
        if len(strs)<=1:
            return strs[0]
        else:
            def check(a,b):
                res=""
                for i in range(min(len(a),len(b))):
                    if a[i]==b[i]:
                        res+=a[i]
                    else:
                        break
                return res
            pre=check(strs[0],strs[1])
            for i in range(2,len(strs)):
                pre=check(pre,strs[i])
            return pre

class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res+=i+'|'
        return res
    def decode(self, s: str) -> List[str]:
        l=list(s.split("|"))
        l.pop()
        return l

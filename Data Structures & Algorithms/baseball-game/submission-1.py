class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for i in operations:
            print(res)
            if i.isdigit():
                res.append(int(i))
            elif i=='+':
                res.append(res[-1]+res[-2])
            elif i=='D':
                res.append(res[-1]*2)
            elif i=='C':
                res.pop()
            else:
                i=int(i)
                res.append(i)
        return sum(res)
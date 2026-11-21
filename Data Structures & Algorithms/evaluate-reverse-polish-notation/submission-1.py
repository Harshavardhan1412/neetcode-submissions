class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        x=[]
        for i in tokens:
            if i not in ['+', '-', '*','/']:
                x.append(int(i))
            else:
                a=x.pop()
                b=x.pop()
                res=0
                if i=='+':
                    res=b+a
                elif i=='-':
                    res=b-a
                elif i=='*':
                    res=b*a
                else:
                    res=int(b/a)
                x.append(res)
        return int(x[0])
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if stack==[]:
                stack.append(i)
            else:
                if i=="[" or i=="(" or i=="{":
                    stack.append(i)
                elif i=='}' or i==']' or i==')':
                    if stack!=[]:
                        if (stack[-1]=='[' and i==']') or (stack[-1]=='(' and i==')') or (stack[-1]=='{' and i=='}'):
                            stack.pop(-1)
                        else:
                            return False
                    else:
                        return False
        if stack==[]:
            return True
        return not True
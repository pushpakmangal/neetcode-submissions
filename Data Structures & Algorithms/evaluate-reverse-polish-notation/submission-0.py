class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op=('+', '-', '*', '/')
        for ele in tokens:
            # print(ele, stack)
            if ele not in op:
                stack.append(int(ele))
            else:
                b,a=int(stack[-1]), int(stack[-2])
                stack.pop()
                stack.pop()
                if ele=='+':
                    val=a+b
                elif ele=='-':
                    val=a-b
                elif ele=='*':
                    val=a*b
                elif ele=='/':
                    val=int(a/b)
                stack.append(val)
        return stack[0]


        
'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.

python 有个牛逼的函数，就是eval()，可以给它一个运算表达式，直接给你求值。中缀表达式转正常表达式很简单了，直接用栈就行。

但是！！需要注意的是，python中的’/’负数除法和c语言不太一样。在python中，(-1)/2=-1，而在c语言中，(-1)/2=0。也就是c语言中，除法是向零取整，即舍弃小数点后的数。而在python中，是向下取整的。而这道题的oj是默认的c语言中的语法，所以需要在遇到’/’的时候注意一下。
'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '/' and int(a) * int(b) < 0:
                    res = eval('-' + '(' + '-' + a + '/' + b + ')')
                else:
                    res = eval(a + token + b)
                stack.append(str(res))
        return int(stack.pop())

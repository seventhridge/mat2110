"""
This does not work at all!
"""

def do_op(num, op, num2):
    if op == '+':
        return num + num2
    if op == '*':
        return num * num2


def solve(result, expression):
    if expression[0] == '(':
        return solve(result, expression[1:])
    elif expression[0] == ')':
        return result
    elif len(expression) > 1 and expression[1] != ')':
        # number operator expression
        return do_op(float(expression[0]), expression[1], solve(0, expression[2:]))
    else:  # number )
        return solve(float(expression[0]), expression[1:])


e = "( 1 + ( 2 * 3 ) + ( 4 + 5 ) )".split()
print(solve(0, e))

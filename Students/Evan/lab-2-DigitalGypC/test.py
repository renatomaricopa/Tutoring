import doctest
from stack_array import Stack


'''
    operator    precedence      associativity
    --------    ----------      -------------
    **          3 high           Right
    ^           3 high           Right
    *           2 medium         Left
    /           2 medium         Left
    +           1 low            Left
    −           1 low            Left
'''


def infix_to_postfix(input_str: str) -> str:
    operators = {'+', '-', '*', '/', '(', ')', '^'}
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '<<': 3, '>>': 3}

    stack_in = []
    out_postfix = ''

    # Process the expression from left-to-right
    # if operand push postfix
    # if operator push to stack_in
    for symbol in input_str:
        if symbol not in operators:
            out_postfix += symbol

        elif symbol == '(':
            stack_in.append('(')

        elif symbol == ')':

            while stack_in and stack_in[-1] != '(':
                out_postfix += stack_in.pop()

            stack_in.pop()

        else:

            while stack_in and stack_in[-1] != '(' and precedence[symbol] <= precedence[stack_in[-1]]:
                out_postfix += stack_in.pop()

            stack_in.append(symbol)

    while stack_in:
        out_postfix += stack_in.pop()

    return out_postfix







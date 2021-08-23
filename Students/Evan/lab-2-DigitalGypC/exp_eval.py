from stack_array import Stack

"""
Assignment: lab 2 & Project 2

Repository: CalPolyCPE/cpe202_project_2/Project-2
    file: exp_eval.py

Name: Evan Last

Cal Poly User: ebsahagu
"""

''' * Process the expression from left-to-right
    * When a value is encountered:
      * Push the value(numbers not operators) onto the stack
    * When an operator is encountered:
      * Pop the required number of values from the stack
      * Perform the operation
      * Push the result back onto the stack
    * Return the last value remaining on the stack '''

CAPACITY = 30
OPERATORS = ('+', '-', '*', '/', '**', '^', '>>', '<<')
ASSOCIATIVITY = {'+': 'l', '-': 'l', '*': 'l', '/': 'l', '^': 'r', '<<': 'l', '>>': 'l', '**': 'r'}
PRECEDENCE = {'+': 2, '-': 2, '*': 3, '/': 3, '^': 4, '**': 4, '<<': 1, '>>': 1}


# You do not need to change this class
class PostfixFormatException(Exception):
    pass


def perform_op(operator: str, num1: float, num2: float):
    """ performs the given operation on the two input numbers

    Args:
        operator: from OPERATORS
        num1 (float): some number
        num2 (float): some number

    Returns:
        float: the result of the operation
    """
    # depending on what operator is we need to do different things
    # i.e. if operator == '+': return num1 + num2
    # we basically need to do this for all the operators in OPERATOR
    if operator == '+':
        return num2 + num1
    elif operator == '-':
        return num2 - num1
    elif operator == '*':
        return num2 * num1
    elif operator == '/':
        return num2 / num1
    elif operator == '**':
        return num2 ** num1
    elif operator == '^':
        return num2 ** num1  # "^" this character does not work with int so **
    elif operator in ['<<', '>>']:
        # make sure we arent bit shifting using decimals
        if num1 != int(num1) or num2 != int(num2):
            raise ValueError(f"Bit-shifting using non-integer operands: {num2} {num1}")
        elif operator == '<<':
            return int(num2) << int(num1)
        elif operator == '>>':
            return int(num2) >> int(num1)


def postfix_eval(input_str: str) -> float:
    """ Returns:Evaluates a postfix expression

    Args:
        input_str: a string containing a postfix expression where tokens
        are space separated. Tokens are either operators + - * / ** >> << or numbers.

    Returns:
        float: the result of the expression evaluation
    Raises:
        PostfixFormatException: if the input is not well-formed
        DO NOT USE PYTHON'S EVAL FUNCTION!!!

    Examples:
        >>> postfix_eval("3 5 +")
        8
        >>> postfix_eval("blah")
        :raise PostfixFormatException("Invalid token"):
        >>> postfix_eval("4 +")
        :raise PostfixFormatException(): put something here
        >>> postfix_eval("1 2 3 +")
        "Too many operands"
    """

    '''Returns:Evaluates a postfix expression
    Input argument:  a string containing a postfix expression where tokens
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation.
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    # Functional Template (pseudocode)

    # Process the expression from left-to-right
    list_exp = input_str.split()  # i.e. [3, 5, +]; [2, 3, 6, +, *] -> [2, 9, *] -> [18]; [1 4 + 2] -> [5 2]
    my_stack = Stack(CAPACITY)

    for token in list_exp:
        # When a value is encountered:
        if token.isnumeric():
            # if the token is a number, cast as a float and push to the stack
            my_stack.push(float(token))
        elif token in OPERATORS:
            # “Insufficient operands” if the expression does not contain
            # if the token is an operator, apply the operation and push to the stack
            # “Too many operands” if the expression contains too many operands.
            try:  # what should happen
                num1 = my_stack.pop()
                num2 = my_stack.pop()
                my_operation = perform_op(token, num1, num2)
                my_stack.push(my_operation)
            except IndexError:
                raise PostfixFormatException("Insufficient operands")
        else:
            raise PostfixFormatException("Invalid token")
    if my_stack.size() > 1:
        raise PostfixFormatException("Too many operands")
    return my_stack.peek()


def infix_to_postfix(input_str) -> str:
    """ Converts an infix expression to an equivalent postfix expression

    Args:
        input_str: a string containing an infix expression where tokens are
        space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers

    Returns:
        String: containing a postfix expression


    """
    '''Converts an infix expression to an equivalent postfix expression

    Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
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

    stack_in = Stack(CAPACITY)
    out_postfix = []
    input_str = input_str.split()

    # Process the expression from left-to-right
    # if operand push postfix
    # if operator push to stack_in
    for symbol in input_str:
        # number
        if symbol.isnumeric():
            # append numbers to the expression
            out_postfix.append(symbol)
        # open paren
        elif symbol == '(':
            stack_in.push(symbol)
        # close paren
        # When you encounter a closing parenthesis:
        # Until the top of stack is an opening parenthesis, pop operators off the stack and append them to the
        # RPN expression
        elif symbol == ')':
            while stack_in.peek() != '(':
                out_postfix.append(stack_in.pop())
            # Pop the opening parenthesis from the stack (but don't put it into the RPN expression)
            stack_in.pop()
        # operator
        elif symbol in OPERATORS:
            # When you encounter an operator, symbol:
            # While there is an operator, o2, at the top of the stack and either
            # symbol is left-associative and its precedence is less than or equal to that of o2, or
            # symbol is right-associative, and has precedence less than that of o2
            while not stack_in.is_empty() and stack_in.peek() in OPERATORS \
                    and (ASSOCIATIVITY[symbol] == 'l' and PRECEDENCE[symbol] <= PRECEDENCE[stack_in.peek()]
                         or ASSOCIATIVITY[symbol] == 'r' and PRECEDENCE[symbol] < PRECEDENCE[stack_in.peek()]):
                out_postfix.append(stack_in.pop())
            stack_in.push(symbol)

        # Pop o2 from the stack and append it to the RPN expression
        # Finally, push o1 onto the stack
        # When you get to the end of the infix expression, pop (and append to the RPN expression)
        # all remaining operators

    while not stack_in.is_empty():
        out_postfix.append(stack_in.pop())
    return " ".join(out_postfix)

# Functional Template (pseudocode)


def prefix_to_postfix(input_str: str) -> float:
    """ Converts a prefix expression to an equivalent postfix expression

    Args:
        input_str: Tokens are either operators + - * / ** >> << parentheses ( ) or numbers

    Returns:
        str: containing a postfix expression(tokens are space separated)

    Examples:
        >>> prefix_to_postfix("* - 3 / 2 1 - / 4 5 6")
        "3 2 1 / - 4 5 / 6 - *"

    """
    '''Converts a prefix expression to an equivalent postfix expression
    
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)'''
    # Functional Template (pseudocode)
    input_str = input_str.split(" ")
    # Read the Prefix expression in reverse order (from right to left)
    input_str.reverse()

    operands = []
    # When an operand is encountered, push it onto the stack
    for symbol in input_str:

        if symbol in OPERATORS:

            # pop 2 elements from stack
            operand1 = operands.pop()
            operand2 = operands.pop()
            concat = operand1 + " " + operand2 + " " + symbol
            operands.append(concat)
        else:
            operands.append(symbol)

    postfix = operands.pop()
    return postfix


if __name__ == '__main__':
    import doctest
    doctest.testmod()

import numpy

class MyStack:
    # Constants
    MAX_CAPACITY = 100000
    DEFAULT_CAPACITY = 10

    # Initializer method
    def __init__(self, default_item, capacity=DEFAULT_CAPACITY):
        # If the capacity is bad, fail right away
        if not self.validate_capacity(capacity):
            raise ValueError("Capacity " + str(capacity) + " is invalid")
        self.capacity = capacity
        self.default_item = default_item
        # Make room in the stack and make sure it's empty to begin with
        self.clear()

    def clear(self):
        # Allocate the storage and initialize top of stack
        self.stack = numpy.empty(self.capacity)
        self.length = 0
        self.top_of_stack = 0
        #Array[:Array] = 0
        #self.stack = [self.default_item for _ in range(self.capacity)]
        #self.stack = [self.default_item for _ in range(self.capacity)]

    @classmethod
    def validate_capacity(cls, capacity):
        return 0 <= capacity <= cls.MAX_CAPACITY

    def push(self, item_to_push):
        if type(item_to_push) != int:
            raise TypeError("Push failed - wrong type, must be integer")
        if self.is_full():
            raise OverflowError("Push failed - capacity reached")
        self.stack[self.top_of_stack] = item_to_push
        self.top_of_stack += 1
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop failed - stack is empty")

        self.top_of_stack -= 1
        self.length -= 1
        return self.stack[self.top_of_stack]

    def is_empty(self):
        return self.top_of_stack == 0

    def is_full(self):
        return self.top_of_stack == self.capacity

    def get_capacity(self):
        return self.capacity


def mystack_test():
    # Instantiate two empty stacks, one of 50 ints, another of 15 strings
    s1 = MyStack(-1, 50)
    s2 = MyStack("undefined")
    # and one more with bad argument
    try:
        s3 = MyStack(None, -100)
        print("Failed test: expected __init()__ to reject negative capcity but it didn't")
    except Exception as e:
        print("Successful test: handled negative capacity: " + str(e))

    # Confirm the stack capacities
    print("------ Stack Sizes -------\n  s1: {}   s2: {}\n".
          format(s1.get_capacity(), s2.get_capacity()))

    # Pop empty stack
    print("------ Test stack ------\n")
    try:
        s1.pop()
        print("Failed test: expected pop() to raise empty-stack exception but it didn't")
    except Exception as e:
        print("Successful test: handled popping empty s1: " + str(e))

    # Push some items
    s1.push(44)
    s1.push(123)
    s1.push(99)
    s1.push(10)
    s1.push(1000)
    # try to put a square peg into a round hole
    try:
        s1.push("should not be allowed into an int stack")
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))
    try:
        s2.push(444)
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))
    try:
        s1.push(44.4)
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except Exception as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))
    # Push to s2
    try:
        s2.push("bank")
        print("Failed test: expected push() to reject due to type incompatibility but it didn't")
    except TypeError as e:
        print("Successful test: rejected due to type incompatibility: " + str(e))

    s2.push("-34")
    s2.push("should be okay")
    s2.push("a penny earned")
    s2.push("item #9277")
    s2.push("where am i?")
    s2.push("4")
    s2.push("4")
    s2.push("4")
    s2.push("4")
    try:
        s2.push("This is when stack is full")
        print("Failed test: expected push() to throw exception but it didn't")
    except Exception as e:
        print("Successful test: handled pushing when stack is full: " + str(e))
    print("\n--------- First Stack ---------\n")

    # Pop and inspect the items
    for k in range(0, 10):
        try:
            print("[" + str(s1.pop()) + "]")
        except Exception as e:
            print("Successful test: handled popping empty stack s1: " + str(e))
    print("\n--------- Second Stack ---------\n")
    for k in range(0, 10):
        print("[" + str(s2.pop()) + "]")

class RpnCalculator:

    def eval(rpn_expression):
        return RpnCalculator.parse(rpn_expression)

    def eval_tokens(tokens):
        stack = MyStack(tokens,len(tokens))
        valid_operators = ["+", "-", "*", "//"]
        for token in tokens:
            try:
                token = int(token)
                stack.push(token)
            except ValueError:
                if len(stack.stack) > 1 and token in valid_operators:
                    first_operand = stack.pop()
                    second_operand = stack.pop()
                    if token == "+":
                        stack.push(int(first_operand + second_operand))
                    elif token == "-":
                        stack.push(int(first_operand - second_operand))
                    elif token == "*":
                        stack.push(int(first_operand * second_operand))      #TEMP!, Add recursive multiply!
                    elif token == "//":
                        stack.push(int(first_operand // second_operand))
                else:
                    raise ValueError('Either length of stack is < 2, or invalid operator')
        if stack.length != 1:
            raise ValueError('Invalid length. Unable to minimize to one integer.')
        print(stack.stack)
        print("len: ",stack.length)
        return stack.pop()

    def parse(rpn_expression):
        tokens = rpn_expression.split(" ")
        return RpnCalculator.eval_tokens(tokens)

    def test_rpn():
        print(RpnCalculator.parse("3 2 + 6 - 124 +"))
        #print(RpnCalculator.eval("3 4 5"))

if __name__ == "__main__":
    #mystack_test()
    RpnCalculator.test_rpn()
class Person:
    def __init__(self, name):
        self.name = name
    def hello(self):
        class_name = self.__class__.__name__
        print("My name is {} and I am a {}".format(self.name, class_name))

tim = Person("tim")
tim.hello()
print(tim)
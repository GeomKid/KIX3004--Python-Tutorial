# Pass is used as a place holder for codes while developing. For example:
def developing_function():
    pass


# This is used when you develop some codes and plan to come back later to add more functionallity


# Another way of using is when inheriting a class and you want some functions to not do anything.
class ParentClass:
    def func_1(self):
        print("Hello")


class ChildClass(ParentClass):
    def func_1(self):
        pass


# This will cause the function of ChildClass to do nothing when func_! is called

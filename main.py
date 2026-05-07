class DunderMethods:
    def __init__(self):
        self.__dunder_methods = {
            "__init__": "Class constructor",
            "__del__": "Class destructor",
            "__str__": "String representation of an object",
            "__repr__": "String representation of an object for debugging",
            "__eq__": "Equality check between objects",
            "__ne__": "Inequality check between objects",
            "__lt__": "Less than check between objects",
            "__le__": "Less than or equal to check between objects",
            "__gt__": "Greater than check between objects",
            "__ge__": "Greater than or equal to check between objects",
            "__add__": "Addition operation between objects",
            "__sub__": "Subtraction operation between objects",
            "__mul__": "Multiplication operation between objects",
            "__truediv__": "Division operation between objects",
            "__floordiv__": "Floor division operation between objects",
            "__mod__": "Modulus operation between objects",
            "__pow__": "Power operation between objects",
            "__pos__": "Positive value of an object",
            "__neg__": "Negative value of an object",
            "__abs__": "Absolute value of an object",
            "__invert__": "Bitwise NOT operation on an object",
            "__lshift__": "Left shift operation on an object",
            "__rshift__": "Right shift operation on an object",
            "__and__": "Bitwise AND operation on an object",
            "__or__": "Bitwise OR operation on an object",
            "__xor__": "Bitwise XOR operation on an object",
            "__nonzero__": "Boolean value of an object",
            "__len__": "Length of an object",
            "__getitem__": "Get item from an object",
            "__setitem__": "Set item in an object",
            "__delitem__": "Delete item from an object",
            "__iter__": "Iterator of an object",
            "__next__": "Next item in an iterator",
            "__contains__": "Check if an item is in an object",
            "__call__": "Call an object as a function",
            "__getattr__": "Get attribute from an object",
            "__setattr__": "Set attribute in an object",
            "__delattr__": "Delete attribute from an object",
            "__dir__": "Directory of an object",
            "__getattribute__": "Get attribute from an object",
            "__hash__": "Hash value of an object",
        }

    def get_dunder_methods(self):
        return self.__dunder_methods


class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass({self.value})"

    def __repr__(self):
        return f"MyClass({self.value})"

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value

    def __floordiv__(self, other):
        return self.value // other.value

    def __mod__(self, other):
        return self.value % other.value

    def __pow__(self, other):
        return self.value ** other.value


obj1 = MyClass(10)
obj2 = MyClass(20)

print(obj1)  # MyClass(10)
print(repr(obj1))  # MyClass(10)
print(obj1 == obj2)  # False
print(obj1 != obj2)  # True
print(obj1 < obj2)  # True
print(obj1 <= obj2)  # True
print(obj1 > obj2)  # False
print(obj1 >= obj2)  # False
print(obj1 + obj2)  # 30
print(obj1 - obj2)  # -10
print(obj1 * obj2)  # 200
print(obj1 / obj2)  # 0.5
print(obj1 // obj2)  # 0
print(obj1 % obj2)  # 10
print(obj1 ** obj2)  # 10000000000

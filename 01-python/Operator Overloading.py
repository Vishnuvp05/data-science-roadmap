"""
Operator overloading means that the same operator can behave differently
for different data types.

Python does this using special methods called magic methods (also called
Dunder methods). These methods have names like __add__, __sub__, __mul__,
and __eq__.

How Python uses them:
- 5 + 3 -> Python calls int.__add__(5, 3) and gives 8
- "Hello" + " World" -> Python calls str.__add__("Hello", " World") and gives "Hello World"
- "Hi" * 3 -> Python calls str.__mul__("Hi", 3) and gives "HiHiHi"

So, the operator + does not always mean the same thing. It depends on the
object type. With our own class, we can define what +, -, *, and == should do.

This example shows how to do that with a custom Vector class.
"""


class Vector:
    """A simple 2D vector class to demonstrate operator overloading."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Add two vectors together using the + operator."""
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Subtract one vector from another using the - operator."""
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Multiply a vector by a scalar using the * operator."""
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        """Support scalar * vector as well."""
        return self.__mul__(scalar)

    def __eq__(self, other):
        """Compare two vectors using the == operator."""
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __repr__(self):
        """Return a readable string representation of the vector."""
        return f"Vector({self.x}, {self.y})"


if __name__ == "__main__":
    print("Built-in examples of operator overloading:")
    print("5 + 3 =", 5 + 3)
    print('"Hello" + " World" =', "Hello" + " World")

    print("\nCustom class example:")
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)

    print("v1:", v1)
    print("v2:", v2)

    print("v1 + v2 =", v1 + v2)
    print("v2 - v1 =", v2 - v1)
    print("v1 * 3 =", v1 * 3)
    print("4 * v2 =", 4 * v2)

    print("v1 == Vector(1, 2)?", v1 == Vector(1, 2))
    print("v1 == v2?", v1 == v2)


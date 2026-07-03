class Vector:
    """
    A simple 2D vector class to demonstrate operator overloading.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Overload the + operator
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # Overload the - operator
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        # Overload the * operator for scalar multiplication
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        # Support scalar * vector as well
        return self.__mul__(scalar)

    def __eq__(self, other):
        # Overload the == operator
        return isinstance(other, Vector) and self.x == other.x and self.y == other.y

    def __repr__(self):
        # String representation for debugging
        return f"Vector({self.x}, {self.y})"


if __name__ == "__main__":
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
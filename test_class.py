class Frog:
    def __init__(self, name):
        self.name = name


frog1 = Frog("Tony")
frog2 = Frog("Claudia")


print(frog1)
print(frog2)

# example of __repr__


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point(x=%s, y=%s)' % (self.x, self.y)


point = Point(1, 4)

print(point)

# the property Keyword


class Color:
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self.name = name

    def _set_name(self, name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name
    name = property(_get_name, _set_name)


c = Color("#0000ff", "blue")

print(c.name)

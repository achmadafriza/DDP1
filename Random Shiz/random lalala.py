class a:
    def __init__(self):
        self.number = 1
        self.character = 'a'

    def __add__(self, other):
        return self.number + other.number

    def __str__(self):
        return self.character


class b:
    def __init__(self):
        self.number = 2
        self.character = 'b'

    def __add__(self, other):
        return self.number + other.number

    def __str__(self):
        return self.character



myA = a
myB = b

print(myA)
print(myB)
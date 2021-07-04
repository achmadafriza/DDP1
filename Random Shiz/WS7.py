def myFunction(number1=0, number2=50):
    print("In myFunction:")
    print("Before exchange: ", number1, number2)
    number1, number2 = number2, number1
    print("After exchange: ", number1, number2)


def main():
    number1 = 12
    number2 = 25
    myFunction(number1, number2)
    print("In main: ", number1, number2)
    myFunction(number1)
    print("In main: ", number1, number2)
    myFunction()
    print("In main: ", number1, number2)
    myFunction(number2 = number1, number1 = number2)
    print("In main: ", number1, number2)
    x = (2, 3)
    myFunction(*x)
    myFunction(x)

class MyClass(object):
    def __init__(self):
        self.local_list = []
        self.sum_int = 0

    def method1(self, param):
        for element in param:
            if element > 10:
                self.local_list.append(element)

    def method2(self):
        for element in self.local_list:
            self.sum_int += element
        return self.sum_int

def funcMyClass():
    inst1 = MyClass()
    inst2 = MyClass()
    inst1.method1([1, 2, 3])
    print(inst1.local_list)
    inst1.method1([10, 11, 12])
    print(inst1.local_list)
    print(inst1.method2())
    x = inst2.method2()
    print(x)

class NewClass:
    def __init__(self, param_int):
        print("Calling __init__")
        self.the_int = param_int
        if param_int%2 == 0:
            self.parity = 'even'
        else:
            self.parity = 'odd'

    def process(self, instance):
        sum_int = self.the_int + instance.the_int
        if sum_int < 0:
            return 'negative'
        elif sum_int%2 == 0:
            return 'even'
        else:
            return 'odd'

    def __str__(self):
        print("Calling __str__")
        return 'Value {} is {}'.format(self.the_int, self.parity)
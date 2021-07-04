def findMax(a):
    if len(a) == 1:
        return a[0]
    elif a[0] < a[1]:
        return findMax(a[1:])
    else:
        return findMax([a[0]] + a[2:])

print(findMax([1,2,3,4,5,6,10,2]))

#
# def fb():
#     first, second = 0,1
#     while True:
#         yield first
#         first, second = second

class bonbin:
    def __init__(self):
        self.isi = ['anjing', 'tai', 'babi', 'bangsat']
    def __iter__(self):
        self.i = 0
        print("iterating")
        return self
    def __next__(self):
        if self.i < len(self.isi):
            temp = self.isi[self.i]
            self.i += 1
            return temp
        else:
            self.i = 1
            return self.isi[0]
    def printisi(self):
        print(self.isi)

class A:
    def __init__(self):
        print("making class A")
        self.isi = 'A lala'

    def __cetak(self):
        print("printing from A")

    def getCetak(self):
        self.__cetak()

class B(A):
    def __init__(self):
        global temp
        temp = 12312513
        print("making class B", temp)
        super().__init__()

    def __cetak(self):
        print("printing cetak from B")

    def getCetak(self):
        self.__cetak()
        global temp
        print(temp)

    def ngeprint(self):
        print("printing from B")

def sumString(s):
    if not s:
        return 0
    if ord('0') <= ord(s[0]) <= ord('9'):
        return int(s[0]) + sumString(s[1:])

    return sumString(s[1:])

def createIntList(a):
    if not a:
        return []
    elif isinstance(a, int):
        return [a]
    elif isinstance(a, list):
        return createIntList(a[0]) + createIntList(a[1:])
    else:
        return createIntList(a[1:])

# [2,4, [1,2]]
# f(2) + f([4, [1,2]])
# [2] + [4] + f([[1,2]])
# [2] + [4] + f([1,2]) + []

def translate(s):
    word = ""
    temp = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    for i in range(len(s)):
        if s[i].isalpha():
            for k in range(len(temp)):
                if s[i].lower() in temp[k]:
                    # word = word[:i] + str(k) + word[i+1:]
                    word += str(k)
                    break
        else:
            word += s[i].lower()

    return word

amira = 1
for i in range(10):
    amira *= 2
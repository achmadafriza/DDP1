
def numOnes(n): return (n%2 + numOnes(n//2)) if n != 0 else 0

def countneg(a): return ((a[0] < 0) + countneg(a[1:])) if a else 0
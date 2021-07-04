
ans = {}
for i in range(10, 115):
    temp = []
    for a in range(1, 31):
        for b in range(a+1, 31):
            for c in range(b+1, 31):
                for d in range(c+1, 31):
                    if not (a == b or a == c or a == d or b == c or b == d or c == d):
                        if (a+b+c+d) == i:
                            temp.append((a, b, c, d))
    ans[i] = temp

for i, j in ans.items():
    print(f"i = {i}")
    for k in j:
        print(k)
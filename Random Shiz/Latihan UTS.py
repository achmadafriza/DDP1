from pandas import bdate_range


def k_sum_pairs1(a, sum):
    ans = []
    for i in a:
        for k in a:
            if (i + k) == sum:
                ans.append((i, k))
    return ans

def find_modus(a):
    ans, ans_sum, max = [], [], a[0]
    for i in a:
        if i in ans:
            ans_sum[ans.index(i)] += 1
        else:
            ans.append(i)
            ans_sum.append(1)

        if ans_sum[ans.index(i)] >= ans_sum[ans.index(max)]:
            max = i

    return max

def k_sum_pairs(a, k):
    s = set()
    ans = []
    for i in a:
        temp = k - i
        if temp in s:
            ans.append((i, temp))
        s.add(i)
    return ans

def max_cap(s):
    ans = -1
    for i in s:
        if ord(i) >= ans and 'A' <= i <= 'Z':
            ans = ord(i)

    if ans != -1:
        return chr(ans)
    else:
        return None

"""
    for i in range(1, 50, 3):
    if i%7 == 1:
        print(i-1)
"""

k_sum_pairs([-4, 5, -2, 7], 3)
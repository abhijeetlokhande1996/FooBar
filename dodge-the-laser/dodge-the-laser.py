import math
import time


def main(alpha, n, ans):
    if n == 0 or n == 1:
        return n
    nDash = int((alpha - 1) * n)
    firstTerm = math.floor((n * nDash)) + math.floor(((n * (n + 1)) / 2))
    secondTerm = math.floor(nDash * (nDash + 1) / 2)
    ans += firstTerm - secondTerm
    minusFactor = math.floor(main(alpha, nDash, 0))
    ans -= minusFactor
    return math.floor(ans)


def solution(str_n):
    n = str_n
    alpha = math.sqrt(2)
    ans = main(alpha, n, 0)
    return str(ans)


s = time.time()
ans = solution(10)
print(ans)
e = time.time()
print(e-s)

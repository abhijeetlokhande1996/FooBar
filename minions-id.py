import math

def generatePrimeNumberString(upperLimit):
    primeNumberString = "2"
    for num in range(3, upperLimit + 1, 2):
        flag = True
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i != 0:
                flag = flag and True
            else:
                flag = flag and False
                break
        if flag:
            primeNumberString += str(num)
    return primeNumberString



def solution(i):
    primeNumberString = generatePrimeNumberString(10000)
    return primeNumberString[i:i+5]


ans = solution(3)
print(ans)

from math import gcd


def phi(n):
    result = 1
    for i in range(2, n):
        if(gcd(i, n) == 1):
            result += 1
    return result


def euler_method():
    n = int(input("Введіть число: "))
    print("Результат виконання функції: ", phi(n))

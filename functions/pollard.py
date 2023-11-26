def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def f(x, n):
    return (x * x + 3) % n


def pollard(a):
    x = 2
    y = 2
    d = 1
    while d == 1:
        x = f(x, a)
        y = f(f(y, a, ), a)
        d = gcd(abs(x - y), a)
        if 1 < d < a:
            return d
        if d == a:
            return -1


def pollard_method():
    n = int(input("Введіть число: "))
    print("Результат виконання функції: ", pollard(n))

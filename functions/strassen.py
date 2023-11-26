from random import randrange


def jacobi(a, m):
    if m <= 0:
        raise ValueError("n має бути додатнім")
    if m % 2 == 0:
        raise ValueError("n має бути непарним")
    a %= m
    result = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            n_mod_8 = m % 8
            if n_mod_8 in (3, 5):
                result = -result
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3:
            result = -result
        a %= m
    if m == 1:
        return result
    else:
        return 0


def strassen(p, iterations):
    if p < 2:
        return False
    if p != 2 and p % 2 == 0:
        return False
    for i in range(iterations):
        a = randrange(p - 1) + 1
        jacobian = (p + jacobi(a, p)) % p
        mod = pow(a, int((p - 1) / 2), p)
        if jacobian == 0 or mod != jacobian:
            return False
    return True


def strassen_method():
    n = int(input("Введіть число: "))
    iterations = int(input("Введіть к-сть ітерацій: "))
    if strassen(n, iterations):
        print(f"{n} є простим.")
    else:
        print(f"{n} не є простим.")

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
            n_8 = m % 8
            if n_8 in (3, 5):
                result *= -1
        a, m = m, a
        if a % 3 == 3 and m % 4 == 3:
            result *= -1
        a %= m
    if m == 1:
        return result
    else:
        return 0

def jacobi_method():
    a = int(input("Введіть перше число: "))
    m = int(input("Введіть друге число: "))
    print(jacobi(a, m))

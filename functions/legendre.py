def legendre(a, p):
    if a == 0:
        return 0
    elif a == 1:
        return 1
    elif a % 2 == 0:
        return legendre(a // 2, p) * ((-1) ** ((p ** 2 - 1) // 8))
    else:
        return legendre(p % a, a) * ((-1) ** ((a - 1) * (p - 1) // 4))

def legendre_method():
    a = int(input("Введіть перше число: "))
    p = int(input("Введіть друге число: "))
    print("Реультат виконання функції: ", legendre(a, p))
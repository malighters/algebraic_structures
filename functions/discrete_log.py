def discrete_log(g, y, p):
    m = int(p ** 0.5) + 1

    baby_steps = {pow(g, j, p): j for j in range(m)}

    gm_inv = pow(g, -m, p)
    giant_step = y
    for i in range(m):
        if giant_step in baby_steps:
            return i * m + baby_steps[giant_step]
        giant_step = (giant_step * gm_inv) % p

    return None


def babystep_giantstep_method():
    print("a = b^x mod m")
    a = int(input("Введіть a: "))
    b = int(input("Введіть b: "))
    m = int(input("Введіть m: "))

    print("x = ", discrete_log(a, b, m))

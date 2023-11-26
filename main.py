from functions.euler import euler_method
from functions.mobius import mobius_method
from functions.legendre import legendre_method
from functions.jacobi import jacobi_method
from functions.pollard import pollard_method
from functions.discrete_log import babystep_giantstep_method
from functions.strassen import strassen_method
from functions.el_gamal import elgamal_method


def main():
    print("Лабораторна робота з алгебраїчних структур.\n Виконав студент групи ТТП-32 Черненко Євгеній")
    print("""
        1. Обчислення функції Ейлера та Мьобіуса
        2. Обчислення символів Лежандра та Якобі
        3. Алгоритм факторизації: ро-алгоритм Полларда
        4. Алгоритм знаходження дискретного логарифму: алгоритм "великий крок - малий крок"
        5. Алгоритм перевірки числа на простоту: алгоритм Соловея-Штрассена
        6. Криптосистема Ель-Гамаля над еліптичними кривими
    """)

    while True:
        item = input("Введіть пункт меню:\n")
        match item:
            case "1":
                while True:
                    choice = input("1. Функція Ейлера\n"
                                   "2. Функція Мьобіуса\n"
                                   "0. Повернутись назад\n")

                    if choice == "1":
                        euler_method()
                        break
                    elif choice == "2":
                        mobius_method()
                        break
                    elif choice == "0":
                        break
                    else:
                        print("Неправльно введене число, будь ласка, спробуйте ще раз")

            case "2":
                while True:
                    choice = input("1. Функція Лежандра\n"
                                   "2. Функція Якобі\n"
                                   "0. Повернутись назад\n")

                    if choice == "1":
                        legendre_method()
                        break
                    elif choice == "2":
                        jacobi_method()
                        break
                    elif choice == "0":
                        break
                    else:
                        print("Неправльно введене число, будь ласка, спробуйте ще раз")

            case "3":
                pollard_method()

            case "4":
                babystep_giantstep_method()

            case "5":
                strassen_method()

            case "6":
                elgamal_method()

            case _:
                print("Неправльно введене число, будь ласка, спробуйте ще раз")


if __name__ == "__main__":
    main()

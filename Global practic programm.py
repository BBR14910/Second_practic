import sys

print("Введите что-нибудь")
choose_programm = 0
for i in sys.stdin:
    choose_programm = int(input("Введите целочисленное число для выбора программы (1 - найти скорость; "
                                "2 - найти массу; 3 -перевести фаренгейты в цельсии;"
                                "4 - найти работы; 5 - найти кинетическую энергию; 6 - найти потенциальную"
                                "энергию)"))

    if i == 'q\n':
        exit(0)

    if choose_programm == 1:
        long = float(input('Введите расстояние в км'))
        time = float(input('Введите время в часах'))
        print("Скорость = ", long/time, ' м/с')

    elif choose_programm == 2:
        Force = float(input("Введите силу в Н"))
        acceleration = float(input("Введите ускорение в м/с^2"))
        print("Масса = ", Force/acceleration, " кг")

    elif choose_programm == 3:
        Temperature_Farengeyt = float(input("Введите температуру в фаренгейтах"))
        print("Температура в цельсия = ", (Temperature_Farengeyt - 32)*5/9)

    elif choose_programm == 4:
        Force = float(input("Введите силу в Н"))
        long = float(input('Введите расстояние в м'))
        print("Работа = ", Force * long, ' Дж')

    elif choose_programm == 5:
        mass = float(input("Введите массу в кг"))
        speed = float(input('Введите скосроть в м/с'))
        print("Кинетическая энергия = ", mass * speed**2/2, ' Дж')

    elif choose_programm == 6:
        mass = float(input("Введите массу в кг"))
        acceleration_g = float(input("Введите ускорение свободного падения в м/с^2"))
        high = float(input('Введите высоту в км'))
        print("Потенциальная энергия энергия = ", mass * acceleration_g * high, ' Дж')

    print("Введите что-нибудь")

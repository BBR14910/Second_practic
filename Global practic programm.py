import sys

print("Введите что-нибудь")
choose_programm = 0
for i in sys.stdin:
    choose_programm = int(input("Введите целочисленное число для выбора программы (1 - найти скорость; 2 - найти массу)"))
    if i == 'q\n':
        exit(0)
    if choose_programm == 1:
        long = float(input('Введите расстояние в км'))
        time = float(input('Введите время в часах'))
        print("Скорость =", long/time, 'м/с')
    elif choose_programm == 2:
        Force = float(input("Введите силу в Н"))
        acceleration = float(input("Введите ускорение в м/с^2"))
        print("Масса =", Force/acceleration, "кг")

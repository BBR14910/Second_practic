import sys

print("Введите что-нибудь")
choose_programm = 0
for i in sys.stdin:
    choose_programm = int(input("Введите целочисленное число для выбора программы (1 - найти скорость)"))
    if i == 'q\n':
        exit(0)
    if choose_programm == 1:
        long = float(input('Введите расстояние в км'))
        time = float(input('Введите время в часах'))
        print("Скорость =", long/time)
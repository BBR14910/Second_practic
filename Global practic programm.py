import sys

for i in sys.stdin:
    choose_programm = int(input("Введите целочисленное число для выбора программы"))
    if i == 'q\n':
        exit(0)
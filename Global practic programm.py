import sys

print("Введите что-нибудь\n")
choose_programm = 0
for i in sys.stdin:
    choose_programm = int(input("Введите целочисленное число для выбора программы (1 - найти скорость; "
                                "2 - найти массу; 3 -перевести фаренгейты в цельсии;"
                                "4 - найти работы; 5 - найти кинетическую энергию; 6 - найти потенциальную"
                                "энергию; 7 - найти давление; 8 - найти теплоту; 9 - найти частоту) \n"))

    if i == 'q\n':
        exit(0)

    if choose_programm == 1:
        long = float(input('Введите расстояние в км\n'))
        time = float(input('Введите время в часах\n'))
        print("Скорость = ", long/time, ' км/с\n')

    elif choose_programm == 2:
        Force = float(input("Введите силу в Н\n"))
        acceleration = float(input("Введите ускорение в м/с^2\n"))
        print("Масса = ", Force/acceleration, " кг\n")

    elif choose_programm == 3:
        Temperature_Farengeyt = float(input("Введите температуру в фаренгейтах\n"))
        print("Температура в цельсия = ", (Temperature_Farengeyt - 32)*5/9, "\n")

    elif choose_programm == 4:
        Force = float(input("Введите силу в Н\n"))
        long = float(input('Введите расстояние в м\n'))
        print("Работа = ", Force * long, ' Дж\n')

    elif choose_programm == 5:
        mass = float(input("Введите массу в кг\n"))
        speed = float(input('Введите скосроть в м/с\n'))
        print("Кинетическая энергия = ", mass * speed**2/2, ' Дж\n')

    elif choose_programm == 6:
        mass = float(input("Введите массу в кг\n"))
        acceleration_g = float(input("Введите ускорение свободного падения в м/с^2\n"))
        high = float(input('Введите высоту в м\n'))
        print("Потенциальная энергия = ", mass * acceleration_g * high, ' Дж\n')

    elif choose_programm == 7:
        square = float(input("Введите площадь в м^2\n"))
        Force = float(input("Введите силу в Н\n"))
        print("Давление = ", Force/square, ' Па\n')

    elif choose_programm == 8:
        mass = float(input("Введите массу в кг\n"))
        latent_heat = float(input("Введите удльную теплоемкость в Дж/кг/цельсия\n"))
        change_temperature = float(input("Введите изменение температуры\n"))
        print("Теплота = ", mass * latent_heat * change_temperature, ' Дж\n')

    elif choose_programm == 9:
        T = float(input("Введите период колебаний в с\n"))
        print("Частота = ", 1/T, ' Гц\n')

    print("Введите что-нибудь\n")

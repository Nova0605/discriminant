import sys
import time
print("Решение квадратных уравнений")
while True:
    try:
        a = input("введите ax2: ")
        b = input("введите bx: ")
        c = input("введите  с: ")

        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        ()

    try:
        discr = b**2-4*a*c
    except TypeError:
        print("Разве в уравнениях можно писать буквы и другие символы в качестве переменных?")
        continue

    print('дискриминант = ' + str(discr))
    if discr < 0:
        print("нет корней, так как дискриминант меньше нуля")

    elif discr == 0:
        try:
            x = -b / (2 * a)
            print('x = ' + str(x))
        except ZeroDivisionError:
            print("А ты разве не знаешь, что делить на ноль нельзя?")

    else:
        try:
            x1 = (-b + discr ** 0.5) / (2 * a)
            x2 = (-b - discr ** 0.5) / (2 * a)
            print("x1 =" + str(x1))
            print("x2 =" + str(x2))
        except ZeroDivisionError:
            print("Делить на ноль нельзя?")



    contin_or_no = input("Продолжаем?(Напишите y или n): ")
    if contin_or_no.lower() == "n":
        print('все понял, вырублюсь через 1... 2...')
        time.sleep(2)
        sys.exit
        break
    if contin_or_no.lower() == "y":
        continue
    else:
        print("Я же просил нажать только Y или N...")
        print("давай попробуем еще раз...")
        contin_or_no1 = input("Продолжаем?(Напишите y или n): ")
        if contin_or_no1.lower() == 'n':
            print('все понял, вырублюсь через 1... 2...')
            time.sleep(2)
            sys.exit
            break
        if contin_or_no1.lower() == 'y':
            continue
        else:
            print("Вы вообще видите куда нажимаете?..")
()

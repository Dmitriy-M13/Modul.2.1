num_1 = int(input("введите 1-е число: "))
num_2 = int(input("введите 2-е число: "))
num_3 = int(input("введите 3-е число: "))

R = input("Выберите действие: \n"
               "1 - найти максимальное число\n"
               "2 - найти минимальное число\n"
               "3 - найти среднее арифметическое\n")

if R == "1":
    print("максиммальное значение: ", max(num_1, num_2, num_3))
elif R == "2":
    print(" минимальное значение: ", min(num_1, num_2, num_3))
elif R == "3":
    print("средне арифметическое: ", (num_1 + num_2 + num_3) // 3)
else:
    print("ошибка")
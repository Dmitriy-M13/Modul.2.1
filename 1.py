num_1 = int(input("введите 1-е число: "))
num_2 = int(input("введите 2-е число: "))
num_3 = int(input("введите 3-е число: "))

Z1 = num_1 + num_2 + num_3
Z2 = num_1 * num_2 * num_3

H = int(input("выберите: 1- сумма чисел\n          2- произведение чисел "))

if H == 1:
    print("сумма 3-х чисел: ", Z1)
elif H == 2:
    print("произведение чисел: ", Z2)
else:
    print("ошибка")
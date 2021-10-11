i = 0
def n(a):
    global i
    if a.isdigit():
        i = int(a)
    else:
        try:
            i = float(a)
        except ValueError:
            print('Ошибка')
    if i <= 0:
        print('Число не должно быть отрицательным и равным нулю')
flag = True
while flag:
    k = input('Введите натуральное число: ')
    n(k)
    if i == None or i < 0:
        flag = True
    else:
        if i <= 0 or type(i) == float:
            print('Только натуральные числа!!!')
        else:
            summa = i
            i = None
            flag = False
print(summa)

while summa > 0:
    if  summa > 0:
        n_500 = summa // 500  # Количество купюр по 500
        ostatok_n_500 = summa % 500  # Сумма от размена по 500
        print('Количество купюр по 500 рублей: ', n_500)
        print('Остаток', ostatok_n_500)
    
    if  ostatok_n_500 == 0:
        print('Конец')
        break

    if  summa < 500 or ostatok_n_500 > 0:
        n_200 = ostatok_n_500 // 200  # Количество купюр по 200
        ostatok_n_200 = ostatok_n_500 % 200  # Сумма от размена по 200
        print('Количество купюр по 200 рублей: ', n_200)
        print('Остаток', ostatok_n_200)
         
    if  ostatok_n_200 == 0:
        print('Конец')
        break

    if  summa < 200 or ostatok_n_200 > 0:
        n_100 = ostatok_n_200 // 100  # Количество купюр по 100
        ostatok_n_100 = ostatok_n_200 % 100  # Сумма, от размена 100
        print('Количество купюр по 100 рублей: ', n_100)
        print('Остаток', ostatok_n_100)
        
    if  ostatok_n_100 == 0:
        print('Конец')
        break

    if  summa < 100 or ostatok_n_100 > 0:
        n_10 = ostatok_n_100 // 10  # Количество монет по 10
        ostatok_n_10 = ostatok_n_100 % 10  # Сумма от размена по 10
        print('Количество монет по 10 рублей: ', n_10)
        print('Остаток', ostatok_n_10)
        
    if  ostatok_n_10 == 0:
        print('Конец')
        break
        
    if  summa < 10 or ostatok_n_10 > 0:
        n_5 = ostatok_n_10 // 5  # Количество монет 5
        ostatok_n_5 = ostatok_n_10 % 5  # Сумма от размена по 5
        print('Количество монет по 5 рублей: ', n_5)
        print('Остаток', ostatok_n_5)
        
    if  ostatok_n_5 == 0:
        print('Конец')
        break

    if  summa < 5 or ostatok_n_5 > 0:
        n_2 = ostatok_n_5 // 2   # Количество монет по 2
        ostatok_n_2 = ostatok_n_5 % 2   # Сумма от размена по 2
        print('Количество монет по 2 рубля', n_2)
        print('Остаток', ostatok_n_2)
        
    if  ostatok_n_2 == 0:
        print('Конец')
        break
    
    if  summa < 2 or ostatok_n_2 > 0:
        n_1 = ostatok_n_2 // 1  # Количество монет по 1
        ostatok_n_1 = ostatok_n_2 % 1   # Сумма от размена по 1
        print('Количество монет по 1 рублю', n_1)
        print('Остаток', ostatok_n_1)
        
    if  ostatok_n_1 == 0:
        print('Конец')
        break

    break        
        

# задание 1

#def ListToNumpy(arr):
#    x = len(arr)
#    y = len(arr[0])
#    numpy_array = [[0.0] * y for _ in range(x)]
#    for i in range(x):
#        for j in range(y):
#            numpy_array[i][j] = float(arr[i][j])
#    return numpy_array
#List = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#numpy_array = ListToNumpy(List)
#for row in numpy_array:
#    print(row)




# задание 2

#def get_s_and_razmer(arr):
#    def get_s(arr):
#        if isinstance(arr, list):
#            s = [len(arr)]
#            if s[0] > 0:
#                x, _ = get_s(arr[0])
#                s.extend(x)
#            return tuple(s), s[0]
#        return (), 1
#    def get_razmer(arr):
#        if isinstance(arr, list):
#            razmer = 0
#            for item in arr:
#                razmer += get_razmer(item)
#            return razmer
#        return 1
#    s = get_s(arr)
#    razmer = get_razmer(arr)
#    return s, razmer
#num_arrays = int(input("Введите количество массивов:"))
#all_arrays = []
#for i in range(num_arrays):
#    input_str = input(f"Введите массив {i + 1} (числа через пробел): ")
#    numbers = input_str.split()
#    numbers = [int(num) for num in numbers]
#    all_arrays.append(numbers)
#print("Все массивы:")
#print(all_arrays)
#s, razmer = get_s_and_razmer(all_arrays)
#print("Форма массива:", s)
#print("Размер массива:", razmer)



# задание 1

#import matplotlib.pyplot as plt
#import numpy as np
#x = np.linspace(-10, 10, 100)
#y = 6 * x - 2
#plt.plot(x, y, label='y = 6x - 2')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('График линейной функции y = 6x - 2')
#plt.legend()
#plt.grid(True)
#plt.axhline(0, color='black',linewidth=0.5)
#plt.axvline(0, color='black',linewidth=0.5)
#plt.show()




# задание 2

#import matplotlib.pyplot as plt
#import numpy as np
#x = np.linspace(-10, 10, 400)
#y1 = 6 * x**3 - 2 * x + 8
#y2 = 3 * x + 1
#plt.figure(figsize=(10, 5))
#plt.subplot(1, 2, 1)
#plt.plot(x, y1, label='F(x, y) = 6x^3 - 2x + 8')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('График функции F(x, y) = 6x^3 - 2x + 8')
#plt.legend()
#plt.subplot(1, 2, 2)
#plt.plot(x, y2, label='F(x, y) = 3x + 1')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.title('График функции F(x, y) = 3x + 1')
#plt.legend()
#plt.tight_layout()
#plt.show()



# задание 3

#import matplotlib.pyplot as plt
#products = ['помидоры', 'огурцы', 'тыква', 'свекла', 'редис', 'картофель']
#quantities = [100, 65, 12, 47, 89, 256]
#plt.bar(products, quantities)
#plt.xlabel('Продукты')
#plt.ylabel('Количество')
#plt.title('Столбчатая диаграмма данных о продуктах')
#plt.xticks(rotation=45)
#plt.show()



# задание 1

#Проверка, является ли 2027 год високосным:

#import calendar
#is_leap = calendar.isleap(2027)
#if is_leap:
#    print("2027 год високосный")
#else:
#    print("2027 год не високосный")




#Определение, каким днем недели был 25 июня 1995 года:

#import calendar
#day_of_week = calendar.weekday(1995, 6, 25)
#days = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
#print(f"25 июня 1995 года был {days[day_of_week]}")



#Вывод календаря на 2023 год:

#import calendar
#cal_2023 = calendar.TextCalendar(calendar.SUNDAY)
#print(cal_2023.formatyear(2023))

# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
n = int(input("Введите количество элементов "))
numbers = input('Введите элементы списка через пробел: ')
arr = list(map(int, numbers))
if n == len(numbers) or n == 0:
    x = int (input('Введите число х: '))
    a = 0
    for i in range(n):
        if arr[i] == x:
            a += 1
    print(f'Число {x} встречается в списке А {a} раз.')
else:
    print("Введенные количества не соответствуют! ")   





#  Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = int(input("Введите количество элементов "))
# numbers = input('Введите элементы списка через пробел: ')
# arr = list(map(int, numbers))
# a = 0
# if n == len(numbers) or n == 0:
#     x = int(input("Введите число "))
#     min = abs(x-arr[0])
#     for i in range(1,n):
#         cnt = abs(x-arr[i])
#         if cnt < min:
#             cnt = min
#             a=i
#     print(f'Число {arr[i]} в списке A наиболее близко по величине к числу {x}')       
# else:
#     print("Введенные количества не соответствуют! ")           

    

#  В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;
# K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# list= {1:"AEIOULNSTRАВЕИНОРСТ",
#        2:"DGДКЛМПУ",
#        3:"BCMPБГЁЬЯ",
#        4:"FHVWYЙЫ",
#        5:"KЖЗХЦЧ",
#        8:"JXШЭЮ",
#        10:"QZФЩЪ"}

# alphabet = input("Введите слово: ").upper()
# sum = 0
# for i in alphabet:
#     for k, v in list.items():
#         if i in v:
#             sum += k
# print(f"Количество баллов за введеное слово: {sum}")
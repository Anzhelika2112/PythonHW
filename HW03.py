# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.

# list_1 = [1, 2, 3, 4, 5]
# k = 3


# count_k = 0 
# for i in list_1: 
#     if i == k: count_k += 1 
# print(count_k)

# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# list_1 = [1, 2, 3, 4, 5]
# k = 6


# index_element = 0
# min_element = abs(k - list_1[0])
# for i in range(len(list_1)):
#     buffer_element = abs(k -list_1[i])
#     if buffer_element < min_element:
#         min_element = buffer_element
#         index_element = i

# print(list_1[index_element]) 

# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:

# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:

# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

# k = 'ноутбук'

# list_letters = {1:"aeioulnstrавеинорст",
#                 2:"dgдклмпу",
#                 3:"bcmpбгёья",
#                 4:"fhvwyйы",
#                 5:"kжзхцч",
#                 8:"jxшэю",
#                 10:"qzфщъ"}

# summ = 0
# for i in k:
#     for j, v in list_letters.items():
#         if i in v:
#             summ += j
# print(summ)
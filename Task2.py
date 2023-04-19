# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
# -> 9

size = int(input("Enter array size: "))
dif = 0
arr = [0]*size
min = 0
dif = 0
for i in range(size):
    arr[i] = int(input(f"Enter #{i+1} of array: "))
print()
el = int(input("Enter your number: "))

min = el - arr[0]
if min < 0:
    min*=-1

for j in arr:
    dif = el - j
    if dif < 0:
        dif*=-1
    if dif <= min:
        min = dif
        x = j
# print("")
print(f"Answer: {x}")

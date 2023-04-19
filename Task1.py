# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 3 2 3 7 5
# Ввод: 3
# -> 2

size = int(input("Enter array size: "))
count = 0

arr = [0]*size
for i in range(size):
    arr[i] = int(input(f"Enter #{i+1} of array: "))
print()
x = int(input("Enter number X: "))
for j in arr:
    if j == x:
        count+=1
print(arr[0])
print(f"Answer: {count}")

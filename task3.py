# # Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# # В случае с английским алфавитом очки распределяются так:
# # A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# # F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# # Д, К, Л, М, П, У – 2 очка;
# # Б, Г, Ё, Ь, Я – 3 очка;
# # Й, Ы – 4 очка;
# # Ж, З, Х, Ц, Ч – 5 очков;
# # Ш, Э, Ю – 8 очков;
# # Ф, Щ, Ъ – 10 очков.
# # Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово,
# # которое содержит либо только английские, либо только русские буквы.
# # ноутбук
# # 12
word = input("Enter your word: ")
summ=0
points = 0
scrabble = {"a1": "AEIOULNSTR", "a2": "DG", "a3": "BCMP", "a4": "FHVWY", "a5": "K", "a8": "JX", "a10":"QZ",
             "aa1":"АВЕИНОРСТ", "aa2":"ДКЛМПУ", "aa3": "БГЁЬЯ", "aa4":"ЙЫ", "aa5": "ЖЗХЦЧ", "aa8": "ШЭЮ", "aa10": "ФЩЪ"}
for key, value in scrabble.items():
    for i in word:
        for j in value:
            if i.lower() == j.lower():
                if key == "a1" or key == "aa1":
                    points= 1
                elif key == "a2" or key == "aa2":
                    points = 2
                elif key == "a3" or key == "aa3":
                    points = 3
                elif key == "a4" or key == "aa4":
                    points = 4
                elif key == "a5" or key == "aa5":
                    points = 5   
                elif key == "a8" or key == "aa8":
                    points = 8                   
                else:
                    points = 10
                summ+=points
                print(summ)

        
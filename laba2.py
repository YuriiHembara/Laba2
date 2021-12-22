import collections
x = None
y = 1
while y == 1:
    print("Виберіть дію. Введіть 1 для сортування слів по алфавітному порядку. Введіть 2 для підрахунку літер. Для виходу введіть 3.")
    x = int(input("Виберіть дію: "))
    if x == 1:
        my_str = input('Введіть текст для сортування:')
        words = my_str.split()
        words.sort()
        for word in words:
            print(word)
    elif x == 2:
            print('Введіть текст для підрахунку літер:')
            d = input()
            print(dict(collections.Counter(d)))
    elif x == 3:
        break
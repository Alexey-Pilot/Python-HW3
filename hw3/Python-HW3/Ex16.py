a = [int(input(f"Введите элемент спика № {i + 1}: ")) for i in range(int(input("Введите колличество элементов: ")))]
x = int(input("Введите число: "))
print(f"Число {x} встречается {a.count(x)} раз")

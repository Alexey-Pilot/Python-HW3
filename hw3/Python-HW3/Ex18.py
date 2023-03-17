
a = [int(input(f"Введите элемент № {i + 1}: ")) for i in range(int(input("Введите колличество элементов: ")))]
x = int(input("Введите число: "))
diff = abs(x - (n := a[0]))
for i in a:
    if abs(x - i) < diff:
        n = i
print(n)
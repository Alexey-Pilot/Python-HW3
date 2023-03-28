def isSimple(n, i):
    if i > n / 2:
        return True
    elif n % i == 0:
        return False
    return isSimple(n, i + 1)

n = int(input())
print(["Сложное", "Простое"][isSimple(n, 2)])

def write_num(n):
    s = ""
    while n > 0:
        if 1000 > n > 99:
            key = n // 100 * 100
            s += word_nums[key] + " "
            n = n % 100
        elif 100 > n > 19:
            key = n // 10 * 10
            n = n % 10
            s += word_nums[key] + " "
        elif n < 20:
            key = n
            n = 0
            s += word_nums[key] + " "
    return(s)

def cat_word(i, num):
    if i == 0 or num == 0:
        return cat[0]
    if 4 < num % 100 < 20 or num % 10 > 4 or num % 10 == 0:
        j = 2
    elif 5 > num % 10 > 1:
        j = 1
    else:
        j = 0
    return cat[i][j]

def corr(w):
    if x % 100 != 11 and x % 10 == 1:
        w = w[:-3] + "на "
    elif x % 100 != 12 and x % 10 == 2:
        w = w[:-2] + "е "
    return w

word_nums = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять",
             10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать",
             16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать", 20: "двадцать",
             30: "тридцать", 40: "сорок", 50: "пятьдесят", 60: "шестьдесят", 70: "семьдесят", 80: "восемьдесят",
             90: "девяносто", 100: "сто", 200: "двести", 300: "триста", 400: "четыреста", 500: "пятьсот",
             600: "шестьсот", 700: "семьсот", 800: "восемьсот", 900: "девятьсот", 0: ""}

cat = ["", ["тысяча", "тысячи", "тысяч"], ["миллион", "миллиона", "миллионов"],
            ["миллиард", "миллиарда", "миллиардов"]]


n = int(input("Введите число: "))
word = ""
cycle = len(str(n)) // 3 - int(len(str(n)) % 3 < 0) # считаем циклы по 3 цифры + остаток
for i in range(cycle, -1, -1):
    x = n // pow(10, 3 * i)
    n = n % pow(10, 3 * i)
    word += f"{write_num(x)}"
    if i == 1:
        word = corr(word)
    word += f"{cat_word(i, x)} "

print(word.strip())
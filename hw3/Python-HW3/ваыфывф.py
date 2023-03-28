import modul1 as m1

list_1 = []
for i in range(1,11):
    list_1.append(m1.fib(i))

print(list_1)

print(m1.quick_sort([1, 453, 232, 443, 67, 4, 6, 756, 54, 7]))

list_2 = [1, 33,6, 654,23,234,2,3,45,4]
m1.merge_sort(list_2)
print(list_2)
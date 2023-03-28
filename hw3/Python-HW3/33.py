def changeMarks(lst):
    res = []
    for i in lst:
        if i > 3:
            i = 1
        res.append(i)
    print(*res)



marks = [int(input("Mark: ")) for _ in range(int(input("Marks amount: "))) ]
changeMarks(marks)
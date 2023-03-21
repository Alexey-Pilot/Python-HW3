eng = {
        1:'AEIOULNSTR',
       2:'DG',
       3:'BCMP',
       4:'FHVWY',
       5:'K',
       8:'JZ',
       10:'QZ'
        }
rus = {
        1:'АВЕИНОРСТ',
       2:'ДКЛМПУ',
       3:'БГЁЬЯ',
       4:'ЙЫ',
       5:'ЖЗХЦЧ',
       8:'ШЭЮ',
       10:'ФЩЪ'
        }


worlds = input('Введите слово: ').upper()
points = 0
for i in worlds:
    for key in eng.keys():
        if i in eng[key] or i in rus[key]:
            points += key
print(points)

d = {}
for k, v in eng.items():
    d.fromkeys(v, k)
    print(v)
print(d)
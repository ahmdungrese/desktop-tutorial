import time
class Tuples:
    #عبارة عن مصفوفة لها حجم ثابت, يمكنها تخزين قيم من مختلف الأنواع في وقت واحد و لا يمكن تبديل قيمها.
    A = (10)
    print (A)
    name = ("Ahmad")
    print (name)
    data = (1,19,100,"Abd","salam","Ahmad")
    print(data[4],data[2])
    time.sleep(2)
    print(data[-1]) # names هنا قمنا بعرض قيمة آخر عنصر موجود في الكائن
    for x in data: # و من ثم سيتم طباعتها x في المتغير names في كل مرة سيتم وضع قيمة عنصر من عناصر الكائن
        print(x)
    time.sleep(2)
    nummer =( 105, 115, 223, 123, 223)
    summe = 0
    for x in nummer:
        summe += x
    print("summer ist :",summe)
    

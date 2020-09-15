a = set()
b = set()

i = 0
print("Введите первое множество чисел")
while i <5 :
    number = input()
    a.add(number)
    i = i + 1 

i = 0
print("Введите второе множество чисел")
while i <5 :
    number = input()
    b.add(number)
    i = i + 1 

output = a.union(b)
diff_a = a.difference(b)
symm_diff = a.symmetric_difference(b)
intersect = a.intersection(b)
iss = a.issubset(b)

i = 0
while i<1 :
    print("Выберите операцию с множествами(для выбора введите номер операции)")
    print("1 - объединение")
    print("2 - пересечение")
    print("3 - разность")
    print("4 - симметрическая разность")
    print("5 - принадлежность А к Б")
    n = input()
    if n == "1" :
        print(output)
    elif n == "2" :
        print(intersect) 
    elif n == "3" :
        print(diff_a) 
    elif n == "4" :
        print(symm_diff) 
    elif n == "5" :
        print(iss)
    print("Желаете продолжить?")
    print("1 - Да; 2 - Выход")
    n = input()
    if n == "1" :
        i = 0
    elif n == "2" :
        i = 1



  



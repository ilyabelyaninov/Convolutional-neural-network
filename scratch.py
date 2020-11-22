a = str(input("Введите Имя "))
if a.isalpha():
    True
else:
    while a.isalnum() or a.isdigit():
        a = str(input("Ошибка. Введите имя "))
        if a.isalpha():
            break
b = str(input("Введите Фамилию "))
if b.isalpha():
    True
else:
    while b.isalnum() or b.isdigit():
        b = str(input("Ошибка. Введите Фамилию "))
        if b.isalpha():
            break
c = str(input("Введите Отчество "))
if c.isalpha():
    True
else:
    while c.isalnum() or c.isdigit():
        c = str(input("Ошибка. Введите Отчество "))
        if c.isalpha():
            break


if b[-1] == "а" and b[-2] == "в" :
    q = b[0:-1]
    z=( b)
    x=(q + "ой")
    v=(q + "ой")
    n=(q + "у")
    m=(q + "ой")
    w=(q + "ой")
elif b[-1] == "я" and b[-2] == "а":
    q = b[0:-2]
    z=(b)
    x=(q + "ой")
    v=(q + "ой")
    n=(q + "ой")
    m=(q + "ой")
    w=(q + "ой")
elif b[-1] == "я":
    q = b[0:-1]
    z=(b)
    x=(q + "и")
    v=( q + "и")
    n=(q + "ю")
    m=( q + "ей")
    w=(q + "и")
elif b[-1] == "ь":
    q = b[0:-1]
    z=(b)
    x=(q + "и")
    v=(q + "и")
    n=(b)
    m=( q + "ью")
    w=(q + "и")
elif b[-1] == "й":
    q = b[0:-2]
    z=(b)
    x=( q + "ого")
    v=(q + "ому")
    n=(q + "ого")
    m=(q + "им")
    w=(q + "ом")
elif b[-1] == "о" or b[-1] == "е" or b[-1] == "у" or b[-1] == "х"or b[-1] == "а":
    q = b[0:-1]
    z=(b)
    x=(b)
    v=(b)
    n=(b)
    m=(b)
    w=(b)

else:
    q = b[0:-1]
    z = ( b)
    x = ( b + "а")
    v = (b + "у")
    n = (b + "а")
    m =( b + "ым")
    w = (b + "е")





if c[-1] == "а":
    f=(c)
    g=(c + "ой")
    h=(c + "е")
    j=(c + "у" )
    k=(c + "ой")
    l=(c + "е" )
else:
    f=(c)
    g=(c + "а")
    h=(c + "у")
    j=(c + "а")
    k=(c + "ем")
    l=(c + "е")







if a[-1] == "а":
    q = a[0:-1]
    print("И.П. " + a + " " + z + " " + f)
    print("Р.П. " + q + "ы" + " " + x + " " + g)
    print("Д.П. " + q + "е" + " " + v + " " + h)
    print("В.П. " + q + "у" + " " + n + " " + j)
    print("Т.П. " + q + "ой" + " " + m + " " + k)
    print("П.П. о " + q + "е" + " " + w + " " + l)
elif a[-1] == "я" and a[-2] == "ь":
    q = a[0:-1]
    print("И.П. " + a + " " + z + " " + f)
    print("Р.П. " + q + "и" + " " + x + " " + g)
    print("Д.П. " + q + "е" + " " + v + " " + h)
    print("В.П. " + q + "ю" + " " + n + " " + j)
    print("Т.П. " + q + "ей" + " " + m + " " + k)
    print("П.П. о " + q + "е" + " " + w + " " + l)
elif a[-1] == "я":
    q = a[0:-1]
    print("И.П. " + a + " " + z + " " + f)
    print("Р.П. " + q + "и" + " " + x + " " + g)
    print("Д.П. " + q + "и" + " " + v + " " + h)
    print("В.П. " + q + "ю" + " " + n + " " + j)
    print("Т.П. " + q + "ей" + " " + m + " " + k)
    print("П.П. о " + q + "и" + " " + w + " " + l)

elif a[-1] == "ь" and c[-1] == "ч":
    q = a[0:-1]
    print("И.П. " + a + " " + z + " " + f)
    print("Р.П. " + q + "я" + " " + x + " " + g)
    print("Д.П. " + q + "ю" + " " + v + " " + h)
    print("В.П. " + q + "я" + " " + n + " " + j)
    print("Т.П. " + q + "ем" + " " + m + " " + k)
    print("П.П. о " + q + "е" + " " + w + " " + l)
elif a[-1] == "ь" and c[-1] == "а":
    q = a[0:-1]
    print("И.П. " + a + " " + z + " " + f)
    print("Р.П. " + q + "и" + " " + x + " " + g)
    print("Д.П. " + q + "и" + " " + v + " " + h)
    print("В.П. " + a + " " + z + " " + f)
    print("Т.П. " + q + "ью" + " " + m + " " + k)
    print("П.П. о " + q + "и" + " " + w + " " + l)
elif a[-1] == "й" or a[-1] == "ж":
    q = a[0:-1]
    print("И.П. " + a + " " + z + " " + f)
    print("Р.П. " + q + "я" + " " + x + " " + g)
    print("Д.П. " + q + "ю" + " " + v + " " + h)
    print("В.П. " + q + "я" + " " + n + " " + j)
    print("Т.П. " + q + "ем" + " " + m + " " + k)
    print("П.П. о " + q + "е" + " " + w + " " + l)
elif a[-1] == "о" or a[-1] == "е":
    q = a[0:-1]
    print("И.П. " + a + " " + z + " " + f)
    print("Р.П. " + a + " " + z + " " + f)
    print("Д.П. " + a + " " + z + " " + f)
    print("В.П. " + a + " " + z + " " + f)
    print("Т.П. " + a + " " + z + " " + f)
    print("П.П. о " + a + " " + z + " " + f)
else:
    print("И.П. " + a + " " + z + " " + f)
    print("Р.П. " + a + "а" + " " + x + " " + g)
    print("Д.П. " + a + "у" + " " + v + " " + h)
    print("В.П. " + a + "а" + " " + n + " " + j)
    print("Т.П. " + a + "ом" + " " + m + " " + k)
    print("П.П. о " + a + "е" + " " + w + " " + l)







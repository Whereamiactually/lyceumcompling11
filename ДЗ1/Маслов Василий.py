#Первое задание
import re
re.sub('<.+?>', '', <имя файла>)
#Третье задание
a = input()
a = a.split()
arr = []
c = []
for i in a:

    if ord(i[0])>=1040 and ord(i[0])<=1072:
        if i[-1] == '.' or i[-1] == ',':
            arr.append(i[:-1])
        else:
            arr.append(i)
for i in range(0, len(arr), 2):
    b = []
    b.append(arr[i])
    b.append(arr[i+1])
    c.append(tuple(b))
print(c)

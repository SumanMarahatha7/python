def append(item , lst=[]):
    lst = []
    return lst.append(item)

a = append(1, [])
print(a)

b = append(2, a)
print(b)

c = append(3, [])
print(c)

#output = attribute error
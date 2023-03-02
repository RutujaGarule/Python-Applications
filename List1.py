
values = [10,20,30,40]

print(values)
print(type(values))
print(len(values))

print(values[0])
print(values[1])
print(values[2])
print(values[3])

values.append(50)
print(values)

values.remove(20)
print(values)

values.append(50)
print(values)

print(type(values[0]))

values.append(90.89)
print(values)

values.insert(2,11)
print(values)

values.insert(15,89)
print(len(values))
print(values)

values.reverse()
print(values)

values.copy()
print(values)

values.pop()
print(values)

values.sort()
print(values)

values.clear()
print(values)
print(len(values))
print("demonstration of set")

data = {11,21,51,101,21,11}
data1 = {11,2.6,"hello",True}

print("first set data",data)
print("lenght of data",len(data))
print("data is heterogenous :",data1)
print("data is unordered :",data1)

#print("data ata index 2 :",data1[2])
print("data with unique elements :",data)

print("set is mutable")
data.add(211)
print("data after insertion :",data)

data.remove(211)
print("data after removal :",data)

data.discard(201)
print("data after discard :",data)





Batches = {"PPA": 18000, "LB": 12000, "Python":15000, "Angular":16000}

print("data of dictionary :",Batches)

print("data traversal using for loop")
for x in Batches:
    print(x)

    
print("data traversal using for loop")
for x in Batches:
    print(x,Batches[x])

print("data traversal using for loop")
for x in Batches:
    print(x,Batches.get(x))
    
keyBatches = Batches.keys()
print(keyBatches)
print(type(keyBatches))

valueBatches = Batches.values()
print(valueBatches)
print(type(valueBatches))


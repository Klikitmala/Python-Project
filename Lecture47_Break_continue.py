#Break loop x
'''
for x in range(12):
    for y in range(12):
        print(x+1,"x",y+1,"=",(x+1)*(y+1))
    break
'''
#Check how loop works:
'''for x in range(12):
    print(x)
    break
'''
#Break loop y
'''for x in range(12):
    for y in range(12):
        print(x+1,"x",y+1,"=",(x+1)*(y+1))
        break
'''
for x in range(12):
    break
    for y in range(12):
        print(x+1,"x",y+1,"=",(x+1)*(y+1))

for val in "hello" :
    if val == "l":
        continue
    print(val)
print("The end")
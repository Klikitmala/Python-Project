'''
print("2 x 1 = 2")
print("2 x 2 = 4")
print("2 x 3 = 6")
'''

'''
x = 1
y = 2*x
print("2 x",x,"=",y)
x = x+1
y = 2*x
print("2 x",x,"=",y)
x = x+1
y = 2*x
print("2 x",x,"=",y)
'''

#Playground
'''for x in range(12):
    y = 2*x
    print("2 x",x,"=",y)

#Playground2
for x in range(12):
    x = 1
    y = 2*x
    print("2 x",x,"=",y)
'''
#Short code
'''for x in range(12):
    print("2 x",x+1,"=",2*(x+1))
'''
#Ex2 - Long code
'''for x in range(12):
    x = x+1
    y = 3*x
    print("3 x",x,"=",y)
'''
#Ex2 - 3,4,5 Multiply
'''for x in range(12):
    print("3 x",x+1,"=",3*(x+1))
for x in range(12):
    print("4 x",x+1,"=",4*(x+1))
for x in range(12):
    print("5 x",x+1,"=",5*(x+1))
'''
#Nested Loop
for x in range(12):
    for y in range(12):
        print(y+1,"x",x+1,"=",(y+1)*(x+1))

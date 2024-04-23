#problem1.1
# numberInput = int(input("enter number :"))
# print("*"*numberInput)

#problem1.2
# numberInput = int(input("Enter Number : "))
# text = ""
# for i in range(numberInput):
#     text = text + "*"
# print(text)

#problem1.3 ans1
'''numberInput = int(input("Enter Number : "))
for i in range(numberInput):
    print("*"*(i+1))
'''
#problem1.3 ans2
numberInput = int(input("Enter Number = "))
for x in range(numberInput):
    text = ""
    for y in range(x+1): 
        text = text+"*"    
    print(text)
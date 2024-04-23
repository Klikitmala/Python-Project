#problem1.1
'''
numberInput = int(input("enter number :"))
print("*"*numberInput)
'''
#problem1.2
numberInput = int(input("Enter Number : "))
text = ""
for i in range(numberInput):
    text = text + "*"
print(text)

num = int(input("Please input number of star : "))
for i in range(num):
    print((num-i)*" ",((i*2)+1)*"*")
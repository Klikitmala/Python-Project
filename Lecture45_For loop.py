#range starts from 0.
'''
inputRound = int(input("please Enter Number :"))
sum = 0
for x in range(inputRound) :
    inputNumber = int(input("x"+str(x)+":"))
'''
#range starts from 1. So you have to add +1 after x-value. 
inputRound = int(input("please Enter Number :"))
sum = 0
for x in range(inputRound) :
    inputNumber = int(input("x"+str(x+1)+":"))
    sum = sum+inputNumber
print("Sum of input numbers = ", sum)
    
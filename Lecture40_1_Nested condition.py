#If it True from 1st condition, so it prints all under if block.
'''if True :
    print("Hello Welcome!")
    if True :
        print("Yo ! Mister A")
        if True :
            print("HaHa")
'''
#If it is False, it won't show anything.

usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "admin" and passwordInput == "1234":
    print("Done!")
    
    price = int(input("Price(THB) = "))
    vat = int(input("Vat(%) = "))
    result = price+(price*vat/100)
    print("Result=",result)
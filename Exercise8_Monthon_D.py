id = input("Username ID : ")
password = input("Password : ")
if id == "admin" and password == "1234" :
    print("Login Success")
    print("Welcome to Into the HellShop")
    print("Please select the manu")
    print("1. Milk ")
    print("2. Coconut Milk ")
    print("3. Coco ")
    print("4. Coffee ")
    select = int(input(">>>>"))
if select == 1 :
    print("1. Milk : 12 THB = ")
    amount1 = int(input("Your Amount : "))
    print("=",12*amount1,"THB")
elif select == 2 :
    print("2. Coconut Milk : 25 THB = ")
    amount2 = int(input("Your Amount : "))
    print("=", 25*amount2, "THB")
elif select == 3 :
    print("3. Coco : 20 THB = ")
    amount3 = int(input("Your Amount : "))
    print("=",20*amount3, "THB")
elif select == 4 :
    print("4. Coffee : 25 THB = ")
    amount4 = int(input("Your Amount : "))
    print("=",25*amount4, "THB")
else:
        print("None your selected")

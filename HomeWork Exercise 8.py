print("Please sign in")
username = input("Username:")
password = input("Password:")
if username == "Admin" and password == "01234":
    print("===================================================")
    print("Welcome to Ding Tea, the drink that makes you come.")
    print("===================================================")
    B_Sugar_Price = 7.50
    M_Milk_tea = 7.00
    Thai_Iced = 6.50
    print("(1)Brown Sugar Milk Tea",B_Sugar_Price,"$")
    print("(2)Matcha Milk Tea     ",M_Milk_tea,"$")
    print("(3)Thai Iced Tea       ",Thai_Iced,"$")
    drink_Choice = int(input(">>"))
    if drink_Choice == 1 or drink_Choice == 2 or drink_Choice == 3:
        if drink_Choice == 1:
            print("Brown Sugar Milk Tea")
            print("How many orders would you like?")
            order_choice = int(input(">>"))
            total_ordering = order_choice * B_Sugar_Price
            print("Brown Sugar Milk Tea 7.50$ x",order_choice,"Total:",total_ordering,"$")
        elif drink_Choice == 2:
            print("Matcha Milk Tea")
            print("How many orders would you like?")
            order_choice = int(input(">>"))
            total_ordering = order_choice * M_Milk_tea
            print("Matcha Milk Tea 7.00$ x",order_choice,"Total:",total_ordering,"$")
        elif drink_Choice == 3:
            print("Thai Iced Tea")
            print("How many orders would you like?")
            order_choice = int(input(">>"))
            total_ordering = order_choice * Thai_Iced
            print("Thai Iced Tea 6.50$ x",order_choice,"Total:",total_ordering,"$")
if username != "Admin" and password != "01234":
    print("Username and(or) password is incorrect")
total=0
recieved=1
price=0
purchase="no"
more=0
id=0


import os

os.system('CLS')

code = ["A1" , "A2" , "A3" , "B1" , "B2" , "B3"]
product = ["sandwich" , "coke" , "pepsi" , "energy"  ,"water" ,  "tea"]
price   = ["1.50    " , "1.10"  , "1.10 " ,  "1.50   " , "90p" , "1.30"]
price2 =[150 , 110 , 110 , 150 , 90 , 130]

#detects what coin has been put into the machine#
while recieved != 0:
    print("")
    recieved=input("What cash have you input 10p 20p 50p £1 £2 or input 0 to type product code\n")
    match recieved:
        case  "10p":
            total=total+10
        case  "20p":
            total=total+20
        case  "50p":
            total=total+50
        case  "£1":
            total=total+100
        case  "£2":
            total=total+200
        case  "0":
            break

os.system('CLS')

#prints products,price and item code#
print("You have input",total)
print("    A1       A2       A3      B1        B2     B3")
print(product)
print(price)
print("")

want = input("What product would you want (Make sure it has a capital letter)\n")

#Detects what item code has been input#
match want:
    case "A1":
        id=1
    case "A2":
        id=1
    case "A3":
        id=1
    case "B1":
        id=1
    case "B2":
        id=1
    case "B3":
        id=1


if id == 1: #If the item code is accurate then this will run#
    for i in range(0,5): #compares the item code to the products list#
        if code[i] == want:
            item=product[i]
            price=price[i]
            price2=price2[i]
    os.system('CLS')
    print(item)
    print("This item costs",price)
    choice=input("Would you like this? (yes or no)\n") #Asks the user if this is the correct product#
    
    if choice == "yes":
        os.system('CLS')
        if price2 > total:
            print("You can't afford that")
        else:
            total = total-price2
            purchase="yes"
    
    #converts the pence into pounds#
    while total >= 100: 
        total = total- 100
        more = more + 1
    
    if purchase == "yes":
        print("Thank you for your purchase of a",item)
    print("we have returned £",more,"and",total,"p")

#if item code is inaccurate then this will run#
else: 
    print("Error")
    while total >= 100:
        total = total- 100
        more = more + 1
    print("we have returned £",more,"and",total,"p")

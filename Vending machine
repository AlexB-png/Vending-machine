recieved=1
total=0
cost=0
more=0

while recieved != 0:
    print("")
    recieved=input("What cash have you input 10p 20p 50p 100p 200p")
    if recieved == "10p":
        total=total+10
    elif recieved == "20p":
        total=total+20
    elif recieved == "50p":
        total=total+50
    elif recieved == "100p":
        total=total+100
    elif recieved == "200p":
        total=total+200
    elif recieved == "0":
        break
    else:
        print("coin not recognised")

print(total,"has been input")

print("")
print("")

print("A1 Sandwich £1.50")
print("A2 Coke £1.10")
print("A3 Pepsi £1.10")
print("")
print("B1 Energy drink £1.50")
print("B2 Water 90p")
print("B3 Iced Tea £1.30")    
print("")
item=input("What item would you want")


while item != "End":
    if item == "A1":
        print("That item costs £1.50")
        cost=150
    elif item == "A2":
        print("That item costs £1.10")
        cost = 110
    elif item == "A3":
        print("That item costs £1.10")
        cost = 110
    elif item == "B1":
        print("That item costs £1.50")
        cost = 150
    elif item == "B2":
        print("That item costs 90p")
        cost = 90
    elif item == "B3":
        print("That item costs £1.30")
        cost = 130
    else:
        print("product not recognised")
        break
    
    if total >= cost:
        print("You can afford that!")
        total = total - cost
        print("You have", total,"left")
    elif cost > total:
        print("You don't have enough!")
        
    print("")
    item=0
    item = input("Type End to stop or input another item code")

while total >= 100:
    total = total- 100
    more = more + 1



print("")
print("")
print("Thank you for using the vending machine")
print("We have returned £",more,"and",total,"p")

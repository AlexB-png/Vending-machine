import os
# This was made on the 18/03/25 #
coins = [('1p',0.01),('2p',0.02),('5p',0.05),('10p',0.1),('20p',0.2),('50p',0.5),('£1',1),('£2',2)]
Stock = [('chips',1),('crisps',1.20),('fanta',2),('coke',1.70)]

Total = 0
CoinInput=1
while CoinInput:
    CoinInput = input('Input a coin: ')
    for i in coins:
        if CoinInput == i[0]:
            print('Found Coin')
            Total += i[1]
            os.system('clear') # IT SHOULD BE CLS FOR WINDOWS #
            print(Total)
os.system('clear') # Here Too #
print(Total)
Choice = "N/A"
Purchased = []
while Choice:
    for i in Stock:
        print(i)
    Choice = input("Choose a product: ")
    for i in Stock:
        if i[0] == Choice.lower():
            os.system('clear') # Here Too #
            print(f"That costs {i[1]}")
            Would = input('Would you like that? y/n')
            if Would.lower() == 'y':
                Total = Total - i[1]
                if Total < 0:
                    print("You can't afford that!")
                    Total = Total + i[1]
                else:
                    print('Item has been added')
                    Purchased.append(i[0])
os.system('clear') # Here Too #
print(f"Thank you for purchasing {Purchased}")
print(f"You have been returned {Total}")
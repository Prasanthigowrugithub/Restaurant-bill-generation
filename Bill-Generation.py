# from datetime import datetime

name=input("Enter custmor name: ")

menu='''
1. Biryani      (1 plate)  [INR 800],
2. Pizza        (1)        [INR 100],
3. Cheese Toast (1 piece)  [INR 50],
4. Cake         (250 gm)    [INR 400],
5. Soft Drink   (1 bottel) [INR 100]
'''
price=0
pricelist=[]
totalprice=0
finalprice=0
clist=[]
qlist=[]
plist=[]

menu_items={'Biryani':800,
'Pizza':100,
'Cheese Toast':50,
'Cake':400,
'Soft Drink':100}

option=int(input("Enter '1' For menu"))
if option==1:
    print(menu)
for i in range(len(menu_items)):
    inp1=int(input("If you want to order enter '1' or enter '2' for exit:"))
    if inp1==2:
        break
    if inp1==1:
        choice=input("Enter your menu items: ")
        quantity=int(input("Enter quantity of your choice: "))
        if choice in menu_items.keys():
            price=quantity*(menu_items[choice])
            pricelist.append((choice,quantity,menu_items,price))
            totalprice+=price
            clist.append(choice)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry stock is not available")
    else:
        print("You entered wrong number")
    inp=input("Are you sure for bill yes or no: ")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=","Family Restaurant",25*"=")
            print(28*" ","Andhra Pradesh")
            print("Name:",name,30*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,clist[i],qlist[i],plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','INR',totalprice)
            print("gst amount",52*" ",'INR',gst)
            print(75*"-")
            print(50*" ",'FinalAmount:','INR',finalamount)
            print(75*"-")
            print(50*" ",'Thanks for visting')
            print(75*"-")
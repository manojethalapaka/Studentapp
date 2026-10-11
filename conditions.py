'''ATM_pin=int(input("enter your ATM pin number:"))
balance=67000
if ATM_pin==2003:
    method=input("choose your payment method:").lower()
    if method=="withdrawl":
        amount=int(input("enter your amount to withdrawl"))
        balance=balance-amount
        print("withdrawl successfull")
        print("your current balance is",balance)
        if amount>balance:
            print("you don't have sufficient balance")
        else:
            print("choose correct method to withdrawl")
    elif method=="deposit":
        amount=int(input("enter your amount of deposit:")).lower
        balance=balance+amount
        print("amount deposited successfully")
        print("your current balance is",balance)
        
else:
    print("please enter pin correctly")'''

#program for current bill

'''n=int(input("enter service number of the customer :"))
units=int(input("units consumed by customer:"))
rate=int(input("enter rate per unit:"))
if units>=100 and units<=500:
    totalbill=(units*rate)/10
    print("your total electricity bill is",totalbill)
elif units>=500 and units<2000:
    totalbill=(units*rate)/10
    print("your total electricity bill is",totalbill)
    if totalbill>2000:
        print("you'r qualified for the subsidy")
    else:
        print("youre not eligible for the subsidy")
        
else:
    print("please enter valid service number")'''


'''a=int(input("enter number a :"))
b=int(input("enter number b :"))
c=int(input("enter number c :"))
if a>b and a>c:
    print("largest number is a:",a)
elif b>c and b>a:
    print("largest number is b:",b)
else:
    print("largest number is c:",c)'''

#movie entry
'''age=int(input("enter your age :"))
shows=input("choose which show do you like to book tickets : ")
if age>=18:
        t=int(input("choose your seat numbers:"))
        if shows=="morning":
            print("you booked the tickets for morning show seat numbers",t)
            print("booking successfull")
            print("you're allowed to watch the movie")
        elif shows=="matinee":
             print("you booked the tickets for matinee show seat numbers",t)
             print("booking sucessfull")
        elif shows=="first show":
             print("you booked the tickets for first show seat numbers",t)
             print("booking successfull")
        elif shows=="second show":
             print("you booked the tickets for the second show seat numbers",t)
             print("booking succcessfull")
        else:
             print("shows full")
else:
    print("not allowed due to age restriction")'''

cshopping=int(input("enter the amount of shopping: "))
if cshopping>=1000 and cshopping<=2500:
    
    discount=cshopping*0.02
    print("you got the discount for shopping:",discount)
    totalbill=cshopping-discount
    print("your total bill is",totalbill)
elif cshopping>=2501 and cshopping>=5500:
        discount=cshopping*0.03
        print("you got the discount for shopping:",discount)
        totalbill=cshopping-discount
        print("your total bill is",totalbill)
elif cshopping>=9000:
        discount=cshopping*0.5
        print("you got the discount for shopping:",discount)
        totalbill=cshopping-discount
        print("your total bill is :",totalbill)

else:
    print("thank you visit again")
              
    




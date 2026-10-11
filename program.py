'''b=49.47
b=int(b)
print(type(b))
print(b)'''

'''num_int=int(5.7)
num_int=int(num_int)
print(type(num_int))
print(num_int)'''

'''num_float="432.45"
num_float=float(num_float)
print(type(num_float))
print(num_float)'''

'''message=str(47)
message=int(message)
print(type(message))
print(message)'''

'''is_true=bool(1)
print(is_true)'''
'''is_false=bool(0)
print(is_false)'''

'''non_num_str="mikey"
non_int=int(non_num_str)
print("converted value :",non_int)'''

'''char_a="a"
char_b="b"
ascii_value_a=ord(char_a)
ascii_value_b=ord(char_b)
print("ASCII_VALUE_a:",ascii_value_a)
print("ASCII_VALUE_b:",ascii_value_b)'''

'''num=77
character=chr(num)
print("ASCII_VALUE_4947:",character)'''

'''name=input("enter your name: ")
age=input("enter your age: ")
print("hello," + name + "! your",age, "years old")'''

'''college_name=input("enter your college name: ")
esbd_yr=int(input("enter established year"))
print("@" + college_name +" college was established on year",esbd_yr)'''

'''a=int(input("enter value for a: "))
b=int(input("enter value for b: "))'''
'''print(a," loves 49 but 47 is like devil fruit and 49 is like water")'''
'''print(f"{a} loves {b} but {a} is like devil fruit and {b} is like water both can't be together")'''

'''print(a,b,a,b,sep=" ,",end=" end the line here.")'''

'''name="mikey"
print("hello",name,sep=",",end="!")'''

'''num=int(input("give the value of num:"))
print("you entered:", num,sep="")'''

'''f=float(input("give the value of pi:"))
print("value of pi:",f,sep="")'''

'''s=(input())
x,y,z=s.split(" ")
sum=int(x)+int(y)+int(z)
print(sum)
print("sum of inputs:",sum)'''


'''n=(input("enter multiple inputs:"))
x,y,z=n.split(" ")
x,y,z=10,20,30
n=int(x)+int(y)+int(z)
print("sum of inputs:",n)'''

'''n="john"
a=25
print("Name:john",",Age:25",sep="")'''

'''details=input("enter Name and Age")
Name,Age=details.split(",")
print("Name:",Name,",Age:",Age,sep="")'''

'''c=int(input("enter number :"))
print("countdown: 5 4 3 2 1 ",end="blast off!")'''

'''x,y=input("enter your name and age: ").split(",")
print(f"name:{x},age:{y} years")'''

'''num1=5
num2=10
Sum=(num1+num2)
print("Sum",Sum,sep=":")'''

'''r=int(input("enter value for radius:"))
areaofc=(3.14*r**2)
print("Area of the circle",areaofc,sep=":")'''

'''a=int(input("enter value for a:"))
b=int(input("enter value for b:"))
c=int(input("enter value for c:"))
d=(b**2)-4*a*c
roots=(-b+(d**(1/2)))/2*a
roots2=(-b-(d**(1/2)))/2*a
print(f"Roots:({roots},{roots2})")'''

'''a=10
b=20
b=b+a
a=b-a
b=b-a
print(f"value of a is:{a}")
print(f"value of b is:{b}")'''

'''temp_cel=int(input("enter temperature for celsius: "))
temp_f=temp_cel*(9/5) +32
temp_k=273+temp_cel
print(f"temp in f is:{temp_cel}")
print(f"temp in k is:{temp_k}")'''

'''usd=int(input("enter amount in usd:"))
euro=float(input("enter amount in euro:"))
exchange=usd*euro
print(f"exchange in euro is:{exchange}")'''

'''num1=int(input("enter a value :"))
num2=int(input("enter a value :"))
operation=input("enter type of operation:")
if operation=="+":
    print("after addition result is:",num1+num2)
elif operation=="-":
    print("after subtraction result is:",num1-num2)
elif operation=="*":
    print("after multiplication result is:",num1*num2)
elif operation=="/":
    print("after division result is:",num1/num2)
else:
    print("enter valid operator")'''

flipkart=input("welcome to flipkart ..")
f_user=input("do you like to go through our flipkart yes/no:").lower()
if f_user=="yes":
        f_intf=input("here is the interface home/search/categories/account/cart :").lower()
        if f_user=="categories":
            print("you can see all the trending sales and discounts")
            print(input("if you like to buy anything you can check through going to search click (yes/no):").lower())
            print("you can now explore things in flipkart")
            print(input("would you like to buy a new mobile ..(yes/no)...?:").lower())
            print("show all the brands available in flipkart")

            print(input("would you like to see mobiles on oppo/lenovo/nothing/iphone/samsung choose :").lower())
        elif f_user=="iphone":
            print(input("we have trending iphone 17 pro would you like go check it ..yes/no..:").lower())
            print("give details and latest features about the iphone 17 pro")
            print(input("do you like the features and like to buy it yes/no..?:").lower())
            print(input("would you like to add to you cart yes/no:").lower())
            if f_user=="cart":
                print("click on go through cart")
                print(input("after checking cart would you like to place the order ...yes/no :").lower())
                print("here's the details about your order")
                print("your order i'd is m3455345 ")
                ord_amount=print("cost of the iphone is 1,55000")
                ord_gst=print(155000*2/100)
                deliver_charges=print("delivery charges is 50")
                total_bill=ord_amount+ord_gst+deliver_charges
                print(input("would you like to buy through online/EMI bcoz no Cod on big amounts:").lower())
                if f_user=="online":
                    print(input("so were like to confirm the payment right ..yes/no:").lower())
                    print(input("we have access to multiple upi methods phnpe/paytm/googlepy/bhimupi:").lower())
                    print("your total bill amount is :",total_bill)
                    print(("final call to confirm the payment ..yes/no..:").lower())
                    if f_user=="yes":
                        print("payment cnfirmed",total_bill)
                        print("your payment is successfull")
                        print("order will be delivered in 4 days")
                        print("thank you for choosing us😊😍")
                    else:
                        print("i just want to verify how's the phone and all the details")
                elif f_user=="EMI":
                        print("here's the details for processing EMI")
                        print(("for EMI we can give you 15 months tenure to make payments ..yes/no:").lower())
                        ord_emi=ord_amount*(15/100)/(15)
                        print(("would you like confirm the order yes/no: ").lower())
                        print("your order id is 3453453453")
                        print("make sure to pay on time or charges will be applied")
                        print("your order is confirmed and will be delivered in 5 days")
                        print("thanks for choosing us❤️")
                else:
                    print("i want to buy through COD but option not there")
            else:
                print("i just want to go thorugh it dont want to add to cart ")
        else:

            print("applied catergory is not in the flipkart")
    
        
else:
    print("didnt like the offers and discounts")
    print("inform me when there is better offers or discounts😒")
















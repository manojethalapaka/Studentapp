'''for i in range(1,50,1):
    if i%2==0:
        if i%2==1:
            print(i)'''

'''l=[1,2,3,4,5,"luffy","zoro","sanji",6,7]
for i in l:
    for l in range(len(l)):
        print(l)'''

'''n=[1,50]
for i in n:
    for m in range(1,13,1):
        print(i,"x",m,"=",i*m)'''

'''n=range(1,50)
for i in n:
    for n in range(1,13,1):
        print(i,"x",n,"=",i*n)'''

'''n=[1,2,3,4,5,6,7,8,9,10]
for i in n:
    for j in range(1,13,1):
        print(i,"x",j,"=",i*j)'''


'''n=[1,2,3,34,34,3453,55,64,667,57,5,7,8,768,57,46,345,25,234,234,25,346,567,768,69,8,978,97,46,4,63,645,2525,2]
n.sort()
for i in n:
    if i%3==0:
        print(i)'''

'''total=0
start=1
stop=5
for i in range(start,stop+1):
    total=total+i
    print(f"sum of :{stop} numbers:{total}")'''

'''l=range(1,46)
total=0
for i in l:
    if i %2==0:
        total=total+i
print(f"sum of {i}numbers:{total}")'''

'''l=["manoj",47,46,"reddy",10,42]
rev=[]
for i in range(5,-1,-1):
    rev.append(l[i])
    print(rev)'''

'''l=[1,2,3,4,5,6,7]
rev=[]
for i in range(6,-1,-1):
    rev.append(l[i])
print(rev)'''

'''s="monkey d luffy"
rev=""
for i in range(13,-1,-1):
        rev+=s[i] 
print(rev)'''

'''m="roronoa zoro x sanji"
rev="" 
for i in range(19,-1,-1):
    rev=rev+m[i]
print(rev)'''

'''l=[1,2,3,4,-46,-47,56,-10,8,9,-33]
for i in range(len(l)):
    if l[i]<0:
        l[i]=0
    print(l[i])'''

'''l=[1,2,3,4,-4,5,6,-6,-8,-78]
for i in range(len(l)):
    if l[i]<0:
        l[l.index(l[i])]=0
    print(l[i])'''

'''for i in range(1,13):
    for j in range(1,13):
     print(j,"x",i,"=",j*i, end="\t")
    print()'''

#check if the given string is a palindrome or not
'''s=["mom","pop","parrot","lion","dad","radar","abba"]
rev=str(s)
for i in s:
    if i==i[rev]:
        print("its a palindrome",rev)
    else:
        print("not a palindrome",rev)
        rev=rev+str(s)[i]
print(rev)   '''

#factorial of a number
'''n=4
f=1
for i in range(1,n+1):
    f=f*i
    print(f)'''

'''s=["pop ,dad ,mom, radar, abba "]
rev=str(s)
for i in range(1,19):
    rev=rev+str(s)[i]
    print(rev)'''

#finding range through prime
'''for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            print(i)
            break'''


'''n=input("enter a value :").lower()
v="aeiou"
count=0
for i in n:
    if i in v:
        count+=1
print(count)'''

'''for i in range(1,5):
    for j in range(1,5):
        print(i) '''

'''for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print()'''

'''for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print()'''

'''for i in range(5,0,-1):
    for j in range(i):
        print("^",end=" ")
    print()'''

'''n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()'''

'''l=["mom","dad","madam","python","radar","level"]
palindrome=[]
for word in l:
        rev=""
        for n in word:
                rev=n+rev
                if rev==word:
                    palindrome.append(rev)
print(palindrome)'''


'''l=["mom","dad","madam","python","radar","level"]
palindrome=[]
for word in range(len(l)-1,-1,-1):
    rev="" 
    for n in range(len(l[word])-1,-1,-1):
        rev=rev+l[word][n]
        if rev==l[word]:
            palindrome.append(rev)
print(palindrome)'''


'''n=5
for i in range(n-1,0,-1):
    print("  ",*(n-i-1)+"* " * i)'''

#pyramid pattern

'''n=5
for i in range(1,n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()

n=5
for i in range(n-2,0,-1):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()'''

'''for i in range(1,3):
    n=5
    for j in range(n-i-1):
        print(" "*(n-i-1)+"* "*(2*i-1))'''
    

'''n=5
for i in range(1,n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
n=5
for i in range(1,n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()'''

'''n=5
for i in range(1,n):
    pattern1=" "*(n-i-1)+"*"*(2*i-1)
    pattern2="  "*(n-i-1)+"*"*(2*i-1)
    pattern3="  "*(n-i-1)+"*"*(2*i-1)
    print(pattern1+"  "+pattern2+"  "+pattern3)'''

'''n=5
for i in range(1,n):
    print(" "*(n-i-1)+"*"*(2*i-1),end=" ")
    print("  "*(n-i-1)+"*"*(2*i-1))'''

'''m="python mom dad hello"
rev="" 
for i in range(len(m)-1,-1,-1):
    rev=rev+m[i]
print("original string",m)
print("reversed string",rev)'''


'''m="python"
rev=""
for word in m:
    rev=word+rev
print("original string:",m)
print("reversed string:",rev)'''


'''i=0
while i<5:
    print(i)
    i+=1'''

'''i=1
n=int(input("enter number for table you want to get :"))
while i<=10:
    print(n,"x",i,"=",n*i)
    i+=1'''

'''i=1
while i<=51:
    if i%2!=0:
        print(i)
        i+=2'''

'''secret=49
ask=int(input("guess a number:"))
while ask!=secret:
    ask=int(input("guess is wrong please try again😒:"))
print("guess is correct👌")'''

'''s="avengers mom dad radar level"
i=len(s)-1
rev=""
while i>=0:
    rev=rev+s[i]
    print(rev)
    i-=1

    if s==rev:
        print("its a palindrome",rev)
    else:
        print("its not a palindrome",s)'''


'''n="computer"
i=0
vowels="aeiou"
count=0
while i<len(n):
    if n[i] in vowels:
        count+=1
    i+=1
print(count)'''

'''n=567891234
bigg=0
while n>0:
    digit=n%10
    if digit>bigg:
        bigg=digit
    n=n//10
print(bigg)'''


'''n=8976
i=0
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
    i+=1
print(rev)'''


'''n=545
i=0
temp=n
sum=0
while n>0:
    digit=n%10
    sum=sum+digit**len(str(temp))
    n=n//10
    i+=1
print(sum)'''


'''l=[151,2,4,370,545,371,9474,407]
i=0
while i<len(l):
    n=l[i]
    temp=n
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit**len(str(temp))
        n=n//10
    i+=1
    if sum==temp:
        print(sum)'''


'''l=[151,2,4,370,545,371,9474,407,757]
i=0
while i<len(l):
    n=l[i]
    temp=n
    sum=0
    rev=0
    while n>0:
        digit=n%10
        sum=sum+digit**len(str(temp))
        rev=rev*10+digit        
        n=n//10
    i+=1
    if sum==temp:
        print(sum)
    if rev==temp:
        print(rev)'''

l=[151,2,4,370,545,371,9474,407,757]
i=0
while i<len(l):
    n=l[i]
    temp=n
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit**len(str(temp))
        n=n//10
    i+=1
    if temp==sum:
        print(sum)







    

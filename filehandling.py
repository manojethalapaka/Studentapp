'''file=open("mikey.py","w")
file.write("i'm monkey d luffy")
file.close()'''

'''file=open("mikey.py","r")
print(file.read())
file.close()

file=open("mikey.py","a")
file.write("/n im gonna become king of the pirates")
file.close()'''

program ='''l=[151,143,545,370,371,407]
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
        print("its an armstrong number",temp)
    else:
        print("not a armstrong number",sum)'''

'''file=open("luffy.py","x")
file.write(program)
file.close()'''

'''file=open("luffy.py","r")
print(file.read())
file.close()'''

'''with open("numbers.py","x") as m:
    m.write(l=["151","143","545","370","371","407"])'''

'''with open("numbers.py","r") as m:
    data=m.read().split()
    numbers=[int(numbers) for num in data]'''

'''l=[151,143,545,370,371,407]
with open("results.txt","w") as m:
    i=0
    while i<len(l):
        n=l[i]
        temp=n
        sum=0
        while n>0:
            digit=n%10
            sum=sum+digit**(len(str(temp)))
            n=n//10
        i+=1
        if temp==sum:
            print(temp,"it is a armstrong nuber")
        else:
            print(sum,"not a armstrong number")'''

code='''a=20
b=30
print(a+b)'''

code2='''l=range(1,10)
print([x*2 for x in l])'''

code3='''a=47
b=49
print(a*b)'''

'''files=["ml.py","dl.py","powerbi.py"]
programs=[code,code2,code3]
for filename,codes  in zip(files,programs):
    with open(filename,"w") as f:
        f.write(codes)

exec(open("ml.py").read())
exec(open("dl.py").read())
exec(open("powerbi.py").read())'''

import os
if os.path.exists("armstrong.py"):
    print("file exists")
else:
    print("file not exists")



    







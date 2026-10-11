'''def add(a,b):
    print(a+b)
add(7,9)'''

'''def words():
    print("hello world")
words()'''

'''def words():
    print('python programming')
words()'''

'''def subtract(a,b):
    print(a-b)
subtract(9,6)'''


'''def multiply(a,b,c=6):
    return a*b*c
print(multiply(4,5))'''

'''def greet(mikey):
    print("hello",mikey)
greet('mikey')'''

'''def add(a,b):
    return a+b
print(add(5,7))'''

'''def square(n):
    return(n*n)
print(square(5*5))'''

'''def even_odd(n):
    return 'even' if n%2==0 else 'odd'
print(even_odd(32))
print(even_odd(47))
print(even_odd(49))'''

'''def max_two(a,b):
    return 'a' if a>b else 'b'
print(max_two(11,10))
print(max_two(11,17))'''

'''def fact_num(n):
        f=1
        for  i in range(1,n+1):
            f*=i
        return f
print(fact_num(7))'''

'''def length(s):
    return len()
print(length('mikey'))'''

'''def check_num(n):
    if n>0:return 'postive'
    elif n<0:return 'negative'
    else:return 'zero'
print(check_num(-1))
print(check_num(7))
print(check_num(0))'''

'''def sum_list(lst):
    return sum(lst)
l=[4,5,6,7]
print(sum_list(l))'''

'''def reverse(s):
    return s[::-1]
print(reverse('manoj'))'''

'''def palindrome(s):
    return s==s[::-1]
print(palindrome("mom"))
print(palindrome("python"))'''

'''def ctof(c):
    return (c*9/5)+32
print(ctof(87))'''

'''def largest(lst):
    return max(lst)
l=[232,3,4,54,5,6,56,56,7,6,7,675,654,54,545,445,]
print(largest(l))'''

'''def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return 'not a prime'
        return 'its a prime'
print(is_prime(77))
print(is_prime(49))
print(is_prime(47))
print(is_prime(46))'''

'''def word_count(s):
    return len(s.split())
print(word_count("my name is monkey d luffy"))
print(word_count("i'm gonna become the king of the pirates"))'''

'''def second(lst):
    lst=list(set(lst))
    lst.sort()
    return lst[-2]
l=[343,435,345,5,46,456,46,4,7456,56,345,334,543]
print(second(l))'''

'''def merge(a,b):
    return a+b
print(merge("python programming"," is fun"))'''

'''def common(a,b):
    return list(set(a)&set(b))
print(common([1,7,4,3,5,6,9],[2,8,6,7]))'''

'''def sum_digits(n):
    return sum(int(i)
         for i in str(n))
print(sum_digits("679"))'''

'''def armstrong(n):
    return n==sum(int(i)**len(str(n)) for i in str(n))
print(armstrong(151))
print(armstrong(143))
print(armstrong(370))
print(armstrong(371))'''

'''def table(n):
    for i in range(1,13):
        print(f"{n} x {i} = {n*i}")
print(table(7))'''

'''def inter(a,b):
    return list(set(a)&set(b))
print(inter([3,4,5,6,3,2,2],[44,4,4,3,2,4,5]))'''

'''def capital(s):
    return s.title()
print(capital("monkey d luffy"))'''

'''def fun(x=[]):
    x.append(1)
    return x
print(fun())
print(fun())
print(fun())'''

'''def add_item(item,data=[]):
    data.append(item)
    return data
print(add_item(10))
print(add_item(20))'''

'''x=10
def test():
    x=20
    print(x)
test()
print(x)'''

'''def calculate(a,b):
    return a+b,a*b
x,y=calculate(5,3)
print(x)
print(y)'''

'''numbers=[1,2,3,4]
result=list(map(lambda x:x*2,numbers))
print(result)'''

'''nums=[1,2,3,4,5,6,7,8]
result=list(filter(lambda x:x%2==0,nums))
print(result)'''

'''def operation(func,a,b):
    return func(a,b)
result=operation(lambda x,y:x+y,5,6)
print(result)'''

'''def greet():
    return 'hi'
x=greet
print(x())'''

'''add=lambda x,y:x+y
print(add(8,2))'''

'''nums=[1,2,3]
result=list(map(lambda x:x+5,nums))
print(result)'''

'''nums=[1,2,3,4,5]
result=list(filter(lambda x:x>3,nums))
print(result)'''

'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
print(fact(9))
print(fact(1))'''

'''def add(a,b=10):
    return a+b
print(add(5))'''

'''def test():
    return
print(test())'''

'''def length(s):
    return len(s)
print(length("luffy"))'''

'''def maximum(a,b):
    return max(a,b)
print(maximum(7,9))'''

'''def fun():
    print('A')
    print('B')
fun()'''

'''def test():
    return[10,20,30]
print(test()[2])'''

'''def swap(a,b):
    a,b=b,a
    return a,b
print(swap(9,4))'''

def check(n):
    if n>0:
        return 'positive number'
    return 'negative number'
print(check(-3))
print(check(0))











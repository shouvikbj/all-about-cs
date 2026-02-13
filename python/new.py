# a = 90
# print(a)
# # Basics 
# name=input("Enter the value of a:")
# print(name)
# # Calculation
# first_num = 234
# second_num = 34
# res=first_num // second_num
# res=first_num % second_num
# print(res)
# print(type(res))
# # Simple Interest
# p = int(input("Enter p: "))
# r = int(input("Enter r: "))
# t = int(input("Enter t: "))
# si=(p*r*t)/100
# print(si)
# type(si)
# # Conditional Statements (if-else)
# # ODD-EVEN
# n = 29
# if (n % 2 ==0):
#     print("The number is even")
# else:
#     print("The number is odd")
# # LARGEST AMONG THREE
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# if (a>b and a>c):
#     print("a is the largest")
# elif (b>a and b>c):
#     print("b is the largest")
# else:
#     print("c is the largest")
## Conditioanl Loops ##

'''For Loop'''
# # Version 1
# for i in range(10):
#     print(i)
# # Version 2
# for i in range(10,30,3):
#     print(i)
# Version 3
#li=[12,45,23,56,89,73]
#### One Process
# for i in range(len(li)):
#     print(li[i])
#### Another Process
# for item in li:
#     print(item)
# for i in range(len(li)):
#     if(li[i]==89):
#         print(str(i)+ " => "+ str(li[i]))

'''While Loop'''
# n=int(input("Enter a number: "))
# rev=0
# while(n!=0):
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# print(rev)

#### LIST (Mutable) ####
li=[5,6,[12,56],"Anasmita",(3,4)]
# print(li)
# print(li[0])
# li1=[3,4,5,6]
# li2=[7,8,9,10]
# print(li1+li2)
# print(li2*3)
# li1.append(12)
# li1.insert(1,6.7)
# print(li1)
# li1.append(li2)
# print(li1)

#### TUPLES ####
t=(1, 2, [1, 2], (3, 4), "Annu", 7)
print(t)
print(t[3][1])
'''Convert tuple to list'''
li3=list(t)
print(li3)
tup=tuple("Anasmita")
print(tup)
tup1= (0, 1, 9, 7)
tup2= ("Mango","Apple","Orange")
tup3=tup1+tup2
print(tup3)
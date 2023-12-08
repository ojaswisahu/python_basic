# print("twinkle,twinkle,little star""\n\t how i wonder what you are!""\n\t\t up above the world so high"
#       "\n\t like a diamond in the sky","\n twinkle,twinkle,little star","\n\t how i wonder what you are")


# # importing platform library
# from platform import python_version
# # getting python interpreter version as a result
# print("current version of python interpreter we are using-",python_version())


# import datetime
# now=datetime.datetime.now()
# print("current date and time :")
# print(now.strftime("%d-%m-%Y %H:%M:%S"))


# import math as M
# Radius=float(input("please enter the radius of the given circle:"))
# area_of_the_circle=M.pi* Radius * Radius
# print("The area of the given circle is:",area_of_the_circle)


#fname=input("input your first name : ")
#lname=input("input your last name : ")
#print(" hello! "+ fname + " " + lname)


#value=input("input some comma seprated numbers :")
#list=value.split(",")
#tuple=tuple(list)
#print('List :',list)
#print('tuple :',tuple)


#color_list=["Red","Green","White","Black"]
#print("%s %s"%(color_list[0],color_list[-1]))


#exam_st_date=(9,10,2023)
#print("The examination will start from : %i / %i / %i"%exam_st_date)


#a=int(input("input an integer :"))
#n1=int("%s"%(a))
#n2=int("%s%s"%(a,a))
#n3=int("%s%s%s"%(a,a,a))
#print(n1+n2+n3)


#print(abs.__doc__)


#even
# for a in range(0,101):
#     if a % 2 == 0:
#         print(a, end=",")


#odd
# for a in range(1,101):
#     if a % 2 !=0:
#         print(a,end=",") 


# pi=3.1415926535897931
# r=6.0
# v=4.0/3.0*pi*r**3
# print('The volume of the sphere is: ',v)


# def difference(n):
#     if n <= 17:
#         return 17-n
#     else:
#         return (n-17)*2
# print(difference(22))
# print(difference(14))


# def near_thousand(n):
#     return((abs(1000-n)<=100)or(abs(2000-n)<=100))
# print(near_thousand(1000))
# print(near_thousand(900))
# print(near_thousand(800))
# print(near_thousand(2200))


# def sum_thrice(x,y,z):
#     sum=x+y+z
#     if x==y==z:
#         sum=sum*3
#         return sum
    
# print(sum_thrice(1,2,3))
# print(sum_thrice(3,3,3))


# def new_string(text):
#     if len(text)>=2 and text [:2]=="is":
#         return text
#     return "is"+text
# print(new_string("array"))
# print(new_string("isempty"))


# def larger_string(text,n):
#     result = ""
#     for i in range (n):
#         result=result+text
#     return result
# print(larger_string('abc',2))
# print(larger_string('.py',3))


# num=int(input("enter any number to text whether it is odd or even: "))
# if(num%2)==0:
#     print("the number is even")
# else:
#     print("the provided number is odd")


# def list_count_4(nums):
#     count = 0
#     for num in nums:
#         if num == 4:
#             count = count + 1
#     return count
# print(list_count_4([1,4,6,7,4]))
# print(list_count_4([1,4,6,4,7,4]))


# def substeing_copy(text,n):
#     flen=2
#     if flen> len(text):
#         flen=len(text)
#     substr=text[:flen]
#     result=""
#     for i in range(n):
#         result=result+substr
#     return result
# print(substeing_copy('abcdef',2))
# print(substeing_copy('p',3))

# c =int(input("enter temperature in celsius: "))
# f =(1.8*c)+32
# print("temperature in fahrenheit: ",f)

# f =float(input("enter temperature in fahrenheit: "))
# c =(f-32)*5/9
# print("temperature in celsius: ",c)

# a=[]
# for x in range(1500,2701):
#     if(x %7==0) and (x %5==0):
#         a.append(str(x))
# print(','.join(a))        

# a= input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
# b = int(a[:-1])
# c = a[-1]

# if c.upper() == "C":
#   result = int(round((9 * b) / 5 + 32))
#   d = "Fahrenheit"
# elif c.upper() == "F":
#   result = int(round((b - 32) * 5 / 9))
#   d = "Celsius"
# else:
#   print("Input proper condition.")
#   quit()
# print("The temperature in", d, "is", result, "degrees.")

# import random
# target_num, guess_num = random.randint(1, 10), 0
# while target_num != guess_num:
#     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
# print('Well guessed!')

# n=int(input("enter a digit: "))
# for i in range(n):
#     for j in range(i):
#         print ('*', end="")
#     print('')

# for i in range(n,0,-1):
#     for j in range(i):
#         print('*', end="")
#     print('')
	
# txt = "Hello World"[::-1]
# print(txt)

# a=['sham','shan','vishnu','laxmi']
# a.reverse()
# print(a)

# a=('sham')
# print(len(a))

# a=input("enter here: ")
# c=0
# b=('a','e','i','o','u')
# for i in a:
#     for j in b:
#         if (i==j):
#             c+=1     
#             print(i)
# print(c)


# a=input("enter here: ")
# c=0
# b=('a','e','i','o','u')
# for i in a:
#     if i not in b:
#         c+=1 
#         print(i)
# print(c)

# a=input(("enter here: "))
# opp=a[: :- 1]
# if a==opp:
#     print("true")
# else :
#     print("false")

# a={5,4,3,2,6,9}
# a.add('raju')
# a.remove('raju')
# for items in a:
# if 9 in a:
#     print('true')
# else:
#     print('false')

# a=input("enter here: ")
# c=0
# b=("1234567890")
# for i in a:
#     for j in b:
#         if i==j:
#             c+=1     
#             print("int")

# a=input("enter here: ")
# c=0
# b=("1234567890")
# for i in a:
#     for j in b:
#         if (i==j):
#             c+=1     
#             print(i)

# a=('      roshni manshi manya     ')   
# print(a.strip())

#------------------------------------------------------------------------------------------------------------------------------------------------
# 6 8 12 14 16 incomplet

# #1
# a=("shan","sahu","ram","krishn")
# print(len(a))

# #2 net
# a=input("enter here: ")
# def reverse(s):
# 	str = ""
# 	for i in s:
# 		str = i + str
# 	return str
# s = (a)
# print(reverse(s))

# #3
# a=input("enter here: ")
# c=0
# b=('a','e','i','o','u')
# for i in a:
#     for j in b:
#         if (i!=j):
#             c+=1     
#             print(i)
# print(c)

# #4
# a=input("enter here: ")
# def reverse(s):
# 	str = ""
# 	for i in s:
# 		str = i + str
# 	return str
# s = (a)
# t=(reverse(s))
# if s == t:
# 	print("True")
# else:
# 	print("False")

# #5
# a=input("enter here: ")
# c=0
# b=("1234567890")
# for i in a:
#     for j in b:
#         if (i==j):
#             c+=1     
#             print(i)

# #7
# a=input("enyer here: ")
# print(a.title())

# #9 not run
# a=input("enter here: ")
# b=set({a})
# print(b)

# #10
# a='      shan sahu      '   
# print(a.strip())

# #11
# h=("a","b","c","d")
# print(h.index("a"))

# #13
# a=("shan sahu")
# b=a.split()
# print(b)

# #15
# a=input("enter gmail: ")
# if "@gmail.com" in a:
#     print("True")
# else:
#     print("False")    
# --------------------------------------------------------------------------------------------------------------------------------------------------
# class Student:
#     def __init__(self,a,b,c,d,e):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
#         self.e=e
#     def add (self):
#         res=self.a+self.b+self.c+self.d+self.e
#         return res
#     def div (self):
#         res=ab/500
#         return res
#     def mul (self):
#         res=abc*100
#         return res
# obj=Student(50,50,50,50,50)
# ab=obj.add()
# abc=obj.div()
# abcd=obj.mul()
# print(abcd,"%")
# -------------------------------------------------------------------------------------------------------------------------------------------------

# # 1
# class persion:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def attributes (self):
#         return f'my name is {self.name} and i am {self.age} years old.'
    
# obj=persion('ojaswi',16)
# ab=obj.attributes()
# print(ab)

# # 2
# class Circle():
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return self.radius**2*3.14
    
#     def perimeter(self):
#         return 2*self.radius*3.14

# obj=Circle(8)
# print(obj.area())
# print(obj.perimeter())

# # 3
# class Bankaccount():
#     def __init__(self):
#         self.balence=0
#     def deposite(self):
#         d=int(input("deposite ammount: "))
#         self.balence+=d
#         print("balence: ",self.balence)
#     def widdrow(self):
#         w=int(input("widdrow ammount: "))
#         if self.balence>=w:
#             self.balence-=w
#             print("balence: ",self.balence)
#         else:
#             print("not seficent ammount")
# obj=Bankaccount()
# obj.deposite()
# obj.widdrow()

# # 4
# class Employee():
#     def __init__(self):
#         self.name="ramesh"
#         self.salery=10000
#     def bonus(self):
#         b=int(input("Enter Bonus Amount: "))
#         self.salery+=b
#         print(" Name:",self.name,"\n Salery: 10000Rs\n Bonus:",b,"\n Total Salery:",self.salery)
# obj=Employee()
# obj.bonus()
# ------------------------------------------------------------------------------------------------------------------------------------------------
# class Bank:
#     def __init__(self):
#         self.dict={
#             "rakesh":{
#                 "pin":"1234",
#                 "balence":1000,
#             },
#             "nitin":{
#                 "pin":"1245",
#                 "balence":1500,
#             },
#             "montu":{
#                 "pin":"3748",
#                 "balence":1100,
#             },
#             "chintu":{
#                 "pin":"4890",
#                 "balence":1550,
#             },
#             "sandeep":{
#                 "pin":"9423",
#                 "balence":2000,
#             },
#         }
#         add=int(input("Add coustmor 1 / deposite and widdrow 2: "))
#         if add == 1:
#             c_name=input("Enter coustomer name: ")
#             c_pin=input("Enter your pin: ")
#             self.dict[c_name]={"pin":c_pin,"balence":0}
#             print("name: ",c_name," pin: ",c_pin," balence: 0")
#             b=input("you can see the all coustomer dateles enter yes or no: ")
#             if b == "yes":
#                 print(self.dict)
#         elif add == 2:
#             name=input("Enter your name: ")
#             if name not in self.dict:
#                 print("Your account is not available in this bank")
#                 exit()
#             else:
#                 pin_inp=(input("Enter yoiur PIN: "))
#                 a=(self.dict[name]["pin"])
#                 if pin_inp not in a:
#                     print("Please enter currect PIN")
#                     exit()
#             self.balence=(self.dict[name]["balence"])
#     def work(self):
#         dep_wid=input("Deposite or Widdrow: ")
#         if dep_wid == "deposite":
#             deposite=int(input("Deposite ammount: "))
#             print("Previous Balence: ",self.balence)
#             self.balence+=deposite
#             print("Balence after Deposite: ",self.balence)
#         elif dep_wid == "widdrow":
#             widdrow=int(input("Widdrow ammount: "))
#             print("Previous Balence: ",self.balence)
#             if self.balence>=widdrow:
#                 self.balence-=widdrow
#                 print("Balence after Widdrow: ",self.balence)
#             else:
#                 print("Not Seficent Ammount")
#                 print("Your Ammount: ",self.balence)
            
    
# obj=Bank()
# obj.work()
# ------------------------------------------------------------------------------------------------------------------------------------------------
# # 1
# class Person:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def display(self):
#         print("My name is",self.__name,"and i am",self.__age,"years old.")
# a=Person("shan","16")
# a.display()

# # 2
# class Bank_account():
#     def __init__(self):
#         self.__balence=0
#         self.input=int(input("Enter PIN: "))
#     def display(self):
#         if self.input == 1234:
#             self.user_input=int(input("(deposite:1)(widdrow:2): "))
#             if self.user_input == 1:
#                 d=int(input("deposite ammount: "))
#                 self.__balence+=d
#                 print("balence:",self.__balence)
#             elif (self.user_input == 2):
#                 w=int(input("widdrow ammount: "))
#                 if self.__balence>=w:
#                     self.__balence-=w
#                     print("balence:",self.__balence)
#                 else:
#                     print("not seficent ammount")
#         else:
#             exit()
# obj=Bank_account()
# obj.display()

# # 3
# class Students:
#     def __init__(self,name,roll,persent):
#         self.__name=name
#         self.__roll=roll
#         self.__persent=persent
#     def display(self):
#         print("My name is:",self.__name,"My roll no. is:",self.__roll,"My persent is:",self.__persent)
# a=Students("shan","16","45%")
# a.display()

# # 4
# class Temperature:
#     def __init__(self):
#         self.user=int(input("Enter digit: "))
#     def method(self):
#         a=input("Your enter digit is celciuse/C or ferinight/F: ")
#         if a == "C":
#             b=self.user
#             c=((b*9/5)+32)
#             print(c,"F")
#         elif a == "F":
#             d=self.user
#             e=((d-32)*5/9)
#             print(e,"C")
# obj=Temperature()
# obj.method()

# # 5 incompleat
# class Vehicle:
#     def __init__(self,speed):
#         self.speed=speed
#     def met(self):
#         print("Speed:",self.speed)
# class Car(Vehicle):
#     def __init__(self,brand):
#         self.brand=brand
#     def display(self):
#         print("Speed:",self.speed,"Brand:",self.brand)
# obj=Vehicle("Royal royas")
# obj=Car("24")
# obj.met()
# obj.display()
# -----------------------------------------------------------------------------------------------------------------------------------
a=input("enter shape: ")
if a == "rec":
    class Rectangle:
        def __init__(self,l,b):
            self.l=l
            self.b=b
        def calculate_area(self):
            print(self.l*self.b)
    l=int(input("enter length: "))
    b=int(input("enter breath: "))
    obj1=Rectangle(l,b)
    obj1.calculate_area()
elif a == "cir":
    class Circle:
        def __init__(self,r):
            self.r=r
        def calculate_area(self):
            print(3.14*self.r*self.r)
    r=int(input("enter radius: "))
    obj2=Circle(r)
    obj2.calculate_area()















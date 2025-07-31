# Functions in python :
# Functions is a block of code that perform a specific task

# sai_ex = [1200,1500,1650]
# kiran_ex = [800,1555,3200,4500]

# def mothly_exp(s): # function arguments
#     total = 0 
#     for i in s:
#         total += i 
#     return total # return value

# sai_monthly_exp = mothly_exp(sai_ex)
# kiran_monthly_exp = mothly_exp(kiran_ex)

# print('Sai monthly exp:',sai_monthly_exp)
# print('Kiran monthly exp:', kiran_monthly_exp)


# Arguments are of two types in python 
# 1. Positional Arguments
# 2. Named Arguments 
# 3. Default Arguments

# Dictionary in pythons :
# Dictionary allows you to key, values pair Also known as, Maps, Haashtables, Associate arrays
 
# Creating Dictionary 
# Dic_a = {'sai':728601245,'kiran':7897458789,'tom':8858575485} 

# Dic_a["sai"] = 8297716856 
# print(Dic_a)
# del Dic_a['kiran'] 
# print(Dic_a)

# find the key and pair values in the dic:
# for key in Dic_a:
#     print("Name :", key, "Mobile no: ",Dic_a[key] )

# tuples in python :
# List : All values have similar meaning (Homogenous)
# Tuple : All vlues have diffrent meaning (heterogeneous)

# Modules in python 
# Module is a way to resue a code written by someone else:

# import math

# print(math.sqrt(16))
# print(math.pow(2,5))
# print(dir(math))

# import calendar 
# # cal = calendar.calendar(2020) 
# # print(cal)
# is_leap = calendar.isleap(2020) 
# # print(is_leap)
# print(dir(calendar))

# import sys 
# sys.path.append("")

# import function as f 
# import area : to find the areas

# 1. What is json 
# JSON(Java script object notation ) : 
        # JSON is a data exchenge format similar to xml 
        #JSON is lightweight format compares to xml 
# 2. json vs Xmlc
# 3. Create address book useing JSON format


# We will write two programs 
# 1. Tocreate address book and write some records into it 
# 2. Read this address book

# book = {}
# book['sai'] ={
#     'name' : 'Sai',
#     "address": 'Hyderabad',
#     "phone": 98787799
# }
# book['Kiran'] ={
#     'name' : 'Kiran',
#     "address": 'Hyderabad',
#     "phone": 82977185
# }
# import json 
# dum = json.dumps(book) 

# with open("C://Users//DELL//OneDrive//Desktop//Python Github//sai.text", 'w') as f:
#     f.write(dum)

# we want read the file 
 
# f = open('C://Users//DELL//OneDrive//Desktop//Python Github//sai.text','r')
# s = f.read()
# print(type(s))

# import json 
# book = json.loads(s) 
# print(type(book)) 

# Reading and writing files in python 
# 1. Create a new file and write to it 
# 2. Reading file line by line 
# 3. File open modes 
# 4. With statament 

# f = open("C:\\Json_data\\text.txt", 'a')
# f.write("\n I Love Css")
# f.close() 
# print(f)

# f = open("C:\\Json_data\\text.txt", 'r')
# for i in f :
#     word_count = i.split()
#     print(len(word_count))
# f.close()

# word = input("Enter a word:")
# f = open("C:\\Json_data\\data.txt", 'a')
# print(f.write(f'\n{word}'))
# f.close()

# print(__name__)

# Exceptions handling in python  :
# Excption are errors detected at the time of program execution /
# Accident = Exception 
#Detour = Handling Exception 

# x = int(input("Enter a number: ")) 
# y = int(input("Enter a number :"))
# try:
#     z = x / y 
# except ZeroDivisionError as e:
#     print('Divdes: ', e) 
#     z = None
# print("Division is: ", z)


# Class in python :
# combined the properties and methods is called class : 
# Object is the instace of class  

# Example code:

# class Human:
#     def __init__(self, name, occupation):
#         self.name = name 
#         self.occupation = occupation 
#     def do_work(self):
#         if self.occupation == "tennis player":
#             print(self.name, "Plays tennis")
#         elif self.occupation == "actor":
#             print(self.name, "Shoot a film")
#     def speaks(self):
#         print(self.name, "Says how are you?") 
# sai = Human("Saikiran", "actor")
# sai.do_work()
# sai.speaks()    

# print()
# print()
# kiran = Human("Kiran", "tennis player")
# kiran.do_work()
# kiran.speaks()

# Inheritance in python 
# Benefits of Inheritance 
# 1. Code Resuce 
# 2. Extensibility 
# 3. Readability  


# class Vechile:
#     def __init__(self):
#         print("I'm Vechile")

# class car(Vechile):
#     def __init__(self):
#         print("I AM  A CAR")
#         self.wheels = 4 
#     def use_of_car(self):
#         print("I have 4 wheels")

# class bike(Vechile):
#     def __init__(self):
#         print("I AM  A bike")
#         self.wheels = 4 
#     def use_of_bike(self):
#         print("I have 2 wheels only")

# c = car()
# m = bike() 

# c.use_of_car()
# m.use_of_bike()


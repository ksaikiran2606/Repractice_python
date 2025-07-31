# #  Why python 
# # -- 1. Easy to learn 
# # -- 2. Code Developement 
# # -- 3. Code  development speed
# # -- 4. Rich set of liabraries (modules)
# # -- 5. Used Heavly In (Data Science, Machine Learning, Scientific computing)
# # -- 6. Plenty Job opportunites 

# # Varibles in python :
# # Variables is like a container that store the data like numeric, tesxt etc...

# # examples : (Home expensive )
# rent = 1220 
# gas = 200 
# groceries = 305 
# total = rent + gas + groceries
# print(total)

# item1 = "rent"
# item2 = "gas"
# item3 = "groceries" 
# print("Expencies names:" , item1, item2, item3)

# # the rules for declaring variables in Python:
# #  1. Variable names must start with a letter or underscore
# #  2. Variable names can only contain letters, numbers, and underscores (_)
# #  3. Variable names are case-sensitive
# #  4. Don’t use Python reserved keywords as variable names
# #  5. No spaces in variable names
# #  6. Variable names should be meaningful

# # Numbers in python 
# a = 255 
# b = 25 
# print(a + b) 
# print(a-b)
# print(a*b) 
# print(a/b)
# print(a % b)
# print(a**b)


# # calculate the distance 
# # time = total_distan / speed
# # example :--- 

# acpt = 128 
# vijayawada = 255 
# total_distance = acpt + vijayawada 

# km =65 
# time = total_distance / km 
# print(round(time,2)) 

# # Numerical are worked :
# #  BODMAS stands for:
# # B – Brackets ()

# # O – Orders (Powers and Roots) **

# # D – Division /

# # M – Multiplication *

# # A – Addition +

# # S – Subtraction -


# # strings in python 
# # strings in python that is store the text data enclosed with
# #  quotes and  strings are  immutable 
# # example :
# text = "ice cream" 
# print(text)

# # we can use the \n in to new line

# # lists  in python

# items = ["bread", "milk","pasta", "maggi"] 
# print(items[0])
# print(items[1])
# print(items[2])

# # We can change the values in the list
# items[0] = "Chips"
# print(items)
# print(items[0:2])

# # We can  the items useing append() 
# items.append("Butter") 
# print(items)

# # we can insert the item particular location use insert keyword insert() 
# items.insert(3,"Banana")  
# print(items)


# veg_items  = ["Palakura", "Puntikurra"]
# non_veg   = ["chicken" , "mutton"] 

# print(veg_items + non_veg )
# print(len(veg_items)) 


# # if condition in python (control statemnets)

# num = input("Enter a number: ")
# num = int(num) 

# if num % 2 == 0:
#     print("number is even")
# else:
#     print("number  is odd")

# and operator works if the all condition are get true
# or operator works atlist one condtion is true get true
# 

# indian_dishes = ["Samosa","butternan","dall"]
# chinese_dishes = ["egg", "chicken", "fried rice"]
# italian_dishes = ["pizza","pasta", "rissto"]


# dish = input("Enter a sish name:  ")

# if dish in indian_dishes:
#     print("Indian dish")
# elif dish in chinese_dishes:
#     print("chinese")
# elif dish in italian_dishes:
#     print("Italian dish")
# else:
#     print("I don't no dish name")

# loops in python :

# Loops in Python are used to execute a block of code repeatedly
# for loop : For loop is used to iterate the over the sequence (list,tuple,string)
# print 1 to 10 numbers
# for i in range(1,11):
#     print(i)


#while loop: Used to run a block of code as long as a condition is True.

# i =  1 # installation
# while i <= 10: # condition 
#     print(i)   # print statement 
#     i = i + 1  # Increase the i value 

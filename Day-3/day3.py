# # Day3 start: 

# class Father():
#     def gardening(self):
#         print("I Enjoy gardening")
# class Mother():
#     def Cooking(self):
#         print("I Love Cooking")

# class child(Father,Mother):
#     def sports(self):
#         print("I Enjoy Sorts") 

# c = child()
# c.gardening()
# c.Cooking()
# c.sports()


# Exceptions in python 
# 1.  How to raise standard exceptions
# 2 . How to raise user exceptions
# 3 . How to raise Key word exceptions 


# 22 pending Video

# Iterators in python   & Iterator implementation using class

# class RemoteControl():
#     def __init__(self):
#         self.channels = ["HBO","National Geographic", "Tensports", "Sony Sports"]
#         self.index = -1 
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.index += 1 
#         if self.index == len(self.channels):
#             raise StopIteration 
#         return self.channels[self.index]

# r = RemoteControl() 
# itr = iter(r)
# print(next(itr))


# Generator is a simply way of creating Iterator 

# def remote_control():
#     yield "CNN"
#     yield "National Geographic"
#     yield "Ten Sports" 

# remote_obj = remote_control() 

# for c in remote_obj:
#     print(c)

# # We are going to produce fibonaaci sequence uesing generator ... Yay!!! 
 
# def fib():
#     a, b = 0, 1 
#     while True:
#         yield a 
#         a,b = b, a+b 
# for f in fib():
#     if f > 100 :
#         break
#     print(f)

# List Comprehessions 
# List Comprehessions provides a way to transform one list into another 
# [expression for item in iterable]
# example : 
# squares = [x**2 for x in range(1,6)]
# print(squares)

# Set in python : 

# sets is a unorder collection of unique items 

# s = set([1,2,2,3,3])
# print(s)

# s1 = {1,2,2,3,3}  
# odd = {i for i in s1 if i % 2 != 0} 
# print(odd) 

# dictionary Comprehessions  

# cityes = ["Mumbai", "Hyderabad","Dehli"]
# countries = ["India", "Usa","France"] 

# zip is a built in function it will combine two dictionries object
# result = zip(cityes, countries)

# for i in result:
#     print(i)

# d = {city:country for city,country in zip(cityes,countries)}
# d2 = [i for i in d]
# print(d2)


# Frozen sets 

# fs = frozenset({1,2,3,4})
# fs.add(5) 
# print(fs)

# Uninoon operator in sets: 

# combine the unique values in two dic  

# d1 = {"a","b","c"}
# d2 = {"b","d","e"} 
# print(d1|d2) 
# print(d1.union(d2))

# Intersection 
# d1 = {"a","b","c"}
# d2 = {"b","d","e"} 
# print(d1&d2)

# Types of Arguments 
# 1. Positional 
# 2. Optional 


# Here we are Writing a program that takes 3 inputs 
# 1. First Number
# 2. Second Number 
# 3. Operations ("add","subtract","multiply") 

# it should return result of operations based on inputs 

# import argparse 

# if __name__  == "__main__":
    # parser = argparse.ArgumentParser()
#     parser.add_argument("number1", help = "First number") 
#     parser.add_argument("number2", help = "Second number") 
#     parser.add_argument("operations", help = "Third number")  

# args = parser.parse_args()
# print(args.number1)
# print(args.number2)
# print(args.operations)
# Remember : video(27)

# To make arguments optional just add -iin front of arguments name


# Decorators in python most important topic:

# Decorators def : Decorators to allow wrapp to functions to in another functions

# import time 

# def time_it(func):
#     def wrapper(*args, **kwrags):
#         start = time.time()
#         result = func(*args, **kwrags)
#         end = time.time()
#         print(func.__name__ + " took " + str((end-start)) + "mil sec")
#         return result 
#     return wrapper
# @time_it
# def cal_squares(numbers):
#     result = [] 
#     for num in numbers:
#         result.append(num * num)
#     return result

# @time_it
# def cal_cubes(numbers):
#     result = [] 
#     for num in numbers:
#         result.append(num * num * num) 
#     return result 


# array = range(1, 100000)
# out_squares = cal_squares(array)
# out_cubes = cal_cubes(array)


# Multithreading In python 

# Handling multiple task at a time its called Multhreading 
# Examples of multithreading:

# for a given list of numbers  print square and cubes of array numbers

# input: [2,3,4,5]

# Output_squares = [4,9,64,81]
# cube_list = [8,27,512,729]


# import time 
# import threading

# def cal_squares(numbers):
#     print("Calculate square numbers")
#     time.sleep(0.5)
#     for num in numbers:
#         print('squares', num*num)

# def cal_cubes(numbers):
#     print("Calculate cubes of numbers")
#     time.sleep(0.5)
#     for num in numbers:
#         print('squares', num*num*num)

# array = [2,3,4,5]

# t = time.time()
# cal_squares(array)
# cal_cubes(array) 

# print("Done in ", time.time()-t)
# print("Hah... I am done with all my work now!")
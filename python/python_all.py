"""
Anasmita Math

Python mainly follows snake_case for variable and function names
Ex: first_name, last_name, calculate_total()
And PascalCase (also known as CamelCase) for class names
Ex: class BankAccount(), class StudentDetails()

variable name => snake case (first_name)
function name => Camel case (getFullName())
class name => Pascal case (StudentDetails)

Python is interpreted or compiled?
=> Interpreted + Compiled 
(Python code is first compiled to bytecode, 
which is then interpreted by the Python interpreter)

"""

## Variables ##

# first_name: str = "John"
# print(first_name)

# first_name = 10
# if type(first_name) == str:
#     print("This is a string")
# else:    
#     print("Wrong type data")

# first_number: int = 10
# second_number: int = 3
# total: str = str(first_number) + str(second_number)
# result = first_number + second_number
# result = first_number - second_number
# result = first_number * second_number
# result = first_number ** second_number
# result = first_number / second_number # (float division)
# result = first_number // second_number # (integer division)
# result = first_number % second_number # (remainder)

# print(result)

# first_name = "Shouvik"
# last_name = "Bajpayee"
# full_name = first_name + " " + last_name
# first_name = first_name + last_name

## Lists ## (mutable)

# my_list = [1, 2, [1, 2], (1, 2), "Shouvik", 5]

# print(my_list[4]) # Shouvik
# print(my_list[-2]) # Shouvik

# print(my_list[2][1]) # 2

# print(my_list[1:4]) # start_index is inclusive and end_index is exclusive

# my_list[0] = 10
# print(my_list)

# my_list[4] = "Bajpayee"
# print(my_list)

# li1 = [1, 2, 3]
# li2 = [4, 5, 6]

# print(li1+li2) # [1, 2, 3, 4, 5, 6]
# print(li1*3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# li1.append(100)
# li1.insert(0, 100) # insert(index, value)
# li1.extend(li2) # extend(list)
# li1.append(li2) # append(list)
# print(li1)

# li3 = [[0, 1]] * 10
# print(li3)

## Tuples ## (immutable)

# t1 = (1, 2, [1, 2], (1, 2), "Shouvik", 5)

# print(t1[2][0]) # 1

# t1[2][0] = 100
# print(t1) # (1, 2, [100, 2], (1, 2), 'Shouvik', 5)
# t1[0] = 100 # TypeError: 'tuple' object does not support item assignment

"""
Usecase of tuples:
1. When we want to store a collection of items that should not be modified after creation.
2. When we want to use tuples as keys in a dictionary (since tuples are hashable, while lists are not).
3. When we want to return multiple values from a function, we can use tuples to group those values together.
"""

# li1 = list(t1) # convert tuple to list
# print(li1) # [1, 2, [100, 2], (1, 2), 'Shouvik', 5]

# t2 = tuple(li1) # convert list to tuple
# print(t2) # (1, 2, [100, 2], (1, 2), 'Shouvik', 5)

## Dictionaries ## (mutable)

# d1 = {
#     "name": "Shouvik",
#     "age": 27,
#     "hobbies": ["coding", "bike riding"],
#     "education": {
#         "degree": "Master's",
#         "major": "Computer Science"
#     }
# }

# print(d1["name"]) # Shouvik
# print(d1["hobbies"][1]) # bike riding
# print(d1["education"]["degree"]) # Master's

# d1["name"] = "Bajpayee"
# d1["college"] = "IIIT Kalyani"
# d1.update({ "college": "IIIT Kalyani", "current_study": "PhD Sem 1" })
# d1.update({ "name": "Bajpayee" })
# print(d1)

## Conditionals ##

# age = 20

# if (age >= 18):
#     print("You are an adult.")
# elif (age >= 13):
#     print("You are a teenager.")
# else:
#     print("You are a child.")

## Loops ##

# while loop
# counter = 0
# while (counter < 5):
#     print(counter)
#     counter += 1

# for loop
# version 1
# for i in range(5):
#     print(i)

# version 2
# for i in range(2, 15, 3):
#     print(i)

# version 3
# li = [10, 20, 30, 40, 50, 60, 70, 80]

# for i in range(len(li)):
#     print(li[i])

# for item in li:
#     print(item)

# for item in li:
#     if (item == 50):
#         print(item)

# for i in range(len(li)):
#     if (li[i] == 50):
#         print(str(i) +" => "+ str(li[i]))

# li2 = [ item**2 for item in li if item%3==0 ]
# print(li2)

#!/usr/bin/env python
# coding: utf-8

# In[3]:


print ("Hello World!")


# In[6]:


print (2+2)
print (2*2)
print (10/2)
print ()
print ("The End")


# In[15]:


print("Today is a good day to learn python")
print('Python is fun')
print("Pyhton's String are easy to use")
print('We can include "quotes" in strings')
print("hello" + " World")
greeting = "Hello"
name = input("Please enter your name")
print(greeting + name)

# if we want a space, we can add that too
print(greeting + '' + name)


# # EscapeChar

# In[27]:


splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)
tabbedString = "1\t2\t3\t4\t5\t6"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh, ...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,.. he's resting\".")

print("""The pet shop owner said "No, no, 'e's uh,...he's resting". """)

anotherSplitString = """This string has been
split over
several
times"""

print(anotherSplitString)

print("C:\\Users\\timbuchalka\\notes.txt")


# In[28]:


print("Today is a good day to learn python")
print('Python is fun')
print("Pyhton's String are easy to use")
print('We can include "quotes" in strings')
print("hello" + " World")
greeting = "Hello"
name = input("Please enter your name")
print(greeting + name)

# if we want a space, we can add that too
print(greeting + '' + name)

age = 25
print(age)

print(type(greeting))
print(type(age))

age = "2 Years"
print(age)
print(type(age))


# In[29]:


print("Today is a good day to learn python")
print('Python is fun')
print("Pyhton's String are easy to use")
print('We can include "quotes" in strings')
print("hello" + " World")
greeting = "Hello"
name = input("Please enter your name")
print(greeting + name)

# if we want a space, we can add that too
print(greeting + '' + name)

age = 25
print(age)

print(type(greeting))
print(type(age))

age = "2 Years"
print(name + " is " + age + " years old")
print(type(age))


# # Operators

# In[7]:


a = 12
b = 3

print(a + b) #15
print(a - b) #9
print(a * b) #36
print(a / b) #4.0
print(a // b) #4 integer division, rounded down towards minus infinity
print(a % b) #0 modulo: the remainder after integer division

print()

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) / 3) - 4) * 12)
print(((a + b) /3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

print()

print(a / (b * a) /b)


# # Strings2

# In[32]:


parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])


# In[42]:


parrot = "Norwegian Blue"

print(parrot[0:6]) # Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:14])
print(parrot[10:])
print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])
print(parrot[:])


# In[59]:


parrot = "Norwegian Blue"

print(parrot[0:6]) # Norweg

print(parrot[-4:-2]) #Bl
print(parrot[-4:12]) #Bl

print(parrot[0:6:2]) # Nre
print(parrot[0:6:3]) # Nw

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])


# In[71]:


letters = "abcdefghijklmnopqrstuvwxyz"

backwords = letters[25::-1]
print(backwords)

# create a slice that produces the character qpo
print(letters[16:13:-1])

# create a slice that produces the character edcba
print(letters[4::-1])

# slice the string to produce the last 8 characters, in reverse order
print(letters[:-9:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])


# # Sequence_Operators

# In[76]:


string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)

print("he's " "proably " "pining " "for the " "fjords")

print("Hello " * 5)

print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "friday"
print("day" in today) # True
print("fri" in today) # True
print("thur" in today) #False
print("parrot" in "fjord") #False


# # repfields

# In[91]:


age = 25
print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
     .format(28, 30, 31))

print()

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}""".format(28, 30, 31))


# # Formatting

# In[97]:


for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
    
print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
    
print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))


# In[7]:


print("Today is a good day to learn python")
print('Python is fun')
print("Pyhton's String are easy to use")
print('We can include "quotes" in strings')
print("hello" + " World")
greeting = "Hello"
name = input("Please enter your name")
print(greeting + name)

# if we want a space, we can add that too
print(greeting + '' + name)

age = 25
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 Years"
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")


# In[2]:


age = 25
print("My age is %d years" % age)

major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))
print("PI is approximately %f" % (22 / 7))
print("PI is approximately %60.50f" % (22 / 7))


# # Statements

# In[7]:


name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# if age >= 18:
#    print("You are old enough to vote")
#    print("Please put an X in the box")
    
if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry,Yoda, you die in return of the jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")


# # GuessigGame

# In[22]:


answer = 5

print("Please guess number between number 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:   # guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, You have guessed it")
    else:
        print("Sorry, You have not guessed correctly")
else:
    print("You got it first time")


# if guess < answer:
#    print("Please guess higher")
#   guess = int(input())
#    if guess == answer:
#        print("Well done, You guessed it")
#    else:
#        print("Sorry, You have not guessed correctly")
# elif guess > answer:
#    print("Please guess lower")
#    guess = int(input())
#    if guess == answer:
#        print("Well done, You guessed it")
#   else:
#        print("Sorry, You have not guessed correctly")
# else:
#    print("You got it first time")
    


# In[21]:


answer = 5

print("Please guess number between number 1 and 10: ")
guess = int(input())

if guess == answer:
     print("You got it first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:   # guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, You have guessed it")
    else:
        print("Sorry, You have not guessed correctly")

    


# if guess < answer:
#    print("Please guess higher")
#   guess = int(input())
#    if guess == answer:
#        print("Well done, You guessed it")
#    else:
#        print("Sorry, You have not guessed correctly")
# elif guess > answer:
#    print("Please guess lower")
#    guess = int(input())
#    if guess == answer:
#        print("Well done, You guessed it")
#   else:
#        print("Sorry, You have not guessed correctly")
# else:
#    print("You got it first time")
    


# # Conditions

# In[10]:


age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")


# # True False

# In[20]:


day = "Friday"
temperature = 30
raining = False

if (day == "Saturday" and temperature > 27) and not raining:
    print("Go Swiming")
else:
    print("Learn Python")
    


# In[9]:


if 0:
    print("True")
else:
    print("False")
    
name = input("Please enter yout name: ")
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the name with no name?")
    
    


# # Checkingin

# In[12]:


parrot = "Norwegian Blue"

letter = input("Enter Character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I dont't need that later")


# In[1]:


activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():
    print("But I want to go to cinema")
else:
    print("Yes! Cinema")
    


# # IfChallenge 

# In[16]:


name = input("Please enter your name: ")
age = int(input("How old are you?: "))

if 18 <= age < 31:
    print("Welcome to the club 18-30 Holidays, {0}".format(name))
else:
    print("I'm Sorry, our Holidays are only for cool people")


# # ForLoops

# In[3]:


parrot = "Norwegian Blue"

for character in parrot: 
    print(character)
    


# # String2

# In[15]:


number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char
    
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))


# # Ranges

# In[18]:


for i in range(1, 20):
    print("i is now {}".format(i))


# # Timetables

# In[21]:


for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(j, i, i * j))
        print("--------------")


# # Shopping

# In[27]:


shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#    if item != "spam":
#        print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        continue
         
            
    print("Buy " + item)


# In[5]:


shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None

# for index in range(6):
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        
print("Item found at position {}".format(found_at))


# In[8]:


shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "albatross"
found_at = None

# for index in range(6):
# for index in range(len(shopping_list)):
#    if shopping_list[index] == item_to_find:
#        found_at = index
#        break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)
        
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))


# # WhileLoop

# In[9]:


# for i in range(10):
#     print("i is now {}".format(i))

i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1


# # Adventure

# In[16]:


available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold()  == "quit":
        print("Game over")
        break
    
print("arn't you glad you got out of there")


# # Guessinggame1

# In[25]:


answer = 5

import random

highest = 10
answer = random.randint(1, highest)

print("Please guess number 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("Yo! You got it First")
else:
    if guess < answer:
        print("Please guess Higher")


# In[ ]:


answer = 5

import random

highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess number 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == answer:
        print("Well Done, You guessed it") 
        break
    else:
        if guess < answer:
            print("Please guess Higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
        guess = int(input())
        if guess == answer:
            print("Well Done, You guessed it")
        else:
            print("Sorry!, You have not guessed correctly")


# In[2]:


answer = 5

import random

highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess number 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == answer:
        print("Well Done, You guessed it") 
        break
    else:
        if guess < answer:
            print("Please guess Higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
        guess = int(input())
        if guess == answer:
            print("Well Done, You guessed it")
        else:
            print("Sorry!, You have not guessed correctly")


# # HiLo

# In[7]:


low = 1 
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while True:
    guess = low + (high - low) // 2
    high_low = input("my guess is {}. should I guess higher or lower? " 
                     "Enter h or l, or c if my guess was correct"
                     .format(guess)).casefold()
    
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one lesser than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")
        
    guesses = guesses + 1
    


# # aaa

# In[8]:


x = 23

x += 1
print(x)    # 24

x -= 4
print(x)    # 20

x *= 5
print(x)    # 100

x //= 4
print(x)    # 25

x /= 5
print(x)    # 5.0 - note conversion from int to float

x **= 2
print(x)    # 25.0 - x still represents a float

x %= 5
print(x)    # 0.0 - 25 is exactly divisible by 5

greeting = "Good "

greeting += "morning"
print(greeting)

greeting *= 5
print(greeting)


# # Contrived

# In[21]:


numbers = [1, 45, 31, 12, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list 
        print("The numbers are unacceptable")
        break
else:
    print("All those numbers are fine")


# # hilo

# In[1]:


low = 1 
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while low != high:
    guess = low + (high - low) // 2
    high_low = input("my guess is {}. should I guess higher or lower? " 
                     "Enter h or l, or c if my guess was correct"
                     .format(guess)).casefold()
    
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one lesser than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c")
        
    # guesses = guesses + 1
    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I got it in {} guesses".format(guesses))


# # SummaryChallenge

# In[2]:


print("Please choose your option from the list below:")
print("1:\tLearn Python")
print("2:\tLearn Java")
print("3:\tLearn Swimiing")
print("4:\tHave Dinner")
print("5:\tGo to bed")
print("0:\tExit")

while True:
    choice = input()
    
    if choice == "0":
        break
    elif choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")                  
        print("3:\tLearn Swimiing")
        print("4:\tHave Dinner")             
        print("5:\tGo to bed")
        print("0:\tExit")


# In[2]:


choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")                  
        print("3:\tLearn Swimiing")
        print("4:\tHave Dinner")             
        print("5:\tGo to bed")
        print("0:\tExit")
        
    choice = input()


# # Lists_intro

# In[6]:


computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                 ]

for part in computer_parts:
    print(part)
    
print()
print(computer_parts[2])

print(computer_parts[0:3])
print(computer_parts[-1])


# # immutable

# In[14]:


# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
#
# result = False
# print(id(result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))
print(id(another_result))


# # mutable

# In[18]:


shopping_list = ["Milk", 
                 "Pasta",
                 "Eggs",
                 "Spam",
                 "Bread",
                 "Rice"
                ]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["Cookies"]
print(shopping_list)
print(id(shopping_list))
print(id(another_list))

a = b = c = d = e = f = another_list
print(a)

print("Adding Cream")
b.append("cream")
print(c)
print(d)


# # number_lists

# In[20]:


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()
print(len(even))
print(len(odd))

print()
print("mississippi".count("iss"))


# # Buy_Computer

# In[2]:


availabe_parts = ["computer", 
                   "moniter", 
                   "keyboard",
                   "mouse",
                   "mouse pad",
                   "HDMI Cable",
                   "DVD drive"
                  ]

current_choice = "-"
computer_parts = [] # Create an empty list

while current_choice != '0':
    if current_choice in "1234567":
        print("Adding {}".format(current_choice))
        if current_choice == "1":
            computer_parts.append("computer")
        elif current_choice == "2":
            computer_parts.append("monitor")
        elif current_choice == "3":
            computer_parts.append("keyboard")
        elif current_choice == "4":
            computer_parts.append("mouse")
        elif current_choice == "5":
            computer_parts.append("mouse pad")
        elif current_choice == "6":
            computer_parts.append("HDMI Cable")
        elif current_choice == "7":
            computer_parts.append("DVD drive")

    else:
        print("Please add options from the list below:")
        for number, part in enumerate(availabe_parts):
            print("{0}: {1}".format(number + 1, part))
        
    current_choice = input()
    
print(computer_parts)


# # enumerate_example

# In[1]:


for index, character in  enumerate("abcdefgh"):
    print(index, character)


# In[8]:


available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi cable",
                   "dvd drive"
                   ]
#valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = [] # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)


# # number_list (odd,Even)

# In[12]:


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)
print(even)
another_even = even
print(another_even)

even.sort(reverse=True)
print(even)
print(another_even)


# # Sorting

# In[23]:


pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

another_sorted_numbers = numbers.sort()
print(numbers)
print(another_sorted_numbers)

missing_letter = sorted("The quick brown fox jumps over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Ishan",
         "Isha",
         "Bhavik",
         "Shubham",
         "Dhruv",
        ]
names.sort(key=str.casefold)
print(names)


# # number_lists

# In[2]:


empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers =even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = sorted("432985617")
print(digits)

# more_numbers = list(numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()
print(more_numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)


# # lists_intro

# In[6]:


computer_parts = ["computer", 
                   "moniter", 
                   "keyboard",
                   "mouse",
                   "mouse pad",
                   "HDMI Cable",
                   "DVD drive"
                 ]
print(computer_parts)

# computer_parts[3] = "trackball"
print(computer_parts[3:])

computer_parts[3:] = ["trackball"]


# # outliers

# In[9]:


data = [4, 6, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

# del data[0:2]
# print(data)
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

for index, value in enumerate(data):
    if (value < min_valid) or (value > max_valid):
        del data[index]
               
print(data)


# In[13]:


data = [4, 6, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
        
print(stop) # for debugging
del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        start = index + 1
        break
        
print(start) # for debugging
del data[start:]
print(data)


# In[17]:


# data = [4, 6, 104, 105, 110, 120, 130, 130, 150,
#        160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [4, 6, 104, 105, 110, 120, 130, 130, 150,
#        160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [104, 105, 110, 120, 130, 130, 150,
#        160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [104, 105, 110, 120, 130, 130, 150,
#        160, 170, 183, 185, 187, 188, 191]
data = []

min_valid = 100
max_valid = 200

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
        
print(stop) # for debugging
del data[:stop]
print(data)

# process the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # We have the index of the last item to keep.
        # Set 'Start' to the position of the first
        # item to delete, which is 1 after 'index'.
        start = index + 1
        break
        
print(start) # for debugging
del data[start:]
print(data)


# # gobackwards

# In[9]:


data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

# for index in range(len(data) - 1, - 1, - 1):
#   if data[index] < min_valid or data[index] > max_valid:
#       print(index, data)
#       del data[index]
        
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]
    
print(data)


# # Timing_delete

# In[20]:


import timeit
 
max_value = 100  # 100000000
min_valid = 10
max_valid = 97  # 99999997
 
data_list1 = list(range(max_value))
data_list2 = list(range(max_value))
data_list3 = list(range(max_value))
 
 
def sanitise_1(data):
    # process the low values in the list
    stop = 0
    for index, value in enumerate(data):
        if value >= min_valid:
            stop = index
            break
 
    del data[:stop]
 
    start = 0
    for index in range(len(data) - 1, -1, -1):
        if data[index] <= max_valid:
            # We have the index of last item to keep.
            # Set 'start' to the position of the first
            # item to delete, which is 1 after 'index'.
            start = index + 1
            break
 
    del data[start:]
 
 
def sanitise_2(data):
    top_index = len(data) - 1
    for index, value in enumerate(reversed(data)):
        if value < min_valid or value > max_valid:
            del data[top_index - index]
 
 
def sanitise_3(data):
    for index in range(len(data) - 1, -1, -1):
        if data[index] < min_valid or data[index] > max_valid:
            del data[index]
 
 
if __name__ == "__main__":
    # print("Timing")
    # x = timeit.timeit("sanitise_1(data_list1)",
    #                   setup="from __main__ import sanitise_1,"
    #                         "data_list1",
    #                   number=1)
    # print("{:15.15f}".format(x))
    # y = timeit.timeit("sanitise_2(data_list2)",
    #                   setup="from __main__ import sanitise_2,"
    #                         "data_list2",
    #                   number=1)
    # print("{:15.15f}".format(y))
    # z = timeit.timeit("sanitise_3(data_list3)",
    #                   setup="from __main__ import sanitise_3,"
    #                         "data_list3",
    #                   number=1)
    # print("{:15.15f}".format(z))
 
    # sanitise_1(data_list1)
    # print(data_list1)
    # sanitise_2(data_list2)
    # print(data_list2)
    # sanitise_3(data_list3)
    print(data_list3)


# # Number_list_1
# 

# In[26]:


empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for number_list in numbers:
    print(number_list)
    
    for value in number_list:
        print(value)


# # spam

# In[15]:


menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"]
]        

for meal in menu:
    if "spam" not in meal:
        print(meal)
        
        for item in meal:
            print(item)
    else:
        print("{0} has a spam score of {1}"
              .format(meal, meal.count("spam")))
        


# # NoSpam

# In[32]:


menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"]
]   

# for meal in menu:
#    for index in range(len(meal) - 1, -1, -1):
#        if meal[index] == "spam":
#            del meal[index]
#            
#    print(meal)

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
    print()
        


# # MorePrint

# In[3]:


name = "Tim"
age = 10

print(name, age, "Python", 2021)
print(name, age, "Python", 2021, sep=", ")


# # joining_things

# In[18]:


flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

# for flower in flowers:
#   print(flower)

separator = " , "
output = separator.join(flowers)
print(output)

print(",".join(flowers))


# # splitting_things

# In[29]:


panagram = """The quick brown
fox jumps\tover
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

# values = "".join(char if char not in separators else " " for char in numbers).split()
generated_list = ['9', ' '
                  '2', '2', '3', ' '
                  '3', '7', '2', ' '
                  '0', '3', '6', ' '
                  '8', '5', '4', ' '
                  '7', '7', '5', ' '
                  '8', '0', '7']
values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

# use a for loop to produce a list of ints, rather than strings.
# You  can either modify the contents of the 'valence_list' listin place,
# or create a new  list  of ints.

# replace  the values  in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
    
print(values_list)


# # tuples_intro

# In[1]:


t = ("a", "b", "c")
print(t)


# In[31]:


welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

metallica2 = list(metallica)
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2)


# # unpacking

# In[36]:


a = b = c = d = e = f = 42
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("UnPacking a tuple")

data = 1, 2, 76 # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)

print("UnPacking a tuple")

data_list = [12, 13, 14]
p, q, r = data_list
print(p)
print(q)
print(r)


# # tuples_intro1

# In[6]:


welcome = "welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "NightFlight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

name, length, width, height, price = table
print(length * width)


# In[10]:


albums = [("welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("NightFlight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984)
          ]

print(len(albums))

for name, album, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))
    
    
         
         
        


# In[16]:


albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

for name, album, year, songs in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))
    
print()

album = albums[2]
print(album)

songs = album[3]
print(songs)

song = songs[1]
print(song)


# # nested_data

# In[14]:


albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

for name, artist, year, songs in albums:
    print("Album: {}, Artist: {}, Year: {}, Songs: {}"
          .format(name, artist, year, songs))
    
print()

album = albums[3]
print(album)

songs = album[3]
print(songs)

song = songs[2]
print(song)
print(song[1])

mayhem  = albums[3][3][2][1]
print(mayhem)

print(albums[3])
print(albums[3][3])
print(albums[3][3][2][1])


# # functions

# In[22]:


def multiply():
    result = 10.5 * 4
    return result

answer = multiply()
print(answer)


# In[27]:


def multiply(x, y):
    result = x * y
    return result

answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()

for val in range (1, 5):
    two_times = multiply(2, val)
    print(two_times)


# In[31]:


def multiply(x, y):
    result = x * y
    return result

def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1] == string
    

word = input("Please enter a word to check: ")
if is_palindrome(word):
    print("'{}'is a palindrome".format(word))
else:
    print("'{}'is not a palindorme".format(word))


# In[6]:


def multiply(x, y):
    result = x * y
    return result

def is_palindrome(string):
    # backwards = string[::1]
    # return backwards == string
    return string[::1].casefold() == string.casefold()


def palindorme_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    
    return string[::1].casefold() == string.casefold()


word = input("Please enter a word to check: ")
if palindorme_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a plaindrome".format(word))


# In[7]:


def multiply(x, y):
    result = x * y
    return result

def is_palindrome(string):
    # backwards = string[::1]
    # return backwards == string
    return string[::1].casefold() == string.casefold()


def palindorme_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::1].casefold() == string.casefold()
    return is_palindrome(string)
        
word = input("Please enter a word to check: ")
if palindorme_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a plaindrome".format(word))


# In[ ]:


import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)

    
highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess number 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == answer:
        print("Well Done, You guessed it") 
        break
    else:
        if guess < answer:
            print("Please guess Higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
        guess = int(input())
        if guess == answer:
            print("Well Done, You guessed it")
        else:
            print("Sorry!, You have not guessed correctly")


# # Banner

# In[3]:


def banner_text(text):
    screen_width = 80
    if len (text) > screen_width - 4:
        print("EEK!!")
        print("THE IS TO LONG TO FIT IN THE SPECIFIED WIDTH")
        
    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)
        

banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(" ")
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")

result = banner_text("Nothing is returned")
print(result)

numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
print(numbers.sort())


# In[11]:


def banner_text(text, screen_width=80):
    if len (text) > screen_width - 4:
        raise valueError("string {0} is larger then specified width {1}"
                        .format(text, screen_width)) 
        
    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)
        

banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There's something you've forgotten!")
banner_text("And that's to laugh and smile and dance and sing,")
banner_text(" ")
banner_text("When you're feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")

result = banner_text("Nothing is returned")
print(result)


# In[12]:


import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number".format(temp))


highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly")


# In[ ]:


import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{0} is not a valid number".format(temp))


highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly")


# In[2]:


import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{0} is not a valid number".format(temp))

def multiply(x, y):
     """
    Multiply 2 numbers.
 
    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.
 
    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result
 
 
def is_palindrome(string):
    """
    Check if a string is a palindrome.
 
    A palindrome is a string that reads the same forwards as backwards.
 
    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    return string[::-1].casefold() == string.casefold()
 
 
def palindrome_sentence(sentence):
    """
    Check if a sentence is a palindrome.
 
    The function ignores whitespace, capitalisation and
    punctuation in the sentence.
 
    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)

highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly")


# In[3]:


def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


# word = input("Please enter a word to check: ")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

answer = multiply(18, 3)
print(answer)


# In[2]:


# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def colour_print(text:str, effect: str) -> None:
    """
    Print 'text' using the ANSI Sequence to change colour, etc
    
    :param text: The text to print.
    :param effect: The effect we want. One of the constants
        define at the start of this module.
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)
    
colour_print("Hello, Red", RED)
# test that the colour was reset
print("This should be in the default terminal colour")
colour_print("Hello, Blue", BLUE)
colour_print("Hello, Yellow", YELLOW)
colour_print("Hello, Bold", BOLD)
colour_print("Hello, Underline", UNDERLINE)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, Black", BLACK)


# In[2]:


LOW = 1
HIGH = 65535

# print("Please think of a number between 1 and 1000")
# input("Press ENTER to start")


def guess_binary(answer, low, high):
    guesses = 1
    while True:
        # print("\tGuessing in the range {} to {}".format(low, high))
        guess = low + (high - low) // 2
        # high_low = input("My guess is {}. Should I guess higher or lower? Enter h or l, or c if my guess was correct."
        #                  .format(guess)).casefold()

        # if high_low == "h":
        if guess < answer:
            # I have to guess higher.  The low end of the range becomes 1 greater than the guess.
            low = guess + 1
        # elif high_low == "l":
        elif guess > answer:
            # I have to guess lower.  The high end of the range becomes 1 less than the guess.
            high = guess - 1
        # elif high_low == "c":
        elif guess == answer:
            # print("I got it in {} guesses!".format(guesses))
            # break
            return guesses
        # else:
        #     print("Please enter h, l or c")

        guesses += 1


correct_count = 0
max_guesses = 0
for number in range(LOW, HIGH + 1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, correct_count = number_of_guesses, 1
    elif number_of_guesses == max_guesses:
        correct_count += 1        
        
print("I guessed without being told {} times.Max {} guesses."
      .format(correct_count, max_guesses))


# # Fizzbuzz

# In[14]:


def fizz_buzz(number: int) -> str:
    """
    Play Fizz buzz
    
    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
         'buzz' if its's divisible by 5.
         'fizz buzz' if it's divisible  by both 3 and 5.
         The number, as a string, otherwise.
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)
    
    
input("Play Fizz Buzz.   Press ENTER to Start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You Lose, The Correct Answer was {}".format(correct_answer))
        break
else:
    print("Well Done, You reached {}".format(next_number))


# # star_examples

# In[20]:


numbers = (0, 1, 2, 3, 4, 5)

# print(numbers, sep=";")
# print(*numbers, sep=";")
# print(0, 1, 2, 3, 4, 5, sep=";")

def test_star(*args):
    print(args)
    for x in args:
        print(x)
        
test_star(0, 1, 2, 3, 4, 5)

print()
test_star()


# # Colour_print

# In[28]:


import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

def colour_print(text: str, *effects: str) -> None:
    """
    Print 'text' using the ANSI Sequence to change colour, etc
    
    :param text: The text to print.
    :param effect: The effect we want. One of the constants
        define at the start of this module.
    """
    effect_string = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)

colorama.init()
colour_print("Hello, Red", RED)
colour_print("Hello, Red in Bold", RED, BOLD )
# test that the colour was reset
print("This should be in the default terminal colour")
colour_print("Hello, Blue", BLUE)
colour_print("Hello, Blue reversed", BLUE, REVERSE)
colour_print("Hello, Blue reversed and underlined", BLUE, REVERSE, UNDERLINE)
colour_print("Hello, Yellow", YELLOW)
colour_print("Hello, Yellow bold", YELLOW, BOLD)
colour_print("Hello, Bold", BOLD)
colour_print("Hello, Underline", UNDERLINE)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, Black", BLACK)
colorama.deinit()


# # parameters_types

# In[31]:


def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:...{}, {}".format(p1, p2))
    print("var-positional (*args):..{}".format(args))
    print("keyword:.................{}".format(k))
    print("var-keyword:.............{}".format(kwargs))
    
func(1, 2, 3, 4, 5, 9, k=6, key1=7, key2=8)


# # dict_intro

# In[6]:


vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier can-am 250',
    'virago': 'Yahama XV250',
    'tenere': 'Yahama XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

my_car = vehicles['fiesta']
print(my_car)

commuter = vehicles['virago']
print(commuter)

learner = vehicles.get("ER5")
print(learner)


# In[18]:


vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier can-am 250',
    'virago': 'Yahama XV250',
    'tenere': 'Yahama XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple',
}

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

# Upgrade the Virago
vehicles["virago"] = "Yamaha XV535"
# delete vehicles["f1"]
result = vehicles.pop("fi", "You wish! Sell the Learjet and you might afford a racing car.")
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()
# for key in vehicles:
#    print(key, vehicles[key], sep=", ")
for key, value in vehicles.items():
    print(key, vehicles[key], sep=", ")


# # buy_computer_dict

# In[1]:


availabe_parts = {"1": "computer", 
                  "2": "moniter", 
                  "3": "keyboard",
                  "4": "mouse",
                  "5": "mouse pad",
                  "6": "HDMI Cable",
                  "7": "DVD drive"
                 }

current_choice = None
while current_choice != "0":
    if current_choice in availabe_parts:
        chosen_part = availabe_parts[current_choice]
        print(f"Adding {chosen_part}")
        
    current_choice = input("> ")


# In[5]:


availabe_parts = {"1": "computer", 
                 "2": "moniter", 
                 "3": "keyboard",
                 "4": "mouse",
                 "5": "mouse pad",
                 "6": "HDMI Cable",
                 "7": "DVD drive"
                }

current_choice = None
while current_choice != "0":
   if current_choice in availabe_parts:
       chosen_part = availabe_parts[current_choice]
       print(f"Adding {chosen_part}")
   else:
       print("Please add options from the list")
       for key, value in availabe_parts.items():
           print(f"{key}: {value}")
       print("0: to finish")
                 
   current_choice = input("> ")


# In[6]:


available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }
 
current_choice = None
computer_parts = []  # create an empty list
 
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part)
        else:
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part)
        print(f"Your list now contains: {computer_parts}")
    else:
        print("Please add options from the list:")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")
 
    current_choice = input("> ")


# In[7]:


available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
computer_parts = {}     # create an empty dictionary

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            # it's already in, so remove it
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary now contains: {computer_parts}")
    else:
        print("Please add options from the list")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")


# # contents

# In[2]:


pantry = {
    "chicken": 500,
    "lemon": 2,
    "cumin": 24,
    "paprika": 18,
    "chilli powder": 7,
    "yogurt": 300,
    "oil": 450,
    "onion": 5,
    "garlic": 9,
    "ginger": 2,
    "tomato puree": 125,
    "almonds": 75,
    "rice": 500,
    "coriander": 20,
    "lime": 3,
    "pepper": 8,
    "egg": 6,
    "pizza": 2,
    "spam": 1,
}

recipes = {
    "Butter chicken": [
        "chicken",
        "lemon",
        "cumin",
        "paprika",
        "chilli powder",
        "yogurt",
        "oil",
        "onion",
        "garlic",
        "ginger",
        "tomato puree",
        "almonds",
        "rice",
        "coriander",
        "lime",
    ],
    "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ],
    "Spam a la tin": [
        "spam",
        "tin opener",
        "spoon",
    ],
}


# # dict_methods

# In[5]:


d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

new_dict = dict.fromkeys(pantry_items)
print(new_dict)


# In[ ]:





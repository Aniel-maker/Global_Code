#print("hello")
#print('hello')

# Maths
4 + 5 
8 * 3 
4 / 3
4.0 / 3
3  + 5 * 9

#Strings
"abc" + "def"
"hello" + " " + "world"
"123" + "5"

#Variables
first = "hello"
second = "world"
first + " " + second
type(first)
#print(first)

#User input
#name = input("What is your name?")
#type(name)
#age = input("What is your age?")
#type(age)

#Problem to solve
# Converting  32 degrees to radians
import math
rad = (32/180) * 2 * math.pi
print("32 degrees in radian is " + str(rad) + " radians.")

# Surface area of a sphere
import math
radius = int(input("Enter the radius of your sphere (in cm)"))
volume = 4/3 * math.pi * (radius)**3
print("The volume of the sphere is " + str(volume) + " cm^3.")
surface_area = 4 * math.pi * (radius)**2
print("The surface area of the sphere is " + str(surface_area) + " cm^2.")

#Time of the day#
time = int(input("What is time?(in GMT)"))
if 6 <= time <12:
   print("Please it is in the morning.")
elif 12 <= time < 16:
     print("Please it is now in the afternoon.")
elif 16 <= time < 19:
     print("Please it is now evening")
else:
     print("Goodnight please.")

# Spliting a sentence
sentence = input("Enter any sentence")
split = sentence.split()
print(split)

# joining a list of words to form a sentence
words = ["Kofi", "is", "a", "boy."]
separator = " "
sentence = separator.join(words)
print(sentence)

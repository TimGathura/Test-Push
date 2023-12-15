#Lessons and tests on variable types and nuances involved
#Lesson1: A variable cannot start with a number, or contain a hyphen.
#Lesson2: type() shows the data type of the variable in question.
#Lesson3: Bool, Tuple () , List [] & Dict {} data types
#Lesson4: complex() How to turn an object to a complex number
#Lesson5: len() shows the length of a data object: Bool has no 
#Lesson6: x[0] How to get the first character in a string
#Lesson7: Whitespaces count in the length of a string.
#Lesson8: x[0] How to type a specific character in a string by referencing the position of the character in the string
#Lesson9: x[2:5] How to get characters in a string in a certain range of positions

var1 = ['one','two','three']
var2 = ('one', 'two', 'three')
var3 = {'name' : 'Timo' , 'Age' : 21 }
var4 = True
var5 = 'Hello, world. This is a test'
x = 10>9

print(type(var1), var1, len(var1))
print(type(var2), var2, len(var2))
print(type(var3), var3, len(var3))
print(type(var4), var4)
print(type(var5), len(var5) ,'This is character 1: ', var5[0], 'This is character 2: ', var5[6], 'To type "ello": ', var5[1:5] )
print(bool(x))
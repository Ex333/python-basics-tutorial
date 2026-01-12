#Lesson1
#The print() function displays text or values in the console (output).

print("Hello Wordl!")

## In this lesson, we use variables and print() to calculate the area of a circle.
pi=3.14
r=10
print(pi, r)
print(pi, r, pi*r*r)
print(pi,r,pi*r**2)
print('area of cycle with radius',r,'=',pi*r**2)

# By default, print() uses a space as a separator.
# You can change it using the 'sep' parameter.
#sep "\n" makes new line and "\t" is a tabulator 4x space
print(1,2,3)
print(1,2,3, sep='-')
print(1,2,3, sep='\n')
print(1,2,3, sep='\t')
# The '\a' escape character triggers a bell sound in the console. 
print('this is a bell: \a')
# '\u03A3' prints a Unicode character (Greek letter Sigma).
print("\u03A3")
#Backslash
print("\\")
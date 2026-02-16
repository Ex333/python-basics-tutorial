# ===============================
# LESSON: int vs float in Python
# ===============================

# int = integer = whole number (no decimal part)
age = 30
temperature = -5
score = 100

print("age:", age)
print("temperature:", temperature)
print("score:", score)

# check type
print(type(age))        # <class 'int'>


# -------------------------------
# float = number with decimals
# -------------------------------

price = 19.99
pi = 3.14
height = 1.80

print("price:", price)
print("pi:", pi)
print("height:", height)

# check type
print(type(price))      # <class 'float'>


# -------------------------------
# math with int
# -------------------------------

a = 10
b = 3

print("a + b =", a + b)     # addition
print("a - b =", a - b)     # subtraction
print("a * b =", a * b)     # multiplication
print("a // b =", a // b)   # integer division (no decimals)
print("a % b =", a % b)     # remainder


# -------------------------------
# math with float
# -------------------------------

x = 10.0
y = 3.0

print("x / y =", x / y)     # normal division
print("x * y =", x * y)


# -------------------------------
# int + float = float
# -------------------------------

result = a + price
print("a + price =", result)
print(type(result))         # float


# -------------------------------
# converting types
# -------------------------------

# int -> float
num_int = 5
num_float = float(num_int)
print(num_float, type(num_float))

# float -> int (cuts decimals!)
num_float2 = 9.9
num_int2 = int(num_float2)
print(num_int2, type(num_int2))   # result = 9


# -------------------------------
# common mistake
# -------------------------------

# user input is ALWAYS string!
user_age = input("Enter your age: ")
print(type(user_age))       # str

# convert string to int
user_age_int = int(user_age)
print(user_age_int + 1)


# -------------------------------
# summary
# -------------------------------

# int   -> whole numbers (1, 5, -3)
# float -> decimal numbers (1.5, 3.14, -0.5)
# int + float = float
# int(9.9) = 9   (decimal is removed)

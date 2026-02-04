# Python String Exercises – Monty Python & Basics
# Author: Mateusz Haldas

# 1–2. Store a copied fragment from the "Monty Python" section on Wikipedia.
# The text contains multiple lines, so triple quotes are used.

article = '''
Monty Python were a British surreal comedy group who created the sketch comedy
television show Monty Python's Flying Circus, that first aired on the BBC in 1969.
The group's influence on comedy has been compared to The Beatles' influence on music.
Their work has been called influential and innovative.
'''

# 3. Convert the text to uppercase and display it in one instruction.
print(article.upper())

# 4. Replace 'monty' with 'flying'.
# The text is first converted to lowercase because Python is case-sensitive.
print(article.lower().replace('monty', 'flying'))

# 5. Split the text into words using spaces and display the list.
print(article.split(' '))

# 6. Display how many times the word "python" appears in the text.
python_count = article.lower().count('python')
print(f"word python appears {python_count} times")

# 7. Display text with backslashes.g
print("to print the \\ you need to put \\ twice in your text like this: \\\\")

# 8. Display the same text in two ways.

# Using single quotes
print('The best hits of \'80s!!!')

# Using double quotes
print("The best hits of '80s!!!")

# 9. Mini currency exchange calculator.

amountPLN = 234

print("cur\texchange\tamount")
print("USD\t3.65\t\t", amountPLN / 3.65)
print("EUR\t4.23\t\t", amountPLN / 4.23)

# 10. Declare a variable with a numeric value stored as text.
ValueAsText = '123.45'

# 11. Declare a float factor.
factor = 1.23

# 12. Display the calculation result.
# The text value is converted to float before multiplication.
print(
    "value is", ValueAsText,
    "factor is", factor,
    "value*factor=",
    float(ValueAsText) * factor
)

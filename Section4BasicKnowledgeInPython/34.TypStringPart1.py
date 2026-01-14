# Create a string variable
text = "This is a text"

# Print the value and its type
print(text)
print(type(text))

# Check if the string ends with "text"
print(text.endswith("text"))

# Check if the string starts with "This"
print(text.startswith("This"))

# Find the position of the substring "text"
position = text.find("text")
print(f'"text" was found at index {position}')

# Find the substring "is" starting from index 3
position2 = text.find("is", 3)
print(f'"is" was found at index {position2} when starting search from index 3')

# Replace "text" with "sample"
new_text = text.replace("text", "sample")
print(new_text)

# Replace only the first occurrence of "is" with "was"
new_text2 = text.replace("is", "was", 1)
print(new_text2)

somethinglikenumer = "12345"
# Check if the string is digits
print(somethinglikenumer.isdigit())
# Check if the string is decimal
print(somethinglikenumer.isdecimal())
# Check if the string is alphabetic
print(somethinglikenumer.isalpha())
# Check if the string is alphanumeric
print(somethinglikenumer.isalnum())
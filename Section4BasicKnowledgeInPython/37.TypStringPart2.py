drive = "C:\\"
folder = "Users\\Public\\Documents\\"
filename = "report.txt"
full_path = drive + folder + filename
print(full_path)

# Using raw string to avoid escape sequences
raw_path = r"C:\Users\Public\Documents\report.txt"
print(raw_path)# Concatenating strings to form a file path

#Syntax error due to unescaped single quote
#just_test = 'simple text's'

just_test = "simple text's"
print(just_test)

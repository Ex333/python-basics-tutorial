# ==========================================
# LESSON: STRING FORMATTING IN PYTHON
# ==========================================

# -------- 1. OLD STYLE FORMATTING (%) --------

# %s = placeholder for a string
message1 = 'Processing file %s'
print(message1 % ('file_1.txt'))

# %s = string, %d = integer
message2 = 'File %s has size %d KB'
print(message2 % ('file1.txt', 100))


# -------- 2. WIDTH & ALIGNMENT (OLD STYLE) --------

# %20s = string, width 20 characters (right-aligned)
# %10d = integer, width 10 characters (right-aligned)
message3 = 'File %20s has size %10d KB'
print(message3 % ('file1.txt', 100))


# -------- 3. NEW STYLE FORMATTING (.format()) --------

# {0:s} = first argument as string
message4 = 'Processing file {0:s}'
ms4 = message4.format('file1.txt')
print(ms4)

# {0:s} = string, {1:d} = integer
message5 = 'File {0:s} has size {1:d}'
ms5 = message5.format('file1.txt', 100)
print(ms5)


# -------- 4. WIDTH & ALIGNMENT (.format()) --------

# {0:20s} = string, width 20
# {1:10d} = integer, width 10
message6 = 'File {0:20s} has size {1:10d} KB'
ms6 = message6.format('file1.txt', 100)
print(ms6)


# -------- 5. MODERN PYTHON: F-STRINGS (RECOMMENDED) --------

filename = 'file1.txt'
size = 100

# f-string with width formatting
print(f'File {filename:20s} has size {size:10d} KB')


# ==========================================
# END OF LESSON
# ==========================================

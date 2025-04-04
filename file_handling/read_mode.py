#Reading a File
#File ko read karne ke liye read() function ya readline() function ka use hota hai.

file = open('filename.txt', 'r')  # Open file in read mode

# Reading entire file content at once
content = file.read()
print(content)

file.close()  # Always close the file after use


# Agar file me bohot zyada data hai, aur aapko ek line-by-line read karna hai, to readline() ya readlines() ka use kar sakte hain:

# Read line by line
file = open('filename.txt', 'r')
line = file.readline()  # Reads one line at a time
while line:
    print(line, end='')
    line = file.readline()  # Read next line
file.close()


#Ya phir readlines() use kar sakte hain, jo file ki saari lines ek list ke form me return karte hain:


file = open('filename.txt', 'r')
lines = file.readlines()  # Read all lines into a list
print(lines)
file.close()
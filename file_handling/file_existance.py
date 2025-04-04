# File Existence Check

# Agar aapko pehle check karna ho ke file exist karti hai ya nahi, to os module ka exists() function use kar sakte hain.

import os

if os.path.exists('filename.txt'):
    print("File exists.")
else:
    print("File doesn't exist.")



# Example of fole handling

# Write to a file
with open('fruit.txt', 'w') as file:
    file.write("Apples\nBananas\nOranges")

# Read from a file
with open('fruit.txt', 'r') as file:
    content = file.read()
    print("Fruits in the file:")
    print(content)

# Append to a file
with open('fruit.txt', 'a') as file:
    file.write("Grapes\n")

# Read again to see appended content
with open('fruit.txt', 'r') as file:
    content = file.read()
    print("Updated Fruits in the file:")
    print(content)

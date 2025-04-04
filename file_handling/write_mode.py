# Writing to a File
# File me kuch likhne ke liye aap write() function ka use karte hain

file = open('filename.txt', 'w')  # Open file in write mode
file.write("Hello, this is a new file.\n")  # Write to file
file.write("This is another line of text.")  # Write more content
file.close()




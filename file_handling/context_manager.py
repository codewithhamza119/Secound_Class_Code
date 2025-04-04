# Context Manager (with statement)


#File Closing
#Har file ko open karne ke baad, usay close karna bohot zaroori hota hai. Agar aap file ko properly close nahi karenge, to file lock ho sakti hai aur aap future me usay access nahi kar paayenge.

file = open('filename.txt', 'r')
lines = file.readlines()  # Read all lines into a list
print(lines)
file.close()  # Close the file after you are done with it

# Aap with statement use kar ke file automatically close kar sakte hain jab kaam complete ho jaye. Isse file ko close karne ka tension nahi hota.

with open('filename.txt', 'r') as file:
    content = file.read()
    print(content)  # File automatically closes after block ends



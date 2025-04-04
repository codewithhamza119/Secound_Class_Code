#  Agar file pehle se exist karti hai aur w mode use kar rahe hain, to purani file ka data replace ho jayega. Agar aap chahein ke naya content purane content ke baad add ho, to a mode (append mode) ka use karein.

file = open('filename.txt', 'a')  # Open file in append mode
file.write("\nThis is an appended line.")  # Append content
file.close()

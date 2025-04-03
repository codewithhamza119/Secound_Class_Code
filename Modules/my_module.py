# # Modules Python ke code ko organize aur re use karne ka tareqa hain 1 module 1 file hota hai jisme related functions classes aur variables hote hain Python me modules ka use code ko logical blocks me divide karne ke liye kiya jata hai taake aap apne code ko efficiently maintain or re use kar sakein.


#  What is a Module?
# Module 1 Python file hoti hai jo .py extension ke saath save ki jati hai. Agar aapko apne program me kisi particular functionality ko bar-bar use karna hai to us functionality ko 1 module me store karne ke baad me use kiya ja sakta hai

#  How to Use a Module?
# Python me module ko import kar ke use kiya jata hai Hum import karte waqt 1 module ka naam likhte hain or uske andar ke functions classes etc ko access kar sakte hain

#  How to Create a Module:
# Create a Python File (Module):
# Sabse pehle ek Python file banao jisme aap apni functionality define karenge Jaise ke 1 module my_module.py bana kar usme kuch functions likhna.


# Examples

# my_module.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# Import the Module in Another Python File

# Ab aap apne program me module ko import kar ke uske functions ko use kar sakte hain


# Garbage Collection ka kaam unused memory ko free karna hota hai Jab koi object use nahi hota to Python ka Garbage Collector (GC) usko automatically delete kar deta hai taake memory waste na ho Python Reference Counting + Cyclic Garbage Collector ka use karta hai memory ko manage karne ke liye.


import gc  # pehle ham Garbage Collection module import krte hain.
import sys  # Reference count check karne ke liye module

class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} object bana!")

    def __del__(self):
        print(f"{self.name} object delete ho gaya!")

# Object create karte hain
obj = MyClass("Hamza")

# Object ka reference count check karte hain
print("Reference Count:", sys.getrefcount(obj))  

# Manually object delete ham del krke krte hain.
del obj  

# Garbage Collector ko manually call istrah krte hain
gc.collect()  # Zyada cases me yeh automatic hota hai

# Positional-only arguments wo hote hain jo sirf specific order me pass kiye ja sakte hain aur unko keyword arguments ki tarah use nahi kar sakte. Python me / (forward slash) ka use karke positional-only arguments enforce kiye ja sakte hain.

def greet(name, age, /):  # `/` ka matlab hai ye sirf position se pass honge
    print(f"Hello {name}, you are {age} years old.")

# Sahi tarika: Arguments ko position se pass karna
greet("Hamza", 25)  # Output: Hello Hamza, you are 25 years old.

# Ghalat tarika: Keyword arguments use karna
# greet(name="Hamza", age=25)  # ❌ Ye TypeError dega


# Jab hum / ka use karte hain, iska matlab hota hai is se pehle jo arguments hain, unko sirf position se pass karna hoga.

# Keyword arguments ka use nahi ho sakta.

# "greet("Hamza", 25)" chalega, lekin "greet(name="Hamza", age=25)" error dega.
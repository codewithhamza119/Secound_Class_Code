# Default arguments wo arguments hote hain jinka default value function definition me diya jata hai Agar function call me wo argument na diya jaye to default value use hoti hai



def greet(name, age=18):
    print(f"Hello {name}, you are {age} years old.")

# Default argument use karke function call
greet("Hamza")  # Output: Hello Hamza, you are 18 years old.

# Argument specify karte hue
greet("Sara", 19)  # Output: Hello Sara, you are 19 years old.

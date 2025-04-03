# Aap apne function me positional arguments, default arguments, *args, aur **kwargs ko combine kar sakte hain. Lekin unko specific order me dena parta hai

# Positional Arguments

# Default Arguments

# *args (arbitrary positional arguments)

# **kwargs (arbitrary keyword arguments)


def display_info(name, age=20, *hobbies, **additional_info):
    print(f"Name: {name}")
    print(f"Age: {age}")
    
    if hobbies:
        print("Hobbies:", ", ".join(hobbies))
    
    if additional_info:
        for key, value in additional_info.items():
            print(f"{key}: {value}")

# Function call with all types of arguments
display_info("Hamza", 25, "Reading", "Coding", city="Karachi", profession="Developer")

# Output:
# Name: Hamza
# Age: 25
# Hobbies: Reading, Coding
# city: Karachi
# profession: Developer

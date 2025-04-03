# Keyword arguments me arguments ko function me pass karte waqt ap parameter names specify karte hain Isse aapko values ko exact order me pass karne ki zarurat nahi parti Aap name=value ke format me argument pass karte hain.


def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")

# Keyword arguments ke through function call
greet(age=25, name="Hamza")  # Output: Hello Hamza, you are 25 years old.

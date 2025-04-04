# (a) Arbitrary Positional Arguments (*args)
# Agar aapko function me kisi bhi number of positional arguments ko pass karna ho to aap *args ka use kar sakte hain args 1 tuple ban jata hai jisme saare extra arguments store ho jate hain.


def greet(*names):
    for name in names:
        print(f"Hello {name}!")

# Multiple arguments pass karte hain
greet("Hamza", "Sara", "Hamza Swati")  
# Output: 
# Hello Hamza!
# Hello Sara!
# Hello Hamza Swati!



# (b) Arbitrary Keyword Arguments (**kwargs)

# Agar aapko kisi function me any number of keyword arguments pass karne ho to aap **kwargs ka use karte hain. kwargs 1 dictionary ban jata hai jisme key-value pairs store hote hain.


def show_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

# Keyword arguments pass karte hain
show_info(name="Hamza", age=25, city="Karachi")
# Output:
# name: Hamza
# age: 25
# city: Karachi


# # Tuples in Python

# # Tuples ek immutable data structure hote he jo Python me sequences ko store karne ke liye use kiye jate he Tuples ka use kab karna chahiye aur 1 karna chaye, isko samajhna bohot zaroori he taake ap apne code me efficient aur correct decisions le sako


# Why Use Tuples?
# Immutability (Unchangeable):
# Tuples me 1 baar value set kar dene ke baad unko modify nahi kiya ja sakta Isliye agar aapko kisi sequence ko safe rakhna ho jisme changes nahi chaye to tuple use karna acha he Isse aap accidental modifications se bach sakte he.

# Faster than Lists:
# q ke tuples immutable hote hain isliye lists ki comparison me faster hote he khas kar jab aapko sirf read operations perform karni hoti hen

# Use as Dictionary Keys:
# Tuples ko aap dictionary ke keys ke roop me use kar sakte hain lekin lists ko aap dictionary keys ke roop me use nahi kar sakte Yeh hashable hote hai isliye unka use dictionary ke key ke shakal me ho sakta he

# Memory Efficient:
# Tuples ko lists ke comparison me kam memory ki zaroorat hoti hai isliye jab aapko large data structures ka use karna ho lekin data ko modify nahi karna ho to tuples best option hain.

# Multiple Values Return:
# Functions me multiple values return karte waqt tuples ka use hota hai q ke tuples unchangeable hote hain ye safe way hai multiple related values ko ek saath return karne ka.

# When to Use Tuples?
# Tuples ko use karne ke kuch common scenarios:

# Data Integrity (When Data Should Not Change):
# Jab aapko data ko modify nahi karna ho jese coordinates fixed settings etc to tuple use karna acha rahega

# Performance (When Speed is Important):
# Jab aapko read-only data ka use karna ho aur speed matter kare to tuples lists se zyada fast hote he to use krsakte he.

# Multiple Values from Functions:
# Jab aapko 1 function se multiple values return karni ho to tuple ka use karna better practice hai

# As Keys in a Dictionary:
# Jab aapko compound keys chaye hon jese coordinates ((x, y)), to tuples ko keys ke shakal me use kar sakte hen.


# Chalen code examples bhi deklete hain take behtareen samaj me ajayen.


# 1. Immutability (Change Prevention)

# Tuple ka use krte hain
my_tuple = (1, 2, 3)

# Try karte hain change karne ka
try:
    my_tuple[0] = 10  # Error aayega q ke tuple immutable hai
except TypeError:
    print("Tuple me modification allowed nahi hai")


    # 2. Use as Dictionary Keys

    # Tuple ko dictionary key ke shakal me use karte hain
my_dict = {}
my_dict[(1, 2)] = "Point 1"
my_dict[(3, 4)] = "Point 2"

# Output
print(my_dict)


# 3. Multiple Values Return

# Ye function tuple return krega
def get_coordinates():
    return (10, 20)

# Is function se multiple value return krwate hain.
x, y = get_coordinates()

# Output
print("X:", x)
print("Y:", y)# # Tuples in Python

# # Tuples ek immutable data structure hote he jo Python me sequences ko store karne ke liye use kiye jate he Tuples ka use kab karna chahiye aur 1 karna chaye, isko samajhna bohot zaroori he taake ap apne code me efficient aur correct decisions le sako


# Why Use Tuples?
# Immutability (Unchangeable):
# Tuples me 1 baar value set kar dene ke baad unko modify nahi kiya ja sakta Isliye agar aapko kisi sequence ko safe rakhna ho jisme changes nahi chaye to tuple use karna acha he Isse aap accidental modifications se bach sakte he.

# Faster than Lists:
# q ke tuples immutable hote hain isliye lists ki comparison me faster hote he khas kar jab aapko sirf read operations perform karni hoti hen

# Use as Dictionary Keys:
# Tuples ko aap dictionary ke keys ke roop me use kar sakte hain lekin lists ko aap dictionary keys ke roop me use nahi kar sakte Yeh hashable hote hai isliye unka use dictionary ke key ke shakal me ho sakta he

# Memory Efficient:
# Tuples ko lists ke comparison me kam memory ki zaroorat hoti hai isliye jab aapko large data structures ka use karna ho lekin data ko modify nahi karna ho to tuples best option hain.

# Multiple Values Return:
# Functions me multiple values return karte waqt tuples ka use hota hai q ke tuples unchangeable hote hain ye safe way hai multiple related values ko ek saath return karne ka.

# When to Use Tuples?
# Tuples ko use karne ke kuch common scenarios:

# Data Integrity (When Data Should Not Change):
# Jab aapko data ko modify nahi karna ho jese coordinates fixed settings etc to tuple use karna acha rahega

# Performance (When Speed is Important):
# Jab aapko read-only data ka use karna ho aur speed matter kare to tuples lists se zyada fast hote he to use krsakte he.

# Multiple Values from Functions:
# Jab aapko 1 function se multiple values return karni ho to tuple ka use karna better practice hai

# As Keys in a Dictionary:
# Jab aapko compound keys chaye hon jese coordinates ((x, y)), to tuples ko keys ke shakal me use kar sakte hen.


# Chalen code examples bhi deklete hain take behtareen samaj me ajayen.


# 1. Immutability (Change Prevention)

# Tuple ka use krte hain
my_tuple = (1, 2, 3)

# Try karte hain change karne ka
try:
    my_tuple[0] = 10  # Error aayega q ke tuple immutable hai
except TypeError:
    print("\nTuple me modification allowed nahi hai\n")


    # 2. Use as Dictionary Keys

    # Tuple ko dictionary key ke shakal me use karte hain
my_dict = {}
my_dict[(1, 2)] = "Point 1"
my_dict[(3, 4)] = "Point 2"

# Output
print(f"\n{my_dict}\n")


# 3. Multiple Values Return

# Ye function tuple return krega
def get_coordinates():
    return (10, 20)

# Is function se multiple value return krwate hain.
x, y = get_coordinates() 
# ek trha se yaha unpacking bh ho rhi he qk yaha tuple me (10, 20) return ho rha h to agr dekha jae to ye x,y = (10,20) he

# Output
print("X:", x)
print("Y:", y)




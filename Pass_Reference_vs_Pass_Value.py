# Python me Pass by Reference aur Pass by Value ke concepts thora sa different hain Python me everything is an object aur jab hum kisi function me variable pass karte hain to Python internally pass by object reference ka use karta hai yani ke agar object mutable hai jaise list ya dictionary to usme changes reflect ho sakte hain lekin agar object immutable hai (jaise integer, string), to koi changes nahi honge.


#  Pass by Value

# Pass by Value me function ko jo value pass hoti hai wo directly copied hoti hai Matlab agar hum immutable objects (jaise integer, string) ko function me pass karte hain to function ke andar value change karna possible nahi he.


 # Pass by Reference

# Pass by Reference me function ko memory address pass hota hai Agar hum mutable objects (jaise list, dictionary) ko pass karte hain to function ke andar changes original object me reflect hoti he.


# 1. Pass by Value (Immutable Object)

def modify_value(x):
    x = 10  # Value change karte hai

# Function me integer pass karte hai
num = 5
print("Before Function:", num)
modify_value(num)
print("After Function:", num)  # `num` ki value change nahi hogi


# Explanation:
# Yaha pe num (integer) pass kiya he mene, or integers immutable hote he, is liye original num ki value change nahi hoti

# 2. Pass by Reference (Mutable Object)

def modify_list(lst):
    lst.append(4)  # List me element add karte he

# Function me list pass karte he
my_list = [1, 2, 3]
print("Before Function:", my_list)
modify_list(my_list)
print("After Function:", my_list)  # `my_list` me changes reflect honge


# Explanation:
# Yaha pe my_list (list) pass ki hai Lists mutable hote he is liye function ke andar original list me changes reflect ho gaye






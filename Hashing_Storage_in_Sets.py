# Python me sets ko internally hash tables ke shakal me implement kiya jata sakta he jab hum koi item set me add karte hai Python us item ka hash value calculate karta hai aur us hash value ko storage location ki trah  use karta hai Is process se fast lookup aur unique elements ensure hoti hai



# Jab ham koi element add karte hai set me Python us element ki hash value calculate karta hai

# Hash value ko bucket me map kar diya jata hai

# Agar hash value pe koi aur element pehle se exist kar raha ho to collision hota hai lekin Python usko khud hi handle krleta hai

# Sets me elements unique hote hai is liye duplicate values ko ignore kar diya jata hai


# Set ka example bnate he yha ham
my_set = set()

# Kuch elements add karte hain
my_set.add("Hamza")  # "Hamza" ka hash calculate hoga
my_set.add("Areeba")    # "Areeba" ka hash calculate hoga
my_set.add("Hamza")  # "Hamza" ko duplicate hone ki wajah se add nahi karega

# Output
print(my_set)  # Set me unique elements hi honge

# Check karte hain agar "Hamza" ka hash value kya hai
print("Hash value of Hamza:", hash("Hamza"))
print("Hash value of Ali:", hash("Ali"))

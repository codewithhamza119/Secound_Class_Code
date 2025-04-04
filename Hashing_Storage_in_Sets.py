# Hashing 1 data security aur fast data retrieval technique hai jisme 1 fixed-size unique value (hash) generate hoti hai kisi bhi input se Python me hashing ke liye hash() function aur hashlib module use hota hai.

#Rehashing ka matlab hai dobara hashing karna jab kisi bhi wajah se hash value change karni ho jaise ke collision handling ya security improve karna.


# Hash function ka istemal kar ke hash value generate krte hain
text = "Hamza"
hash_value = hash(text)

# Output
print("Original Text:", text)
print("Hash Value:", hash_value)



# -------------------------------------# 

import hashlib  # Secure Hashing ke liye module import krte hain

# koi bhi text define krden
text = "Hamza"

# SHA-256 hashing algorithm ka use kar ke hash generate karte hain
hash_object = hashlib.sha256(text.encode())  
hash_hex = hash_object.hexdigest()  # Hexadecimal format me output

# Output
print("Original Text:", text)
print("SHA-256 Hash:", hash_hex)


#Note: hashlib ka use password hashing aur security ke liye hota hai q ke hash() function har bar different output de sakta hai (randomized hash).



#-------------------------------------#


import hashlib

# Original text
text = "Hamza"

# Pehle SHA-256 se hash generate karte hain
hash1 = hashlib.sha256(text.encode()).hexdigest()

# Phir Rehashing karte hain (MD5 Algorithm ka use kar ke)
hash2 = hashlib.md5(text.encode()).hexdigest()

# Output
print("SHA-256 Hash:", hash1)
print("MD5 Rehashed Value:", hash2)


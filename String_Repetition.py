# String repetition ka matlab hai 1 string ko multiple dafa repeat karna Python me ye * operator se asaan tareeke se kiya jata hai.


# String repetition ka basic tareeqa

# Ek simple string define karte hain
text = "Hello "

# String ko 3 dafa repeat karwate he * ki madad se
repeated_text = text * 3  

# Output
print(repeated_text)  

# -------------------------- #

# Loop ka istemal kar ke bhi string repetition kiya ja sakta hai
repeat_count = 4  # Yaha ham define krte hain ke kitni dafa repeat krna he

for i in range(repeat_count):
    print(text)  # Har dafa naya line print hoga

# -------------------------- #

# Agar user se input lena ho ke kitni dafa repeat karna hai
user_text = input("Koi text likho: ")  # User text 
repeat_times = int(input("Kitni dafa repeat karna chahte ho? "))  # Yaha ham user se define krwate hain ke kitni dafa repeat krna he

# Output
print(user_text * repeat_times)

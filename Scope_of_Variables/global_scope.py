# Global Scope (Har Jaga Accessible): Jo variable function ke bahar define hota hai, wo pura program me accessible hota hai, lekin agar tum usko function ke andar change karna chaho to global keyword lagana parega.

z = 30  # Global variable

def my_function():
    #global z  # Is se hum function ke andar z ko modify kar sakte hain
    # z += 10
    print("Inside Function:", z)

my_function()
print("Outside Function:", z)
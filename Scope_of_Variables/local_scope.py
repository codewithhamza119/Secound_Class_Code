# Local Scope: Jo variable kisi function ke andar define hota hai, wo sirf us function ke andar accessible hota hai. Bahar uska koi access nahi hota.

def my_function():
    x = 10  # Local variable
    print(x)  # Ye chalega

my_function()
# print(x)  # Ye error dega, kyunki x function ke bahar accessible nahi hai.
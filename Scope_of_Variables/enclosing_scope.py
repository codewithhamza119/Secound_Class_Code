# Enclosing Scope (Non-Local Scope): Agar ek function ke andar dusra function ho, to andar wala function (inner function) bahar wale function ke variables ko access kar sakta hai, lekin change nahi kar sakta jab tak nonlocal keyword use na karein.

def outer_function():
    y = 20  # Enclosing (Non-Local) variable
    
    def inner_function():
       # nonlocal y  # `nonlocal` ka matlab ke y ko modify kar sakte hain
       # y += 5
        print("Inner Function:", y)
    
    inner_function()
    print("Outer Function:", y)

outer_function()
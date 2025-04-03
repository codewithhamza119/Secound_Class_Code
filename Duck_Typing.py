# Duck Typing 1 concept hai jo Python ki Dynamic Typing ka hissa hai Iska matlab hai ke agar koi object ek particular behavior ko follow karta hai to uska specific type hona zaroori nahi Agar koi object 1 duck ki tarah chalta bolta aur dikhai deta hai  to hum use duck hi maan lete hain Isi wajah se is concept ko Duck Typing kehte hain.


# Duck Typing ka concept samajhne ke liye ek function define karte hain

class Duck:
    def speak(self):
        return "Quack Quack!"  # Duck ka sound

class Dog:
    def speak(self):
        return "Bark Bark!"  # Dog ka sound

# Yeh function kisi bhi object ko accept karega jo 'speak()' method rakhta ho
def make_sound(animal):
    print(animal.speak())

# Objects banate hain
duck = Duck()
dog = Dog()

# Function ko call karte hain
make_sound(duck)  # Output: Quack Quack
make_sound(dog)   # Output: Bark Bark

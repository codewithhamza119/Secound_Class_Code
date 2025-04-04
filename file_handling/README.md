# File Handling

**File handling ka matlab hota hai ke aap apne Python program me kisi file ke sath interact kar sakein. Jaise ke file ko read karna, write karna, append karna, ya usme changes karna. Python me file handling bohot asaan hai aur Python built-in functions provide karta hai is kaam ke liye.**

## Basic File Handling Operations:

**Python me file handling ke liye built-in function open() use hota hai, jo file ko open karta hai aur uske baad aap read, write, ya append operations kar sakte hain.**

### 1. Opening a File
**File ko open karne ke liye aap open() function use karte hain. open() function mein do main cheezein pass karni padti hain:**

**File ka naam ya path**

**Mode (jo yeh batata hai ke file ko kis purpose ke liye open kar rahe hain)**

```python
file = open('filename.txt', 'r')  # 'r' mode means read-only


## Modes in File Handling:

**'r' - Read: Yeh mode file ko sirf read karne ke liye open karta hai. Agar file nahi milti to error aati hai.**

**'w' - Write: Yeh mode file ko likhne ke liye open karta hai. Agar file already exist karti hai, to uski purani contents overwrite ho jati hain.**

**'a' - Append: Yeh mode file me naya data append (add) karne ke liye use hota hai. Agar file nahi hai, to nayi file ban jaati hai.**

**'x' - Exclusive: Yeh mode sirf tab file create karega agar wo file pehle se exist nahi karti.**

**'b' - Binary: Agar aap binary files (jaise images, videos, etc.) ke saath kaam kar rahe hain, to aap is mode ka istemal karte hain.**

**'t' - Text: Yeh default mode hai aur text files ke liye use hota hai.**
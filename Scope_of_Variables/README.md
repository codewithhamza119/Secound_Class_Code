# Scope of Variables in Python

Scope ka matlab hai kis jagah ek variable accessible hai aur kis jagah nahi. Python me variables ke scope 4 types ke hote hain: 

## 1. Local Scope

## 2. Enclosing Scope (Non-Local Scope)

## 3. Global Scope

## 4. Built-in Scope


## Scope Hierarchy (LEGB Rule)

Agar ek variable multiple scopes me ho to Python priority is order me dekhta hai (LEGB Rule):

**L (Local) → Function ke andar jo variable define ho wo sabse pehle check hota hai.**

**E (Enclosing) → Agar function ke andar function ho to enclosing function ka scope dekha jata hai.**

**G (Global) → Agar variable local aur enclosing scope me na mile to global variables check hote hain.**

**B (Built-in) → Agar kisi bhi scope me variable na mile to Python apne built-in functions ko check karta hai.**
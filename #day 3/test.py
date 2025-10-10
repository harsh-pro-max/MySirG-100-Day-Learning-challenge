# Python me "soft keywords" wo hote hain jo specific context me keyword ki tarah behave karte hain,
# lekin normal situation me unhe variable name ke roop me bhi use kar sakte hain.

# Example: match, case, type, etc. (Python 3.10+ me introduce hue)
# Ye normal keyword jaise strict nahi hote jaise "if", "for", "while" hote hain.

# Jaise niche example me 'match' soft keyword ki tarah use ho raha hai:
value = 2

match value:      # yahan 'match' ek soft keyword ki tarah use hua (pattern matching ke liye)
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")

# Lekin agar mai isse normal variable name bana du to ye bhi valid hai:
match = "Hello Soft Keyword!"   # yahan ye keyword nahi, ek variable ban gaya
print(match)

# → Iska matlab: soft keywords Python ke grammar ke hisaab se context-dependent hote hain,
# yani kabhi keyword jaise behave karte hain aur kabhi simple variable name jaise.

# use of type
type point = tuple[float,float]
type list_of_points= list[point]
p1:point=(3.0,4.5)
p2:point=(5.0,90.2)
p3:point=(1.0,-0.5)
mylist:list_of_points=[p1,p2,p3]
print(mylist)
print(type(p1))
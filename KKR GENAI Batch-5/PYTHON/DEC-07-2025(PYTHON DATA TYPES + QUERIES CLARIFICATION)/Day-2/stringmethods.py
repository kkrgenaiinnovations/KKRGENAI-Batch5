"""
====================================================
    PYTHON STRING METHODS 
====================================================
"""

s = "  Hello Python World  "
text = "hello world"
upper_text = "HELLO WORLD"
mixed = "PyThOn Is CoOL"
num = "12345"
alnum = "Python3"
space = "   "
words = "Python is fun"
sample = "banana"
csv = ["Python", "is", "awesome"]
multi = "line1\nline2\nline3"
unicode_num = "⅚"        # numeric fraction

print("\n========== 1. CASE CONVERSION ==========\n")

print(s.lower())              # hello python world
print(s.upper())              # HELLO PYTHON WORLD
print(text.capitalize())      # Hello world
print(text.title())           # Hello World
print(mixed.swapcase())       # pYtHoN iS cOol
print("straße".casefold())    # strasse (strong lowercase)

print("\n========== 2. STRIP & REMOVE ==========\n")

print(s.strip())                       # 'Hello Python World'
print(s.lstrip())                      # 'Hello Python World  '
print(s.rstrip())                      # '  Hello Python World'
print("unittest".removeprefix("unit")) # 'test'
print("filename.txt".removesuffix(".txt"))  # filename

print("\n========== 3. SEARCH & FIND ==========\n")

print(sample.find("na"))        # 2
print(sample.rfind("na"))       # 4
print(sample.index("ba"))       # 0
# print(sample.index("xy"))     # ValueError
print(sample.count("a"))        # 3
print(sample.rindex("na"))      # 4

print("\n========== 4. BOOLEAN CHECK METHODS ==========\n")

print("hello".isalpha())        # True
print(num.isdigit())            # True
print(alnum.isalnum())          # True
print(unicode_num.isnumeric())  # True (¼, ⅚ etc)
print(num.isdecimal())          # True only 0–9
print("var_name".isidentifier()) # True (valid variable)
print(upper_text.isupper())     # True
print(text.islower())           # True
print("Hello World".istitle())  # True
print(space.isspace())          # True
print("Python3".isascii())      # True
print("∞".isascii())            # False

print("\n========== 5. SPLIT & JOIN ==========\n")

print(words.split())                 # ['Python','is','fun']
print("a,b,c".split(","))            # ['a','b','c']
print("one-two-three".rsplit("-",1)) # ['one-two','three']
print(multi.splitlines())            # ['line1','line2','line3']

print(" ".join(csv))                 # Python is awesome
print("-".join(csv))                 # Python-is-awesome

print("\n========== 6. REPLACE & MODIFY TEXT ==========\n")

print(text.replace("world","Python"))   # hello Python
print("\tPython".expandtabs(4))         # '    Python'

table = str.maketrans({"a":"@", "e":"3"})
print("peace".translate(table))         # p3@c3

print("\n========== 7. SLICING (IMPORTANT) ==========\n")

t = "PYTHON"

print(t[0:3])     # PYT
print(t[:4])      # PYTH
print(t[2:])      # THON
print(t[-3:])     # HON
print(t[::-1])    # reverse → NOHTYP
print(t[::2])     # PYO

# Exceptions:
# t[10] → IndexError
# t[2:50] → Safe, returns 'THON'

print("\n========== 8. ALIGNMENT / FORMATTING ==========\n")

print("Python".center(12,"*"))    # ***Python***
print("Python".ljust(10,"-"))     # Python----
print("Python".rjust(10,"-"))     # ----Python
print("42".zfill(5))              # 00042

print("My name is {}".format("Sam"))
print("Result = {} + {} = {}".format(2,3,5))
print(f"Square = {6**2}")         # f-string style
print("Value = %.2f"%3.14159)     # old formatting
print("Coordinates: {x}, {y}".format_map({"x":10,"y":20}))

print("\n========== 9. ENCODING/DECODING ==========\n")

encoded = "hello".encode()  # bytes
print(encoded)              # b'hello'
print(encoded.decode())     # hello

print("\n====================================================")
print(" ALL STRING METHODS COVERED ✔")
print("====================================================\n")

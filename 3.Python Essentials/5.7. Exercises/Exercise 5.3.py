string = input("Enter a string: ")

x = 0
for letter in string:
    if letter.isupper():
        x += 1
print(x)
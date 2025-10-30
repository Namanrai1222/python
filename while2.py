while True:
    print("who are you?")
    name=input()
    if name!="Naman":
        continue
    print("Hello Naman. What is the password? (It is a fish)")
    password=input()
    if password=="swordfish":
        break
print("Access granted.")
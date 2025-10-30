while True:
    print("Please type your name:")
    myname=input()
    if myname=="your name":
      print("Hello, "+myname)
      break
    else:
      print("Try again!")
print("It is good to meet you, "+myname)
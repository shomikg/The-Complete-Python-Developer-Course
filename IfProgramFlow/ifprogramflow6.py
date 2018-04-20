parrot = "Norwegian Blue"
letter = input("Enter character: ")

if letter not in parrot:
    print("I don't need that letter")
else:
    print("Give me an {}, Bob".format(letter))
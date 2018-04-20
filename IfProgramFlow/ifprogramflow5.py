x = input("Please enter some text ")
if x:
    print("You entered '{}'".format(x))
else:
    print("You did not enter anything")

age = int(input("How old are you? "))
if not(age<18):
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years".format(18 - age))
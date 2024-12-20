pwd=input("What is the master password")
def view():
    pass
def add():
    pass
while True:
    mode=input("Do you want to add a new password or view a exis password(Enter view to view or Enter add to add or Enter q to quit)").lower()
    if mode == "q":
        break
    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid Input")
        continue
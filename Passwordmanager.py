master_pwd=input("What is the master password")


def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw= data.split("|")
            print("Username: "+ user, "Password: "+ passw )
            
                   # print(f.read())
def add():
    name=input("Account name:")
    pwd=input("Password: ")

    with open("passwords.txt","a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode=input("Do you want to add a new password or view a exis password(Enter view to view or Enter add to add or Enter q to quit)").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Input")
        continue
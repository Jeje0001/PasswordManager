from cryptography.fernet import Fernet
master_pwd=input("What is the master password")

def viewkey():
    file=open("key.key","rb")
    key=file.read()
    file.close()
    return key
key=viewkey() + master_pwd.encode()
fer=Fernet(key)

# def createkey():
#     key=Fernet.generate_key()

#     with open("key.key","wb") as key_file:
#         key_file.write(key)


def view():
    with open("passwords.txt","r") as f:
        for line in f.readlines():
            data=line.rstrip()
            user,passw= data.split("|")
            print("Username: "+ user, "Password: "+ str(fer.decrypt(passw)))
            
                   # print(f.read())
def add():
    name=input("Account name:")
    pwd=input("Password: ")

    with open("passwords.txt","a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

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

#Continue at 1:34:20
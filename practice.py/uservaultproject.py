import os 
import json 
import hashlib
def hashpassword(rabbithole007):
    return hashlib.sha256(rabbithole007.encode()).hexdigest()
if os.path.exists("people.json"):
    print("vault found")
    with open("people.json","r") as f:
        people =json.load(f)
else:
    people =[]
master=hashpassword("rabbithole007")
def masterlogin():
    while True:
        attempt = hashpassword(input("master password: "))
        if attempt == master:
            print("login- succesful")
            return True
        else:
            print("wrong password try again")
masterlogin()
while True:
    print("1. view entire vault")
    print("2. search person from people")
    print("3. add person to vault")
    print("4. exit")
    choice = input("from the menu enter a number to proceed:  ")
    if choice == "1":
        for person in people :
            print(person)
    elif choice == "2":
        name = input("enter the name of the person :   ")
        password = input("enter password: ")
        found = False
        for person in people:
            if person["name"] == name and person["password"] == hashpassword(password):
                print(person)
                found = True
                break
        if not found:
            print("credentials are invalid")
    elif choice == "3":
        person = {"name":input("name:  "),
                 "age":int(input("age:   ")),
                 "sex": input("sex:  "),
                 "country":input("country: "),
                 "password": hashpassword(input("password:  "))}
        people.append(person)
        with open ("people.json","w") as f:
            json.dump(people,f,indent=2)
    else:
        exit()                   
                            
    
 
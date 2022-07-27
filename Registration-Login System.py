import re

mail_pattern = "^[^0-9][a-zA-Z0-9_]+@[a-z]+\.[a-z]{1,3}$"
pwd_pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&_])[A-Za-z\d@$!#%*?&_]{5,16}$"

def registration(email):
    
    file = open("user_basedata.txt","a")
    
    if re.match(mail_pattern, email):
        
        password = input("Please enter your password: ")

        if re.match(pwd_pattern, password):
            
            file.write(email + "," + password + "\n")
            
            file.close()
            
            print("EmailID sucessfully registered")

        else:
            print("Wrong/Invalid Password")
            
    else:
        print("Wrong/Invalid EmailID")


def login(email, password):
    
    file = open("user_basedata.txt", "r")
    
    for i in file:
        
        x,y = i.split(",")
        y = y.strip()
            
        if(x == email and y == password):
            
            print("Successfully LoggedIn!!")
         
        elif(x == email and y!= password):
            
            print("Invalid password")
            
            print("Forget Password?")
            
            change = input("Please type \'Yes\' to proceed: ").capitalize()

            if change == "Yes":
                
                print("Do you want to retrieve your old password or create new one")
                
                retrieve = input("Type \'R\' to Retrirve or \'N\' to create New Password: ").capitalize()
                
                if retrieve == "R":
                    
                    mailid = input("Enter your EmailID to proceed: ")
                    
                    if mailid == x:
                        
                        print(f"{y} is your password")
                        
                    else:
                        
                        print("Wrong/Invalid mailID")

                elif retrieve == "N":
                    
                    mailid1 = input("Enter your EmailID to proceed: ")
                    
                    if mailid1 == x:
                        
                        newpwd = input("Create your password: ")
                        
                        if re.match(pwd_pattern, newpwd):
                            
                            with open('user_basedata.txt', 'r') as file:
                                
                                filedata = file.read()
                                
                            filedata = filedata.replace(y, newpwd)
                            
                            with open('user_basedata.txt', 'w') as file:
                                
                                file.write(filedata)
                                
                            file.close()
                            
                            print(f"{newpwd} is the new password")
                            
                        else:
                            
                            print("Wrong/Invalid Password")
                            
                        
                    else:
                        
                        print("Wrong/Invalid EmailID")
                        
                else:
                    
                    print("Invalid input")
                    
            else:
                print("Invalid input")
        
    file.close()


print("Hi! There!!")

sign_up = input("Please select \'Register\' or \'Login\' to Proceed: ").capitalize()

if sign_up == "Register":
    
    print("Please enter your EmailID and password to register")
    
    email = input("Enter your Email: ")
    
    registration(email)

elif sign_up == "Login":
    
    email = input("Please enter your MailID: ")
    
    new_file = open("user_basedata.txt","r")
    
    readfile = new_file.read()
    
    if email in readfile:
        
        password = input("Please enter your password: ")
        
        login(email,password)
        
    else:
        print("Sorry, emailID doesn't exist. Kindly Register..")

else:
    
    print("Invalid keys")

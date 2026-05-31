# Password strength checker

import re

# password strength check condition:
# min 8 chars, digit,uppercase,lowercase,special character

def check_password_strength(password):
    if len(password) < 8:
        return "weak:password must be at least 8 characters" \
    
    if not any(char.isdigit() for char in password):
        return "weak:password must contain a digit"
    
    if not any(char.isupper() for char in password):
        return "weak:password must contain an upper character"
    
    if not any(char.islower() for char in password):
        return"weak:password must contain an lower character"
    if not re.search(r'[!@#$%^&*(){}<>./?]'):
        return "Medium: password must containa special charatcter"
    
    return "strong: your password is secured"

def password_checker():
    print("weclome to the password strength checker")

    while True:
        password =input("enter your password(or type 'exit'to quit):")

        if password.lower()== 'exit':
            print("thank you fro using this tool")
            break

        result= check_password_strength(password)
        print(result)


#run the password checker tool
if __name__=="__main__":
    password_checker()        
        
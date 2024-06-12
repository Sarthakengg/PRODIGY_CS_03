import string
#import getpass

def check_password():
    print()
    password=input("Enter Password: ")    #you can also use password=getpass.getpass("Enter Password: ") to hide your password in terminal
    print()                               #and for that you need to import getpass 
    strength=0                           
    remarks=""
    lower_count=upper_count=num_count=special_char_count=password_length=0
    length_of_password=0

    for char in list(password): #we check character by character
        if char in string.ascii_lowercase:
            lower_count+=1
        elif char in string.ascii_uppercase:
            upper_count+=1
        elif char in string.digits:
            num_count+=1
        else:
            special_char_count+=1

    if len(password)>=8:
        password_length=1
        length_of_password=len(password)
    else:
        length_of_password=len(password)
        print("Password length must be of 8 atleast")
        print()
    
    if lower_count>=1:
        strength+=1
    if upper_count>=1:
        strength+=1
    if num_count>=1:
        strength+=1
    if special_char_count>=1:
        strength+=1
    if password_length==1:
        strength+=1

    if strength==1:
        remarks="It is a very bad password. Change ASAP!!!"
    elif strength==2:
        remarks="It is not a good password. Change ASAP!"
    elif strength==3:
        remarks="It is a weak password. Consider changing!"
    elif strength==4:
        remarks="It is a hard password,but can be better"
    else:
        remarks="A very strong password,indeed!!!"

    print("Your password has")
    print(str(lower_count)+" lowercase characters,"+str(upper_count)+" uppercase characters,"+str(num_count)+" numeric characters,"+str(special_char_count)+" special characters,"+" Password length is "+str(length_of_password))

    print()
    print("Password Strength is: "+str(strength))
    print()
    print("Hint: "+str(remarks))

if __name__=="__main__":
    print("Welcome to Password Checker")
    print()
    check_password()

            

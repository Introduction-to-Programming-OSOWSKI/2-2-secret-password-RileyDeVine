#WRITE YOUR CODE IN THIS FILE

#define function
def password(p):

    #correct password
    if p == "Knights19":
        return "ACCESS GRANTED"

    #else for incorrect password
    else:
        return "ACCESS DENIED"

#run password
print(password("password"))
    
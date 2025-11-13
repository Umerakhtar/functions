def log_in():
    print("User logged in")
    return True
def log_out():
    print("wrong input")
    return False

u = input("please set username:  ")
p = input("please set password:  ")
print (". . .  please use your username and password to login(in five attempts)  . . . ")
attempt = 0
while attempt < 5:
    u1 = input("username:  ")
    p1 = input("password:  ")
    if u1 == u:
        if p1 == p:
            log_in()
            break
        else:
            print("incorrect password")
            log_out()
    else:
        print("incorrect username")
        log_out()
    attempt += 1
    print("attempt" , attempt, "out of 5 used")

print("\nprogram ended\n")
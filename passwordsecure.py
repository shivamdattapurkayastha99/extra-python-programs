# securing password using encryption
SECURE=(('s','$'),('and','&'),('a','@'))
def securePassword(password):
    for a,b in SECURE:
        password=password.replace(a,b)
    return password


if __name__ == "__main__":
    password=input("Enter the password")
    password=securePassword(password)
    print(f"The secure password is {password}")

     
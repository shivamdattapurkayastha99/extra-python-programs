import os
def isbinod(filename):
    with open(filename,"r") as f:
        str1=f.read()
    if "binod"  in str1.lower():
        return True
    else:
        return False
if __name__ == "__main__":
    
    dir_contents=os.listdir()
    print(dir_contents)
    for item in dir_contents:
        if item.endswith('txt'):

            print(f" Detecting binod in  {item} ")
            flag=isbinod(item)
            if flag==True:
                print(f"binod is found in {item}")
            else:
                print(f"binod not found in {item}")
    

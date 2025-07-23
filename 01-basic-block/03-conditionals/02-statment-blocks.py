
## here we will make a statement block and see which one exectutes 


if "am1t" in ["am1t","john","doe"]:
    print("outer condition is true") #yes 

    if 10 > 20:
        print("inner condtion 1") #no 
    
    print("between inner condition") #yes

    if 10 < 20: 
        print("inner condition 2") #yes
    
    print("end of outer condition") #yes

print("last outer condition") #yes
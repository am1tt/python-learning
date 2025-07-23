

while True:
    try:
        get_input = int(input("enter a number : "))
        print(get_input)
        break
    except ValueError:
        print("there was no input of number, try again")



## am1tt :  added try and except valueError which catches the exception of error 

## am1tt : if there is no input added , it keeps asking for it , and when its entered the break statement executes ## 
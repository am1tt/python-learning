
## Q :  Write a program to sum a list with 4 numbers ## 


foo = []

total = 0

for i in range(4):
    user_input = int(input(f"number {i + 1} : "))

    foo.append(user_input)

    ## without sum

    total += user_input


summed_container = sum(foo)

print(summed_container)
## without using sum 
print(total)


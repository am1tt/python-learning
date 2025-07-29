

## Question : write a program to input eight numbers from the user and display 
## all the unique numbers (once)



all_input = []


for i in range(3):
    num = int(input(f"numbers {i + 3} : "))

    all_input.append(num)

unique_numbers = set(all_input)

print(f"unique : numbers {unique_numbers}")
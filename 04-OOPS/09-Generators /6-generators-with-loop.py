

def even_numbers(): 
    for i in range(2,7,3):
        yield i


for num in even_numbers(): 
    print(num)

# as said yield returns that is why we have to print it with num 

def infinite_streams(): 
    n = 1 
    while True: 
        yield n
        n+=1
    
gen = infinite_streams()

for _ in range(3): 
    print(next(gen))
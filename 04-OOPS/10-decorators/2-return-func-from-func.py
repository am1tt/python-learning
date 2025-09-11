

def create_multiplier(x): 
    def multiplier(y):
        return x * y
    return multiplier


times_two = create_multiplier(2)
times_three = create_multiplier(3)

print(times_two(2))
print(times_three(4))

## returns a func from another func 
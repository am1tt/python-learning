

class Counter:

    def __init__(self,max): 
        self.num =1
        self.max = max 
    

    def __next__(self): 
        if self.num <= self.max: 
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration
    
    def __iter__(self): 
        return self
    
c = Counter(3)

for num in c: 
    print(num)
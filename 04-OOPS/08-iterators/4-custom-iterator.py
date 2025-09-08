
class Counter:
    def __init__(self,limit): 
        self.limit = limit
        self.current = 1


    def __next__(self): 
        if self.current <= self.limit:
            value = self.current 
            self.current +=1 
            return value
        else:
            raise StopIteration
    
        
    def __iter__(self): ## this only returns the iters btw 
        return self
    

counter = Counter(3)

print(next(counter))
print(next(counter))
print(next(counter))
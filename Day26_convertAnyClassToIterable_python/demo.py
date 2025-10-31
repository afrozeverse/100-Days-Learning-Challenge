class CustomRange:
    def __init__(self,start=1,end=10):
        self.start=start
        self.end=end
    def __iter__(self):
        return self.CustomRange_Iterator(self) #this CustomRange_Iterator object is iterator object beacuse it has 'next' method. It is a rule that an object must have the 'next' method to become an iterator object
    
    #this is not child class, this is inner class. 
    #This inner class will return iterator object
    class CustomRange_Iterator:
        def __init__(self,counter): #as if this is an inner class so we cannot access the variable 'start' and 'end' from here. So we passed the 'CustomRange' class from the 'return self.CustomRange_Iterator(self) ' as an argument. That object is catched here with 'counter'. Now we can access. Because without that we cannot define when to start and when to stop.
            self.counter=counter
            self.beg=counter.start
        def __next__(self):
            if self.counter.start>self.counter.end:
                self.counter.start=self.beg
                raise StopIteration
            current_value=self.counter.start
            self.counter.start+=1
            return current_value

        
my_range=CustomRange(1,5)
#here the 'i' is calling the 'iter' method of the given object(here 'my_range')
print('1st time->')
for i in my_range:
    print(i)

print('2nd time->')
for i in my_range:
    print(i)

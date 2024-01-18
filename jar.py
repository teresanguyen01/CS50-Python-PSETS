class Jar: 
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity is negative. Input a non-negative number next time.")
        else: 
            self.capacity = capacity
            self.cookies = 0
    
    def __str__(self):
        return("🍪" * self.cookies)
    
    def deposit(self, n): 
        self.cookies = self.cookies + n
        if self.cookies > self.capacity: 
            raise ValueError("Reached max capacity")

    def withdraw(self, n): 
        self.cookies = self.cookies - n
        if self.cookies < 1: 
            raise ValueError("More cookies withdrawn than cookies in jar")
        
    """@property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self._size"""
    
def main(): 
    jars = Jar(11)
    jars.deposit(5)
    jars.withdraw(3)
    print(jars)

if __name__ == "__main__":
    main()
class shape(self):
    def area(self):
        pass
    
class circle(shape):
    def __init__(self, redius):
        self.radius = redius

        def area(self):
            return self.radius
        
class rectangle(shape):
    def __init__(self, length, widht):
        self.length = length
        self.widht - widht
    
    def area(self):
        return self.length * self.widht
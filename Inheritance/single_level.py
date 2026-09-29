class shape:
    def __init__(self, color, d):
        self.color=color
        self.d=d
    def getcolor(self):
        return self.color
    def getd(self):
        return self.d

class rectangle(shape):
    def __init__(self,length,width,color,d):
        super().__init__(color,d)
        self.length=length
        self.width=width

    def getlength(self):
        return self.length
    def getwidth(self):
        return self.width

s=rectangle(10,5,'red','3d')
print(s.getlength())
print(s.getwidth())
print(s.getcolor())
# print(s.getcolor())

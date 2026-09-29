class add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.c=0
    def addition(self):
        self.c = self.a + self.b
    def getca(self):
        return self.c

class sub:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.c=0
    def subtrat(self):
        self.c=self.a- self.b
    def getcs(self):
        return self.c

class result(add,sub):
    def __init__(self,a,b):
        add.__init__(self, a, b)
        sub.__init__(self, a, b)


r=result(10,20)
r.addition()
print(r.getca())
class vehicles:
    def __init__(self,brande):
        self.brande=brande

    def getbrande(self):
        return self.brande

class car(vehicles):
    def __init__ (self,engine,type ,brande):
        super(). __init__(brande)
        self.engine=engine
        self.type= type

    def getengine(self):
        return self.engine
    def gettype(self):
        return self.type
class Electric(car):
    def __init__(self, color, batterycap,engine,type, brande):
        super(). __init__(engine,type, brande)
        self.color=color
        self.batterycap=batterycap
    def getcolor(self):
        return self.color
    def getbatterycap(self):
        return self.batterycap

p=Electric('red','500000','hybrid','sedan','tata')
print(p.getcolor())
print(p.getbatterycap())
print(p.getengine())
print(p.gettype())
print(p.getbrande())
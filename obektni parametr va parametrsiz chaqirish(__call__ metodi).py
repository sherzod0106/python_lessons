# parametrsiz chaqirish

class Avtosalon:
    def __init__(self,name):
        self.name=name
        self.model='lacetti'
        self.yil=2020
        
    def __repr__(self):
        return f'Kompaniya {self.name}, model {self.model} ,yili-{self.yil}'
    
    def __call__(self):
        return self.salon1

salon1=Avtosalon('gm')
# print(salon1)

# parametr bilan chaqirish 

def __call__(self,*parametr):
    if parametr:
        print(parametr)
    else:
       return self.parametr
    
salon1=Avtosalon('gm')
#print(salon1)
        



class Avtosalon:
    def __init__(self,name):
        self.name=name
        self.avtolar=[]
        
    def add_avto(self,avto):
        if isinstance(avto,Avtosalon):
            self.avtolar.append(avto)
        else:
            print("Avto obyektni kiriting")

avto1=Avtosalon('gm','malibu','qora',2020,40000)
avto2=Avtosalon('gm','lacetti','oq',2020,20000)
avto3=Avtosalon('tayota','carolla','silver',2018,45000)

for avto in [avto1,avto2,avto3]:
    salon1.add_avto(avto)
    
class Avtosalon:
    def __init__(self,name):
        self.name=name
        self.avtolar=[]
        
    def __getitem__(self,index):
        return self.avtolar[index]
    
    
class Avtosalon:
    def __init__(self,name):
        self.name=name
        self.avtolar=[]
        
    def __repr__(self):
        return f'{self.name} avtosaloni'
    
    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self):
        return self.avtolar[index]
    
    def __setitem__(self,index,value):
        if isinstance(value,Avto):
            self.avtolar[index]=value
            
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(value,Avtosalon):
                self.avtolar.append(avto)
        else:
            print('Avto obyektini kiriting')





    

    
class Avtosalon:
    def __init__(self,name):
        self.name=name
        self.avtolar=[]
        
    def __repr__(self):
        return f'{self.name} avtosalon'
    
salon1=Avtosalon('maxavto')

class Avtosalon:
    def __init__(self,name):
        self.name=name
        self.avtolar=[]
        
    def __repr__(self):
        return f'{self.name} avtosaloni'
    
    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self):
        return self.avtolar[0]
    
    def __setitem__(self,index,value):
        if isinstance('gm',Avtosalon):
            self.avtolar[index]=value
            
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance('gm',Avtosalon):
                self.avtolar.append(avto)
        else:
            print('Avto obyektini kiriting')

    def __call__(self):
        return [avto for avto in self.avtolar]





salon1=Avtosalon('maxavto')
salon2=Avtosalon('avto lider')
avto1=Avtosalon('gm','malibu')#'qora',2020,40000)
avto2=Avtosalon('gm','lacetti')#'oq',2020,20000)
avto3=Avtosalon('tayota','carolla')#'silver',2018,45000)
avto4=Avtosalon('mazda',6) #'qizl',2015,35000)
#avto5=Avtosalon('volkswagen','polo',#'qora',2015,3000)
#avto6=Avtosalon('honda','accord') #'oq',2017,42000)
salon1.add_avto(avto1,avto2)
salon2.add_avto(avto4)

def __add__(self,qiymat):
        if isinstance(qiymat,Avtosalon):
            x=Avtosalon(f'{self.name} {qiymat.name}')
            x.avtolar=self.avtolar+qiymat.avtolar
            return x
salon3=salon1+salon2
print(salon3)

def __call__(self):
       return [avto for avto in self.avtolar]


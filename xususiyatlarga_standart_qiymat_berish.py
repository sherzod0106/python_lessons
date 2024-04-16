
# xususiyatlarga standart qiymat berish
class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.bosqich=1 # standart qiymat bu xususiyat obekt yaratilishida xususiyat sifatida uzatilmaydi
        
    def get_info(self): 
        return f'{self.ism} {self.familiya} {self.bosqich}-bosqich talabasi'
    
talaba1=Talaba('sherzod','sulaymonov',1996)
print(talaba1.get_info())    
        
        
class Talaba:
    def __init__(self,ism,familiya,yosh):
        self.ism=ism
        self.familiya=familiya
        self.yosh=yosh
        self.bosqich=4
        
    def get_info(self):
        return f'{self.ism} {self.familiya} {self.bosqich}-bosqich talabasi'

obekt1=Talaba('sherzod','sulaymonov',27)
print(obekt1.get_info())

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya =familiya
        self.tyil =tyil
        self.bosqich =1

    # def get_info(self):
      # return f'ism-{self.ism}, familiya-{self.familiya}, tyil-{self.tyil} {self.bosqich}-bosqich'
  
    def set_bosqich(self,bosqich):
       self.bosqich=bosqich
       return f'{self.bosqich}-kurs talabasiman'

talaba1 = Talaba('sherzod','sulaymonov', 1996)
#talaba1.set_bosqich(5)
print(talaba1.set_bosqich(4))

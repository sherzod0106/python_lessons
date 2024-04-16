# vorislik va polimorfizm
class Shaxs(): #  'super-class' yoki 'ota-class' yaratamiz
    def __init__(self,ism,familiya,passport): # 3 ta xususiyat oladi
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        
        
    def get_info(self):
        info=f'{self.ism} {self.familiya}'
        info += f' passport:{self.passport}, {self.tyil}-yilda tug`ilgan'
        return info
    
    def get_age(self,yil):
        return yil-self.tyil
    
class Talaba(Shaxs):
    def __init__(self,ism,familiya,passport,tyil): # 5 ta xususiyat (yangi voris classimiz xususiyatlari)
        super().__init__(ism,familiya,passport) # 3 ta xususiyat(super class xususiyatlarini to`liq kiritamiz)
        self.tyil=tyil
        self.id=1122
        
talaba3=Talaba('sherzod','sulaymonov','fs1122',1996)
print(talaba3.get_info())

print(talaba3.get_age(2024))
        
        


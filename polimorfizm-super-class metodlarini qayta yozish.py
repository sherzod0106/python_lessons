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
    
  
    
class Talaba(Shaxs):
    def __init__(self,ism,familiya,passport,tyil): # 5 ta xususiyat (yangi voris classimiz xususiyatlari)
        super().__init__(ism,familiya,passport) # 3 ta xususiyat(super class xususiyatlarini to`liq kiritamiz)
        self.tyil=tyil
        self.id=1122
        
    def get_info(self): # super classdan yaratilgan metodni voris classdan qayta yozamiz (get_info nomi o`zgarmaydi)
        x=f'{self.ism} {self.familiya} {self.tyil} {self.id}'
        x += f' passport:{self.passport}, {self.tyil}-yilda tug`ilgan' 
        return x


talaba3=Talaba('sherzod','sulaymonov','fs1122',1996)
print(talaba3.get_info())




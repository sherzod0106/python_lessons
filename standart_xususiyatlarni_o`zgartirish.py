# 
class Talaba:
    def __init__(self,ism,familiya,yosh):
        self.ism=ism
        self.familiya=familiya
        self.yosh=yosh
        self.kurs=4
    
    def jyil(self):
        return f'mening ismim {self.ism} va men {self.kurs}-kursdaman'
    
obekt1=Talaba('sherzod','sulaymonov',27)
print(obekt1.jyil())

obekt1.kurs=1
print(obekt1.kurs)


class Student:
    def __init__(self,ism,familiya,yosh):
        self.ism=ism
        self.familiya=familiya
        self.yosh=yosh
        self.kurs=1
        
    def jyil(self):
        return f'men {self.ism} va {self.kurs}-kursman'

obekt1=Student('sherzod','sulaymonov',27)
print(obekt1.jyil())

obekt1.kurs=3
print(obekt1.kurs)


class Student: # class yaratamiz standart xususiyatli
    def __init__(self,ism,familiya,yosh):
        self.ism=ism
        self.familiya=familiya
        self.yosh=yosh
        self.bosqich=1 # standart xususiyat
    
    def get_info(self): # standart xususiyat qatnashgan metod yaratamiz
        return f'{self.ism} {self.familiya} {self.bosqich}-kursdaman'
        
    
    def set_bosqich(self,bosqich): # standart xususiyatni argument qilib uzatamiz
        self.bosqich=bosqich

talaba1=Student('sherzod','sulaymonov',27) # obekt yaratamiz

# standart qiymatni o`zgartirish uchun 'argument qabul qiladigan metod'ni tanlashimizning sababi bu metod 
# obekt yaratayotgan vaqtda 'argument qabul qiladigan metod' ichida istalgan qiymatni qabul qiladi va uni
# istalgancha o`zgartirish mumkin

talaba1.set_bosqich(4) #  obekt ichida standart qiymatni o`zgartiramiz
print(talaba1.get_info())

class Talaba:
    def __init__(self,ism,familiya,yosh):
        self.ism=ism
        self.familiya=familiya
        self.yosh=yosh
        self.kurs=2
        
    def get_info(self):
        return f"men {self.kurs}-kursman"
    
    def set_bisqich(self,kurs):
        self.kurs=kurs
        
    def update_kurs(self):
        self.kurs+=1 
        
obekt2=Talaba('sherzod','sulaymonov',27)
print(obekt2.get_info())
































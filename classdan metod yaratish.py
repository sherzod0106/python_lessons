class Talaba:
    def __init__(self,ism,familiya,yosh):
        self.ism=ism
        self.familiya=familiya
        self.yosh=yosh
        
    def name(self): # metod yaratishda argument sifatida 'self' beramiz,chunki class xususiyatlari 'selfda''
        return self.ism # saqlanadi, shunday qilsak metod(classga tegishli funksiya) classning xususiyatlarini oladi
    
    def last_name(self):
        return self.familiya
    
    def full_name(self):
        return f'{self.ism} {self.familiya}'
    
   

    def YoshHisobla(self,tyil): # argument qabul qiluvchi metod argument sifatida 'self' dan tashqarida bo'lgan 
        return tyil+self.yosh # (classimiz ichida bo'lmagan ) xususiyatlarni ham qabul qiladi, mn: tyil-xususiyati
                              # classimiz ichida mavjud emas. bu xususiyatimizni(tyil)  print(obekt.metod_nomi(tyil))
                              # ko'rinishida uzatamiz ya'ni obekt yaratilgandan so'ng beramiz
    
    def get_age(self,Tyil):
        return 2023-Tyil
    
obekt2=Talaba('Jack','Sparrow',60) 
print(obekt2.get_age(1962))   
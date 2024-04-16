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
 #ko'rinishida uzatamiz ya'ni obekt yaratilgandan so'ng beramiz(metod qavsining ichida beramiz,mn
                                                                              # Mn: print(obekt.metod_nomi(tyil))        
    def get_age(self,Tyil):
        return 2023-Tyil
    
obekt2=Talaba('Jack','Sparrow',60) 
print(obekt2.get_age(1962))   

 
class Talaba:
    def __init__(self,ism,familiya,yosh):
        self.ism=ism
        self.familiya=familiya
        self.yosh=yosh
        self.bosqich=1 # standart xususiyatning qiymatini 1 ga teng qilib shu yerda berib ketganimiz uchun 
        # obekt yaratayotgan vaqtimizda boshqa xususiyatlar qiymatini uzatayotganimizda standart xususiyat qiymatini
      # uzatmaymiz chunki standart xususiyat(self.bosqich) qiymatini o`z o`rnida self.bosqich=1 ko`rinishida 1 ga
      # teng qilib berdik

    def jyil(self):
        return f"mening ismim {self.ism} va men {self.bosqich}-bosqichda o`qiyman"

obekt1=Talaba('sherzod','sulaymonov',27) 
print(obekt1.jyil()) 

obekt1.bosqich=3
print(obekt1.bosqich)
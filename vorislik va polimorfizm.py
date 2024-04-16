# vorislik va polimorfizm
class Shaxs(): #  'super-class' yoki 'ota-class' yaratamiz
    def __init__(self,ism,familiya,passport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil
        
    def get_info(self):
        info=f'{self.ism} {self.familiya}'
        info += f' passport:{self.passport}, {self.tyil}-yilda tug`ilgan'
        return info
    
    def get_age(self,yil):
        return yil-self.tyil
    
inson=Shaxs('hasan','alimov' ,'FB001122',1995)
print(f'{inson.get_info()} , {inson.get_age(2024)}')

# voris class yaratamiz
class Talaba(Shaxs):
    def __init__(self,ism,familiya,passport,tyil):
        super().__init__(ism,familiya,passport,tyil)
        
talaba2=Talaba('sherzod','sulaymonov','Fa112299',2000)
print(talaba2.get_info())
print(talaba2.get_age(2024))
        


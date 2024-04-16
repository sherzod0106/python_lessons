class shaxs():
    def __init__(self,ism,familiya,passport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil
        
    def get_info(self):
        return f'ismim-{self.ism}, familiyam-{self.familiya}, {self.tyil}-yilda tug`ilganman'
    
    def get_age(self,yil):
        return yil-self.tyil


class Talaba(shaxs):
    def __init__(self, ism, familiya, passport, tyil):
        super().__init__(ism,familiya,passport,tyil)
        
talaba2=Talaba('sherzod','sulaymonov','FS0077',1996)
print(talaba2.get_age(2024))
print(talaba2.get_info())
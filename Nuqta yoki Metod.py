class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya =familiya
        self.tyil =tyil
        self.bosqich =1

    def get_info(self):
      return f'ism-{self.ism}, familiya-{self.familiya}, tyil-{self.tyil} {self.bosqich}-bosqich'
  
    def set_bosqich(self,bosqich):
       self.bosqich=bosqich
       return f'{self.bosqich}-kurs talabasiman'

talaba1 = Talaba('sherzod','sulaymonov', 1996)
#talaba1.set_bosqich(5)
#print(talaba1.set_bosqich(5))

# dir() funksiyasi orqali istalgan 'obekt' yoki 'klassning' metodlarini ko`ra olishimiz mumkin:

# print(dir(Talaba)) # Talaba klassining metodlarini ko`ramiz
  
# print(dir(talaba1)) # talaba1 obektining metodlarini ko`ramiz 

#  __dict__ metodi orqali "obyektning" xususiyatlarini lug`at ko`rinishida ko`rish mumkin

print(talaba1.__dict__)

# natijadan faqat natijalarni ajratib olish uchun ( .keys() ) funksiyasidan foydalansak
print(talaba1.__dict__.keys())
print(talaba1.__dict__.values())
print(talaba1.__dict__.items())







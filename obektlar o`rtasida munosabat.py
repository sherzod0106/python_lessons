# obyektlar o`rtasida munosabat
class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya =familiya
        self.tyil =tyil
        self.bosqich =1

    def get_info(self):
      return f'ism-{self.ism}, familiya-{self.familiya}, tyil-{self.tyil}'


class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar =[]

    def add_student(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

   
    

matematika = Fan('oliy matematika')
talaba1 = Talaba('sherzod','sulaymonov', 1996)

matematika.add_student(talaba1)

print(matematika.talabalar_soni)
print(matematika.talabalar)
print(talaba1.get_info)

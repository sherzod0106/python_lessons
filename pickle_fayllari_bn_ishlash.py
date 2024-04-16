# o`zgaruvchilarni faylda saqlash (pickle)
# pickle fayliga yozish
import pickle 

talaba1={'ism':'sherzod','familiya':'sulaymonov','tyil':1996,'kurs':4}
talaba2={'ism':'nodirbek','familiya':'sulaymonov','tyil':1993,'kurs':3}


# pickle fayliga yozish (pickle.dump metodi)
with open('pickle_fayl.dat','wb') as fayl: # 'wb(write binary)-ikkilik sanoq tizimida yozish uchun
    pickle.dump(talaba1,fayl)
    pickle.dump(talaba2,fayl)
    
# pickle faylini o`qish (pickle.load metodi)
with open('pickle_fayl.dat','rb') as fayl:
    talaba1=pickle.load(fayl)
    talaba2=pickle.load(fayl)
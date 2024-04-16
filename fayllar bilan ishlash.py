# faylni o`qish uchun ochish
with open('talabalar.txt') as fayl:
    x=fayl.read()
    print(x)


# faylni qatorma qator o`qish uchun for siklidan foydalanamiz 
fayl='talabalar.txt'
with open(fayl) as f:
    for x in f:
        print(x)
        
# qatorlarni ro`yxat ko`rinishida saqlab olish uchun .readlines() metodidan foydalanamiz
with open(fayl) as x:
    y=x.readlines()
    print(y)
    
# faylga ma`lumot yozish
# yangi faylga yozish 

faylnomi='ustozlar.txt' # ochilayotgan fayl nomi
with open(faylnomi,'w') as fayl:
    fayl.write('hello world') # faylga yozilayotgan matn

faylnomi='new_file.txt'
ism='sherzod sulaymonov'
tyil=1996
with open(faylnomi,'w') as fayl:
     fayl.write(ism+'\n')
     fayl.write(str(tyil)+'\n')
     
with open('yangi_malumotlar.txt','w') as x:
    y=x.write('arnold schwarzenegger'+'\n')
    y=x.write(str(1947)+'\n')


with open('yangi_malumotlar.txt','a') as x:
    x.write('johnny depp\n')
    x.write('1963\n')  
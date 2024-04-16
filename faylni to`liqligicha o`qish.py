with  open('pi.txt') as fayl:
     x=fayl.read()
     print(x)
    
     x=x.rstrip()  #  matnga ishlov berish
     x=x.replace('\n','')
     x=float(x)
     print(x)
    



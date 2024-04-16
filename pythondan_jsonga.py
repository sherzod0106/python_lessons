# pythondan json ga 

import json 
x=10
x_json=json.dumps(x) # json.dumps()  o`zgaruvchini json matniga o`zgartiradi
ism='sherzod'
ism_json=json.dumps(ism)
sonlar=[10,20,30]
sonlar_json=json.dumps(sonlar)

bemor={
       'ism':'alijon valiyev',
       'yosh':30,
       'oila':True,
       'farzandlar':('ahmad','bonu'),
       'allergiya':None
      }

bemor_json=json.dumps(bemor,indent=10)


bemor={
       'ism':'alijon valiyev',
       'yosh':30,
       'oila':True,
       'farzandlar':('ahmad','bonu'),
       'allergiya':None
      } 
with open('bemor.json','w') as f: # json.dump(x,file) o`zgaruvchini json matniga o`zgartirib, ko`rsatilgan faylga yozish
    json.dump(bemor,f)
    



# json.loads() bu funksiya argument sifatida json matn qabul qiladi va python matniga aylantiradi

sonlar=json.loads(sonlar_json)
bemor=json.loads(bemor_json)
print(bemor) 
print(sonlar)    

# json.load() json fayllarini pythonga yuklab olish uchun ishlatiladi

faylnomi='bemor.json'
with open(faylnomi) as f:
    bemor=json.load(f)
    
print(type(bemor))
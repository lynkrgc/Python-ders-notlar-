#*************  Tuple List; köşeli parantez olmadan tanımlanan liste türü, tuple listelerin indeksleri sonradan değiştirilemez
tuple='damla','ayse'
print(tuple)
#Liste için geçerli olan her şey aynıdır indeks değiştirme hariç.
sehirler=['kocaeli','istanbul']
plakalar=[41,34]

print(plakalar[sehirler.index('istanbul')])     #sırasıyla yazıldığında işe yarar

#print(plakalar['kocaeli]) => 41 bilgisini vermesini istiyoruz.Bu yüzden dictionary kullanılır.

#Key-value

liste={'key': 'value'}
plakalar={'kocaeli':41,'istanbul':34}
print(plakalar['kocaeli'])
plakalar['ankara']=6
print(plakalar)

users={'sadikturan':{
       'age': 36,
       'city': 'ankara',
       'phone':'056982354748',
       'roles':['student','admin']
},'cinarturan':{
       'age': 18,
       'city':'izmir',
       'phone': '05486958241',
       'roles':['student']

}}
print(users['cinarturan'])

ogrenciler={
       '120':{
              'ad': 'Ali',
              'soyad':'Yılmaz',
              'telefon':'532 000 00 01'
       },
       '125':{
              
              'ad': 'Can',
              'soyad':'Korkmaz',
              'telefon':'532 000 00 02'
       },
       '128':{
              
              'ad': 'Volkan',
              'soyad':'Yükselen',
              'telefon':'532 000 00 03'
       }
}
'''
'''
#Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayın.
ogrenciler={}
number=input("öğrenci no:")
name=input("öğrenci adı:")
surname=input("öğrenci soyad:")
phone=input("örenci telefon:")

ogrenciler[number]={
       'ad':name,
       'soyad':surname,
       'telefon':phone
}


#update ile birden fazla key bilgisi eklenebilir.

ogrenciler.update({
       number:{
              'ad':name,
              'soyad':surname,
              'telefon':phone
       }
})
number=input("öğrenci no:")
name=input("öğrenci adı:")
surname=input("öğrenci soyad:")
phone=input("örenci telefon:")
ogrenciler.update({
       number:{
              'ad':name,
              'soyad':surname,
              'telefon':phone
       }
})
number=input("öğrenci no:")
name=input("öğrenci adı:")
surname=input("öğrenci soyad:")
phone=input("örenci telefon:")
ogrenciler.update({
       number:{
              'ad':name,
              'soyad':surname,
              'telefon':phone
       }
})


print('*'*50)
ogrNo=input('öğrenci no:')
ogrenci=ogrenciler[ogrNo]
print(f"Aradığınız {ogrNo} nolu öğrencinin adı :{ogrenci['ad']} soyadı:{ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']}")

#sets list ; Süslü parantezler içinde yazılan listelerdir ve indekslenemezler.
fruits={'banana','apple','orange'}
#print(fruits[0]) run ettiğimizde terminale 'banana' yazılmadığı görülür.
#liste elemanlarını tek tek yazdırabilmek için,
for x in fruits:
       print(x)

fruits.add('cherry')
fruits.update(['mango','strawberry','apple']) #.update ile liste eklenir karışık bir şekilde VE AYNI İNDEKSİ TEKRAR YAZMAZ!
fruits.remove('mango')
fruits.discard('apple')
fruits.pop() #inddekslenebilen listelerde son elemanı siler ancak indekslenemeyen listeler karışık olacağı için son eleman garantisi verilemez
#herhangi bir elemanı siler.
fruits.clear() #tüm elemanları siler
print(fruits)
myList=[1,2,4,5,5,4,4,2,1]
print(set(myList)) #aynı olan indeksleri listeden çıkartır ve tek bir kez yazar.

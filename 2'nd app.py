#Value types vs. Reference types 
#Value types da değer tipi değiştiği zaman farklı adreslerde indekslendiği için değer değişmez

a=25
b=5
a=b
b=10
print(a,b)
#Reference types => Listeler üzerinde aynı adrese indeklsendiği için değer değişir
x=['ali','ayşe']
y=['bebek','adam','kadın']
x=y
y[0]='ali'
print(x)
print(y)

#ASSİGNMENT : TANIMLAMA
x,y,z=5,10,20
x,y=y,x
x +=5 #x=x+5  dört işlem için kullanılabilir mod alma için de % ile kullanılabilir., // işareti ile floatız tam bölme sonucu görülür, ** işaretleri ile üs alınır

print(x,y,z)
values=1,2,3,4,5    #tuple list
print(values)
print(type(values))
x,*y,z= values       #eksik sayıda eleman olursa hata alırız eğer fazla sayıda eleman olursa da değişkenlerin atlandığı adreslerden birinin başına * işareti konularak yeni bir lista yapılır.
print(x,y,z)
print(x,y[1],z)

x,y,z=2,5,10
numbers=1,5,7,10,6
#1)Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
a=int(input('1.sayi:'))
b=int(input('2.sayi:'))
result=((a*b)-(x+y+z))
print(result)
#2)y'nin x'e kalansız bölümünü hesaplayın
print(y//x) 
#3)(x,y,z) toplamının mod3'ü ?
print((x+y+z)%3)
#4) y nin x.ci kuvveti
print(y**x)
#5) x,y*,z=numbers işlemine göre z'nin küpü kaçtır?
x,*y,z=numbers
print(x,y,z)
print(z**3)
#6) x,*y,z=numbes işlemine göre y'nin değerleri toplamı
print(y[0]+y[1]+y[2])


#***********COMPARİSAN OPERATORS (KARŞILAŞTIRMA OPERATÖRLERİ)
# username, password=> databese ;kullanıcıdan alınan bilgileri databese'deki bilgilerle karşılaştırır
a,b,c,d = 5,5,10,4
result=a==b
result=a!=b
result=a>c
result=a>=b 
print(result)
#eg:
#1) Girilen 2 sayıdan hangisi büyüktür?
a=int(input('İlk sayiyi girin:'))
b=int(input('İkinci sayiyi grinizi:'))
result=a>b
print((result==1),'İlk girilen sayi daha büyüktür')
print((result==1), 'İkinci girilen sayi daha büyüktür')
#print(f' a:{a} b:{b} den büyüktür: {result}')
#2) Kullanıcıdan iki vize(%60) ve final(%40) notunu alıp ortalama hesaplayınız.Eğer ortalama  50 ve üstündeyse geçti değil ise kaldı yazdırın

x=float(input('İlk vize notunuzu giriniz:'))
z=float(input('İkinci vize notunuzu giriniz:'))
y=float(input('Final notunuzu giriniz:'))
ortalama=((((x+z)/2)*60)/100)+((y*40)/100)
print(f' not ortalamanız:{ortalama} ve dersten geçme durumunuz: {ortalama>=50}')
#3)Girilen bir sayının tek mi çift mi olduğunu yazdırın
k=int(input('Bir sayi giriniz:'))
tekcift=(k%2==0)
print(f'Girilen sayinin cift olma durumu:{tekcift}')
#4)Girilen bir sayının pozitif mi negatif mi olduğunu
pozitifnegatif=(k>0)
print(f'Girilen sayinin pozitif olma durumu: {pozitifnegatif}')

#5)Parola ve email bilgisi isteyip doğruluğunu kontrol edin
#8(email: email@sadikturan.com   parola:abc123)
email=str(input('Emailinizi giriniz:'))
parola=str(input('Parolanızı giriniz:'))
e=(email=='email@sadikturan.com')
p=(parola=='abc123')
print(f'Girilen emailin doğru mu:{e} ve girilen şifrenin doğru mu:{p}')

#******************************************************************LOGİCAL OPERATORS (MANTIKSAL OPERATÖRLER)

#AND
from typing import List


x=6
hak=0
devam='e'
result= (x>5) and (x<10)   #True,True=> True
result=(hak>0) and (devam=='e')

#OR
result=(x>0) or (x%2 ==0) #True,False =>True

#NOT
result= not(x>0)

#x, 5-10 arasında olan çift bir sayı mı?
result=(((5<x) and (x<10)) and (x%2 == 0))
#print(result)

#Girilen bir sayının 0-100 arasında olup olmadığını kontrol edin
#a=int(input('Bir sayi girin:'))
#print((0<a) and (a<100))

#Girilen bir sayının pozitif çift sayı olup olmadığını kontrol edin
#print( (a>0) and (a %2== 0))

#Girilen 3 sayıyı büyüklük olarak kaşılaştırın
#b=int(input('İkinci sayiyi girin:'))
#c=int(input('Üçüncü sayiyi girin:'))
#sayilar=[a,b,c]
#sayilar.sort()
#print(sayilar)

#Kullanıcıdan 2 vize(%60) ve final (%40) notunu alıp ortalama hesaplayın

#Eğer ortalama 50 ve üstündeyse geçti değil ise kaldı yazdırın.
#a) Ortalama 50 olsa bile final notu en az 50 olmalıdır
#b) Finalden 70 alındığında ortalamanın önemi olmasın

vize1=int(input('İlk vize notunuzu giriniz:'))
vize2=int(input('İkinci vize notunuzu giriniz:'))
final=int(input('Final notunuzu giriniz:'))
if(final>=70):
  print('Dersten geçtiniz')
else:
    ()
ortalama=(((vize1+vize2)/2)*0.6) +(final*0.4)
a=(ortalama>=50 and final>50)
print(ortalama)
if a==1:
 print(f'Dersin ortalaması: {ortalama} ve dersten geçme durumu: GEÇTİ')
else:
 print(f'Dersin ortalaması: {ortalama} ve dersten geçme durumu: KALDI')

'''
6 Kişinin ad,kilo, ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
Formül: (Kilo/ boy uzunluğunun karesi)
Aşağıdaki tabloya göre kişi hangi gruba girmektedir yazdırın.
0-18.4 => Zayıf
18.5-24.9 =>Normal
25.0-29.9 =>Fazla kilolu
30.0-34.9=> Obez
'''
name=input('adınız:')
kg= float(input('kilonuz'))
hg= float(input('boyunuz:'))
indeks= kg/ (hg**2)
print(f'Vücut kitle indeksiniz: {indeks}')
if(indeks<18.4):
  print('Zayıf')
if(18.5<indeks and indeks<24.9):
  print('Normal')
if(25.0<indeks and indeks<29.9):
  print('Fazla kilolu')
if(30.0<indeks and indeks<34.9):
  print('Obez')







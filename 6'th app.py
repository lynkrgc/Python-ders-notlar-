'''
num= int(input('sayi= '))
print(num)
if num>0:
    print('sayi pozitif')
elif num<0:
    print('sayi negatif')
else:
    print('sayi sifir)



1-Kullanıcıdan isim,yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.
İsim= str(input('İsminiz: '))
Soyad= str(input('Soy isminiz:'))
Yaş= int(input('Yaşınız: '))
Eğitim =str(input('Eğitim Durumunuz :'))

if Yaş<18 :
    print('Yasiniz tutmadiği icin ehliyet alamazsiniz')

elif Yaş>=18 and Eğitim== ('Lise') or Eğitim==('Üniversite') :
    print('Ehliyet alabilirsiniz.')
elif Yaş>=18 and Eğitim!= 'Üniversite' or'Lise' :
    print('Ehliyet alamazsınız.')
else:
    print('Girdiginiz bilgiler gecersiz.')



2- Bir öğrenciden 2 yazılı bir sözlü notu alıp ortalama hesabına göre not aralığına karşılık gelen
not bilgisini yazdırınız.
0-24 =>0
25-44=>1
45-54=>2
55-69=>3
70-84=>4
85-100=>5
sınav1=float(input('İlk sınav notunuzu giriniz:'))
sınav2=float(input('İkinci sınav notunuzu giriniz:'))
sözlü=float(input('Sözlü notunuzu giriniz:'))

Ortalama=(sınav1+sınav2+sözlü)/3
if (Ortalama<25):
    print(f'Ortalamanız: {Ortalama} not bilgisi:0')
elif (25<=Ortalama<45):
     print(f'Ortalamanız: {Ortalama} not bilgisi:1')
elif 45<=Ortalama<55:
     print(f'Ortalamanız:{Ortalama} not bilgisi:2')
elif 54<=Ortalama<70:
     print(f"Ortalamanız: {Ortalama} not bilgisi:3")
elif 69<=Ortalama<85:
     print(f"Ortalamanız: {+Ortalama} not bilgisi:4")
elif 84<=Ortalama<101:
     print(f"Ortalamanız: {Ortalama} not bilgisi:5")
else :
     print("Geçerli bir değer giriniz. 0/100")

3-Trafiğe çıkış tarihi alınan bir aracın servis zamanı aşağıdakine göre hesaplayın.
1. Bakım=> 1.yıl
2. Bakım=> 2.yıl
3. Bakım=> 3.yıl
**Süre hesabını alınan gün,ay,yıl bilgisine göre hesaplayınız.
***datetime modülü kullanın.

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

---
import datetime #datetime modülü aktif edildi.
ÇıkısTarihi=input('Trafige çikis tarihinizi yazin:(yıl/ay/gün) ')
ÇıkısTarihi=ÇıkısTarihi.split('/') #indexleri / ile ayır
tarih= datetime.datetime(int(ÇıkısTarihi[0]),int(ÇıkısTarihi[1]),int(ÇıkısTarihi[2]))
simdi= datetime.datetime.now()
fark= simdi - tarih
print(simdi)
days= fark.days #iki tarih arasındaki günleri saymak için
if days<=365:
    print('1.servis aralığı')
elif 365<days<=365*2:
    print('2.servis aralığı')
elif 365*2<days<=365*3:
    print('3.servis aralığı')

4-Girilen bir sayının 0-100 arrasında olup olmadığını kontrol ediniz.
sayi=int(input('Bir tamsayi giriniz: '))
result=(sayi>0)and(sayi<=100)
print(f'sayi 0- 100 arasında mı? {result}')

5-Girilen bir sayinin pozitif çift tam sayi olup olmadığını kontol ediniz.
sayi=int(input('a:'))
result=(sayi>0) and (sayi%2==0)
print (f'sayi pozitif,çift bir tamsayi mi? {result}')

6-Email ve parola bilgileri ile giriş kontrolü yapınız.
email:'aleynakaraagac.ieee@gmail.com
password:'abc123'
Mail=str(input('Email adresinizi giriniz: '))
Şifre=str(input('Şifrenizi giriniz:'))
if Mail==('aleynakaraagac.ieee@gmail.com') and Şifre==('abc123'):
    print('Doğru giriş yaptınız.')
elif Mail==('aleynakaraagac.ieee@gmail.com') and Şifre!=('abc123'):
    print('Şifreyi yanlış girdiniz.')
else:
    print('Hatalı giriş yaptınız.')
    
7-Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
'''
a=float(input('a:'))
b=float(input('b:'))
c=float(input('c:'))

if(a>b)and(a>c):
    print(f'En büyük sayi :{a} ')
    if(b>c):
        print(f'ikinci sayi:{b} ')
        print(f'Üçüncü sayi:{c}')
        print(f'Sıralama şu şekildedir: {a}<{b}>{c}')
    else:
        print(f'ikinci sayi:{c} ')
        print(f'Üçüncü sayi:{b}')
        print(f'Sıralama şu şekildedir: {a}<{c}>{b}')


if(b>a)and(b>c):
    print(f'En büyük sayi :{b} ')
    if(a>c):
        print(f'ikinci sayi:{a} ')
        print(f'Üçüncü sayi:{c}')
        print(f'Sıralama şu şekildedir: {b}<{a}>{c}')
    else:
        print(f'ikinci sayi:{c} ')
        print(f'Üçüncü sayi:{b}')
        print(f'Sıralama şu şekildedir: {b}<{c}>{a}')

if(c>b)and(c>a):
    print(f'En büyük sayi :{c} ')
    if(b>a):
        print(f'ikinci sayi:{b} ')
        print(f'Üçüncü sayi:{a}')
        print(f'Sıralama şu şekildedir: {c}<{b}>{a}')
    else:
        print(f'ikinci sayi:{a} ')
        print(f'Üçüncü sayi:{b}')
        print(f'Sıralama şu şekildedir: {c}<{a}>{b}')
























'''
result = (c>b) and (c>a)
print(result)
if result==True:
    print(f'{c} en büyük sayıdır')
if(b>a):
  result==True and (b>a)
  print(f'İkinci sayı {b} dir.')
  print(f'Üçüncü sayı {a} dir.')
if(a>b):
 result==True and (a>b)
 print(f'İkinci sayı {a} dir.')
 print(f'Üçüncü sayı {b} dir.')

result = (b>a) and (b>c)
if result==True:
    print(f'{b} en büyük sayıdır')
elif result==True and (a>c):
    print(f'İkinci sayı {a} dir.')
    print(f'Üçüncü sayı {c} dir.')
elif result==True and (c>a):
     print(f'İkinci sayı {c} dir.')
     print(f'Üçüncü sayı {a} dir.')

result = (a>b) and (a>c)
if result==True:
    print(f'{a} en büyük sayıdır')
elif result==True and (b>c):
    print(f'İkinci sayı {b} dir.')
    print(f'Üçüncü sayı {c} dir.')
elif result==True and (c>b):
     print(f'İkinci sayı {c} dir.')
     print(f'Üçüncü sayı {b} dir.')
'''
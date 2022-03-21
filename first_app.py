'''
Daire alanı=πr^2
Daire çevresi=2πr

*Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (r=3.14)

'''
'''
print("Yaricapi giriniz:")
r= input()
Yarıcapi=r
type(r)
r=float(r)
π= float()
π=3.14
DaireninAlani=π*r*r
DaireninCevresi=2*π*r
print('Dairenin alani='+ str(DaireninAlani))
print('Dairenin çevresi='+ str(DaireninCevresi))
'''
'''
result =200/700
print('the result is {r:tam kısımda bulunacak karakter bulunacağı:virgülden sonra kaç karaktergeleceği}.format(r=result))
'''
#eg2:
website="http://www.sadikturan.com"
course="python kursu: baştan sona python programlama rehberiniz (40 saat)"
#1-'course' karakter dizisinde kaç karakter bulunmaktadır?
print(len(course))
#2-'website' içinden www karakterlerini alın.
print(website[7:10])
#3-'website' içinden com karakterlerini alın.
print(len(website))
print(website[22:])
#4-'course'içinden ilk 15 ve son 15 karakteri alın.
print(course[:15]+course[49:65])
#5-'course' ifadesinkedi değişkenleri tersten yazdırınız.
print(course[-1:-66:-1])

name,surname,age,job= 'Bora','Yılmaz', 32, 'mühendis'
#6-Yukarıdaki verilen değişkenler ile ekrana şunu yazdırın; 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'
print('Benim adım'+ ' Bora'+' Yılmaz'+ ',Yaşım '+'32'+' ve mesleğim '+'mühendis'+'.')
#7-'Hello world' ifadesindeki w harfini 'W' ile değiştirin
x='Hello world'
print(x[0:6]+'W'+x[7:11])
#8-'abc' ifadesini yan yana 3 defa yazın
x='abc'
print(x*3)
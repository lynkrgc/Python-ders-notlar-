names=['Ali','Şevval','Hakan','Deniz']
years=[1998,2000,1998,1987]
#"Cenk" ismini listenin sonuna ekleyiniz
names.append("Cenk")
print(names)
#"Sena" değerini listenin başına ekleyiniz
names.insert(0,"Sena")
print(names)
#"Deniz" ismini listeden siliniz
names.pop(4)
print(names)
#"Ali" listenin bir elemanı mıdır?
besincisoru="Ali" in names
print(besincisoru)
#Liste elemanlarını ters çevirin
names.reverse()
print(names)
#Liste elemanlarını alfabetik sıralayın
names.sort()
print(names)
years.sort()
years.reverse()
print(years)
#years dizisinde kaç tane 1998 vardır?
print(years.count(1998))
#years dizisinin tüm elemanlarını siliniz
years=[ ]
print(years)
#Kullanıcıdan alacağınız 3 tane marka blgisini bir listede saklayınız
markalar=[]
marka=input("marka: " )
markalar.append(marka)
marka=input("marka: " )
markalar.append(marka)
marka=input("marka: " )
markalar.append(marka)
print(markalar)















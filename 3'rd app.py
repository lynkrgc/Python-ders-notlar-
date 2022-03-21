List=['Bmw','Mercedes',' Opel','Mazda']
#Liste kaç elemanlıdır?
print(len(List))
#Listenin ilk ve son elemanı
print(List[0])
print(List[-1])
#Mazda değerini Toyota ile değiştirin
List.remove('Mazda')
List2=['Toyota']
List.extend(List2)
print(List)
#List[-1]='Toyota'
#print(List)

#Mercedes listenin bir elemanı mıdır?
result='Mercedes' in List
print(result)
#Listenin -2 indeksindeki değeri nedir?
print(List[-2])
#Listenin ilk 3 elemanını alın
print(List[0:3])
#Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin
print(List)
List3=["Renault"]
List.extend(List3)
print(List)
#Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin
List4=['Audi','Nissan']
List.extend(List4)
print(List)
#print(List+['Audi','Nissan'])

#Listenin son elemanını silin
List.remove('Nissan')
print(List)
#del List[-1]
#print [List]

#Liste elemanlarını tersten yazın
print(List[::-1])

'''Aşağıdaki verileri bir liste içinde saklayın.

        #studentA: Yiğit Bilgi 2010,(70,60,70)
        #StudentB: Sena Turan  1999,(80,80,70)
        #StudentC: Ahmet Turan 1998,(80,70,90)
'''
'''
StudentA=['Yiğit','Bilgi',2010,(70,60,70)]
StudentB=['Sena','Turan',1999,(80,80,70)]
StudentC=['Ahmet','Turan',1998,(80,70,90)]
List2=[StudentA +StudentB +StudentC]
print(List2)
result1=StudentC[3][1]
print(result1)
result2=f"{StudentA[0]} {StudentA[1]} {2021-StudentA[2]} yasinda ve not ortalamasi {((StudentA[3][0])+(StudentA[3][1])+(StudentA[3][2]))/3}"
print(result2)
'''
numbers=[1,10,5,16,89,3,47]
letters=['a','b','g','z','y','s']
print(min(numbers))
print(max(numbers))
print(min(letters))
print(max(letters))
#letters.          için de geçerli
numbers.append(49)     #sona 49 ekler
print(numbers)
numbers.insert(3,78) #3.indekse 78i ekle
print(numbers)
numbers.pop(-1)      #-1. indeksi siler
print(numbers)
numbers.sort()      #listeyi sıralar küçükten büyüğe
print(numbers)
numbers.reverse()    #listeyi ters çevirir
print(numbers)
print(type(letters)) #hangi tanımlama türünde tanımlandığını yazar
#.split fonksiyonu ile string içerisindeki elemanları çağırırız.Liste için aynı fonksiyonu kullanamayız.
message='Hey there, I am using whatsapp'.split()  #.split koymazsaan çıktı olarak 'H' vericek.
print(message[0])



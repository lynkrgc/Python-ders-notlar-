
# IDENTİTY & MEMBERSHİP OPERATORS
#IDENTİTY
# 'is' operatörü ile eşitlik sorulduğunda adreslerin aynı olup olmadığına bakar.
x=y= [1,2,3]
z=[1,2,3]
print(x==y)             #değer karşılaştırması
print(x is z)           #adres karşılaştırması
print(x==z)

#MEMBERSHİP
# 'in' operatörü ile str ve ya dizi içerisinde karakter- index olup olmadığını tamamlar

x=['apple','banana']
print('banana' in x)
name='aleyna'
print('a' in name)

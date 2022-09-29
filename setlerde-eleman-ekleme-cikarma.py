l = ["geleceği", "yazanlar"]

s = set(l)

print(s)

print(dir(s))

s.add("gelecegi_ile")

print(s)

s.add("yazanlar")  

print(s) #küme içerisinde sadece bir tane yazanlar ifadesi bulunacaktır.

s.remove("yazanlar")

print(s) #küme içersinde yazanlar ifadesi silinecektir.

s.remove("yazanlar") # küme içerisinde yazanlar ifadesi olmadığı için küme içersinde olmadığına dair hata çıkartacaktır.

s.discard("yazanlar") # küme içerisinde yazanlar ifadesi olmamasına rağmen hata çıkarmayacaktır.
# from ast import Set
# from logging import setLogRecordFactory
# from signal import raise_signal
# Set
# 1) Sırasızdır
# 2) Değerleri Eşsizdir
# 3) Değiştirilebilirdir
# 4) Farklı tipleri barındırabilir

s = set()
print(s)

l = [1,"a",3,"bc"]
t = set(l)
print(t)

x = ("ali","bir",1)
s = set(x)
print(s)

ali = "lutfen_ata_bakma_uzaya_git"
print(type(ali))

y = set(ali)
print(y)

x = ["ali","lutfen","ata","bakma","uzaya","git","git","ali","git"]

s = set(x)
print(s)

print(s[0]) # set indexleme işlemini desteklemez
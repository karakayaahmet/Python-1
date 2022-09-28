# dictionary:
# 1) Kapsayıcıdır.
# 2) Sırasızdır.
# 3) Değiştirilebilirdir.
# 4) Listelerde olduğu gibi index işlemleri yapılamaz

sozluk = {"REG" : "Regresyon",
        "LOJ" : "Lojistik",
        "CART" : "Classification and Reg"}

print(len(sozluk))

sozluk = {
    "REG" : 10,
    "LOJ" : 20,
    "CART" : 30
}

print(sozluk)

sozluk = {
        "REG" : ["bir",10],
        "LOJ" : ["iki",20],
        "CART" : ["uc",30]
}

print(sozluk)
liste = ["ali","veli","isik","ali","veli"]

print(liste.count("ali"))

print(liste.count("veli"))

print(liste.count("isik"))

liste_yedek = liste.copy

print("yedek liste: " , (liste_yedek))

liste.extend(["a","b","c"])

print(liste)

liste.index("ali")

print(liste)

liste.reverse()

print(liste)

liste.sort()

print(liste)

liste.clear()

print(liste)
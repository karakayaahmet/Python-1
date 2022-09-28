liste = ["ali","veli","berkcan","ayse"]

liste[2] = "berkcanın babasi"

print(liste)

liste[2] = "berkcan"

liste[0:3] = "alinin_babasi", "velinin_babasi", "berkcanin_babasi"

print(liste)

liste = liste + ["kemal"]

print(liste)

del liste[2]

print(liste)
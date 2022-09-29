set1 = set([1,2,3])
set2 = set([1,2,3,4,5,6])

print("iki küme arasında kesişim var mı? (kesişim boş mu?) ",set1.isdisjoint(set2))

print("bir kümenin bütün elemanları diğer bir kümede bulunuyor mu? :",set1.issubset(set2))

print("bir küme diğer bir kümeyi kapsıyor mu? ",set1.issuperset(set2))
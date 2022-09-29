set1 = set([1,2,3])
set2 = set([1,5,2])

print("iki kümenin kesişimi: ",set1.intersection(set2))
print("iki kümenin kesişimi: ",set2.intersection(set1))

print(set1 & set2)
print(set2 & set1)

print("iki kümenin birleşimi: ",set1.union(set2))
print("iki kümenin birleşimiÇ ",set2.union(set1))

print("kesişimler artık set1 in elemanları oldu. ",set1.intersection_update(set2))

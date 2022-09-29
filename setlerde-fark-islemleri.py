set1 = set([1,2,3])
set2 = set([1,5,2])

print("set1 de olup set2 de olmayanlar: ",set1.difference(set2))

print("set2 de olup set1 de olmayanlar: ",set2.difference(set1))

print("iki kümede de olmayanlar: ",set1.symmetric_difference(set2))

print(set1 - set2)
print(set2 - set1)


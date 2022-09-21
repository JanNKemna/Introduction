# Other list functions
ls1 = list(range(35,65,4))
print(ls1, len(ls1))

ind1 = ls1.index(47)
count1= ls1.count(47)

lsmax = max(ls1)
lsmin = min(ls1)

ls2 = [ind1, count1, lsmax, lsmin]
print(ls2)
ls2.sort()
ls2.reverse()

ls3 = ls2.copy()
ls2.clear()

print(ls1, "\n", ls2, "\n", ls3)

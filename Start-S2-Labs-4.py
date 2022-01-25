#author: LM (AMDG) 1/25/22
def double_every_other(l):
    # multiplies value by two if the index divided by two has no remainder
    return [x * 2 if i % 2 else x for i, x in enumerate(l)]

print(double_every_other([1,2,3,4,5,6,7,8,9]))
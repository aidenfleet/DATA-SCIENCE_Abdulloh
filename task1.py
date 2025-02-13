def kwargsAcceptFun(**kwargs):
    dic = (kwargs)
    ls = []
    for i, j in dic.items():
        ls.append(j)
    return sum(ls)
print(kwargsAcceptFun(N=7, N1=8, N2=9, N3=10))

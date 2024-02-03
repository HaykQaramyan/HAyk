def f():
    l = []
    for i in range(2, 101):
        p = True
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                p = False
                break
        if p:
            l.append(i)
    return l

r = f()
print(r)
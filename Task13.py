def swap(a):
    a = a.split()
    a[0], a[1] = a[1], a[0]
    a = " ".join(a)
    print (a)
swap("Makers Bootcamp")
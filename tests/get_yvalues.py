def get_yvals(start, end):
    li1 = [.25 * i for i in range(0, 20)]
    li2 = [.5 * i for i in range(10, 40)]
    li3 = list(range(20,100))
    li4 = list(range(100, 1000, 2))
    li5 = list(range(1000, 10000, 10))
    li = li1 + li2 + li3 + li4 + li5
    y_vals = [i for i in li if i < high and i > low ]
    return y_vals

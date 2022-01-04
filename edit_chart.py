from grid import Grid

# load test data

g = Grid(20,31)

g.add_xcol(20)
for i in range(21, 30):
    g.add_x(i)
g.add_ocol(28)
for j in range(27, 24, -1):
    g.add_o(j)
g.add_xcol(26)
for i in range(27, 31):
    g.add_x(i)
g.add_ocol(29)
for j in range(28, 24, -1):
    g.add_o(j)
g.add_o(24)
g.add_xcol(25)
for i in range(26, 28):
    g.add_x(i)
g.add_ocol(26)
g.add_o(25)
g.add_o(24)


# get new price
def get_high_price(daily_high):
    i = 0
    while g.x_vals[i] <= daily_high:
        high_price = g.x_vals[i]
        i += 1
    return high_price

def get_low_price(daily_low):
    i = 0
    while g.x_vals[::-1][i] >= daily_low:
        low_price = g.x_vals[::-1][i]
        i += 1
    return low_price


# update graph
def action(daily_high, daily_low):
    if g.trend == 'x':

        # establish action points
        ap_high = g.x_vals[g.x_vals.index(g.price) + 1]
        ap_low = g.x_vals[g.x_vals.index(g.price) - 3]
        
        # check daily high, did it rise?
        if daily_high >= ap_high:

            # add appropriate x's
            for i in g.x_vals[g.x_vals.index(ap_high): g.x_vals.index(get_high_price(daily_high)) + 1]:
                g.add_x(i)

        else:
            # 3 box reversal?
            if daily_low <= ap_low:

                # add new o column
                g.add_ocol(ap_low + 2)
                for i in g.x_vals[g.x_vals.index(ap_low) + 2: g.x_vals.index(get_low_price(daily_low)) -1: -1]:
                    g.add_o(i)

    # handle later after we take care of x's
    elif g.trend == 'o':
        
        # establish action points
        ap_low = g.x_vals[g.x_vals.index(g.price) - 1]
        ap_high = g.x_vals[g.x_vals.index(g.price) + 3]

        # check daily low, did it fall?
        if daily_low <= ap_low:

            # add appropriate x's
            for i in g.x_vals[g.x_vals.index(ap_low) + 2: g.x_vals.index(get_low_price(daily_low)) -1: -1]:
                g.add_o(i)

        else:
            # 3 box reversal?
            if daily_high >= ap_high:

                # add new o column
                g.add_xcol(ap_high - 2)
                for i in g.x_vals[g.x_vals.index(ap_high) - 1: g.x_vals.index(get_high_price(daily_high)) + 1]:
                    g.add_x(i)

    # new graph    
    else:
        g.add_xcol(get_high_price(daily_high))

    g.printgrid()

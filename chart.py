# create Grid
class Grid:

    # Grid object has two parameters: start and end
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.y_vals = self.get_yvals(start, end)
        self.grid = self.grid()
        self.trend = None
        self.price = None

    # get y-values
    def get_yvals(self, start, end):
        li = [.25 * i for i in range(0, 20)] + [.5 * i for i in range(10, 40)] + list(range(20,100)) + list(range(100, 1000, 2)) + list(range(1000, 10000, 10))
        y_vals = [i for i in li if i < self.start and i > self.end]
        return y_vals

    # create grid
    def grid(self):
        grid = []
        for y in self.y_vals:
            grid.append(str(y) + '|' + '\t')
        return grid[::-1]

    # new x column
    def add_xcol(self, price):
        for row in self.grid:
            if float(row.split('|')[0]) == float(price):
                self.grid[self.grid.index(row)] += 'x'
                self.trend = 'x'
                self.price = float(row.split('|')[0])
            else:
                self.grid[self.grid.index(row)] += ' '

    # new o column
    def add_ocol(self, price):
        for row in self.grid:
            if float(row.split('|')[0]) == float(price):
                self.grid[self.grid.index(row)] += 'o'
                self.trend = 'o'
                self.price = float(row.split('|')[0])
            else:
                self.grid[self.grid.index(row)] += ' '

    # add x to existing column
    def add_x(self, price):
        for row in self.grid:
            if float(row.split('|')[0]) == float(price):
                self.grid[self.grid.index(row)] = self.grid[self.grid.index(row)][:-1] + 'x'
                self.trend = 'x'
                self.price = float(row.split('|')[0])
                
    # add o to existing column
    def add_o(self, price):
        for row in self.grid:
            if float(row.split('|')[0]) == float(price):
                self.grid[self.grid.index(row)] = self.grid[self.grid.index(row)][:-1] + 'o'
                self.trend = 'o'
                self.price = float(row.split('|')[0])

    # get new price
    def get_high_price(self, daily_high):
        i = 0
        while self.y_vals[i] <= daily_high:
            high_price = self.y_vals[i]
            i += 1
        return high_price
    def get_low_price(self, daily_low):
        i = 0
        while self.y_vals[::-1][i] >= daily_low:
            low_price = self.y_vals[::-1][i]
            i += 1
        return low_price

    # demand
    def action(self, daily_high, daily_low):
        if self.trend == 'x':

            # establish action points
            ap_high = self.y_vals[self.y_vals.index(self.price) + 1]
            ap_low = self.y_vals[self.y_vals.index(self.price) - 3]
            
            # check daily high, did it rise?
            if daily_high >= ap_high:

                # add appropriate x's
                for i in self.y_vals[self.y_vals.index(ap_high): self.y_vals.index(self.get_high_price(daily_high)) + 1]:
                    self.add_x(i)

            else:
                # 3 box reversal?
                if daily_low <= ap_low:

                    # add new o column
                    self.add_ocol(ap_low + 2)
                    for i in self.y_vals[self.y_vals.index(ap_low) + 2: self.y_vals.index(self.get_low_price(daily_low)) -1: -1]:
                        self.add_o(i)

        # supply
        elif self.trend == 'o':
            
            # establish action points
            ap_low = self.y_vals[self.y_vals.index(self.price) - 1]
            ap_high = self.y_vals[self.y_vals.index(self.price) + 3]

            # check daily low, did it fall?
            if daily_low <= ap_low:

                # add appropriate x's
                for i in self.y_vals[self.y_vals.index(ap_low) + 2: self.y_vals.index(self.get_low_price(daily_low)) -1: -1]:
                    self.add_o(i)

            else:
                # 3 box reversal?
                if daily_high >= ap_high:

                    # add new o column
                    self.add_xcol(ap_high - 2)
                    for i in self.y_vals[self.y_vals.index(ap_high) - 1: self.y_vals.index(self.get_high_price(daily_high)) + 1]:
                        self.add_x(i)

        # new graph    
        else:
            self.add_xcol(self.get_high_price(daily_high))
                
    # display grid
    def printgrid(self):
        for row in self.grid:
            print(row)

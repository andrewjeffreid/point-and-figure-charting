# create Grid
class Grid:

    # Grid object has two parameters: start and end
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.grid = self.grid()
        self.trend = None
        self.price = None

    # create grid
    def grid(self):
        grid = []
        self.x_vals = [1 * i for i in range(self.start, self.end)]
        for x in self.x_vals:
            grid.append(str(x) + '| ')
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
                
    # display grid
    def printgrid(self):
        for row in self.grid:
            print(row)
    
# test
"""
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

g.printgrid()
"""

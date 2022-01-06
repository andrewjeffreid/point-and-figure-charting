import random

g = Grid(20,31)

# generate random days
def run_simulation(num):
    for i in range(num):
        daily_high = random.randint(21, 29)
        daily_low = random.randint(21, 29)
        action(daily_high, daily_low)

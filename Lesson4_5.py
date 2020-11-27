from functools import reduce
our_list = [el for el in range(100,1001) if el % 2 == 0]
print(reduce(lambda x, y: x*y, our_list))

import collections

big_list = [ i for i in range(30 * 1000 *1000)]
# print(big_list[29000000])
# print(len(big_list))
i = 198292
if i in big_list:
    print("horray")

big_deque = collections.deque([ i for i in range(30 * 1000 *1000)])

i = 198292
if i in big_deque:
    print("horray")
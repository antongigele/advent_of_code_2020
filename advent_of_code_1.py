import numpy as np

zahlen = np.loadtxt("advent_of_code_1.txt", dtype = "int", delimiter = "\n")

for i in zahlen:
    for j in zahlen:
        if i + j == 2020:
            print(i*j)
#-----------------------------------------------#
for i in zahlen:
    for j in zahlen:
        for k in zahlen:
            if i + j + k == 2020:
                print(i*j*k)       
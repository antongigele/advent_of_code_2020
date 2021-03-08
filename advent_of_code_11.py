import numpy as np
import math

def read_data_as_array(file, datatype = "str", delimiter = "\n"):
    matrix = np.loadtxt(file, dtype = datatype, delimiter = delimiter)
    # codierung
    # L = 0
    # # = 1
    # . = 10   
    list_of_lists = [[0 if letter == 'L' else 10 for letter in line] for line in matrix]
    seat_array = np.array(list_of_lists)

    dim = seat_array.shape
    # einbettungsarray eine Schicht als rand rundherum -> kein indexerror
    seat_array_bed = np.full((dim[0]+2, dim[1]+2), 0, dtype = int)
    seat_array_bed[1:-1,1:-1] = seat_array
    return seat_array_bed
   
def first_seating_round(seat_array):
    dim = seat_array.shape
    # erste sitzrunde
    for i in range(1, dim[0]-1):
        for j in range(1, dim[1]-1):
            if seat_array[i][j] == 0:
                seat_array[i][j] = 1
    return seat_array            

# Adjazenzmatrix eines Sitzshuffles
def info_array(seat_array):
    dim = seat_array.shape
    adjacency_matrix = np.full((dim[0], dim[1]), 0, dtype = int)
    for i in range(1, dim[0]-1):
        for j in range(1, dim[1]-1):
            if  seat_array[i][j] != 10:
                adj_sum = (seat_array[i-1][j]
                + seat_array[i-1][j+1]
                + seat_array[i][j+1]
                + seat_array[i+1][j+1]
                + seat_array[i+1][j]
                + seat_array[i+1][j-1]
                + seat_array[i][j-1]
                + seat_array[i-1][j-1])
                adj_sum = int(str(adj_sum)[-1])
                adjacency_matrix[i][j] = (adj_sum)
    return adjacency_matrix        


def single_reshuffle_cycle(seat_array, adjacency_matrix):
    dim = seat_array.shape # seat_array und adjacency_matrix haben dieselbe dimension
    # -ändere die sitzbesetzung anhand der adjazenz-matrix
    for i in range(1, dim[0]-1):
        for j in range(1, dim[1]-1):
            if seat_array[i][j] == 0 and adjacency_matrix[i][j] == 0:
                seat_array[i][j] = 1
            elif seat_array[i][j] == 1 and adjacency_matrix[i][j] > 3:
                seat_array[i][j] = 0
    # -erstelle eine neue adjazenzmatrix nach der neuen sitzbesetzung
    new_adjacency_matrix = info_array(seat_array)
    # -returne die neue sitzbesetzung und die neue adjazenz-matrix
    return seat_array, new_adjacency_matrix

def areSame(A,B):
   dim = A.shape
   for i in range(1, dim[0]-1):
      for j in range(1, dim[1]-1):
         if (A[i][j] != B[i][j]):
            return 0
   return 1

def multiple_reshuffle_cycles(previous_cycle, adjacency_matrix):
    dim = previous_cycle.shape
    # -einen zyklus durchführen
    next_cycle = single_reshuffle_cycle(previous_cycle, adjacency_matrix)
    # -zuerst prüfen ob new_adjacency_matrix == adjacency_matrix gilt
    if areSame(next_cycle[1], adjacency_matrix) == 1:
        sum = 0
        print("Boolean triggered")
        for i in range(1, dim[0]-1):
            for j in range(1, dim[1]-1):
                if previous_cycle[i][j] == 1:
                    sum += 1
        return sum, next_cycle           
    
    else:
        # -zyklusrekursion aufrufen
        return multiple_reshuffle_cycles(next_cycle[0], next_cycle[1])


def main():
    start_array = read_data_as_array("test_11.txt")
    seat_array = first_seating_round(start_array)
    print(seat_array)
    adjacency_matrix = info_array(seat_array)
    print(adjacency_matrix)

    # first_cycle = single_reshuffle_cycle(seat_array, adjacency_matrix)
    # second_cycle = single_reshuffle_cycle(first_cycle[0], first_cycle[1])
    # third_cycle = single_reshuffle_cycle(second_cycle[0], second_cycle[1])
    # fourth_cycle = single_reshuffle_cycle(third_cycle[0], third_cycle[1])
    # fifth_cycle = single_reshuffle_cycle(fourth_cycle[0], fourth_cycle[1])
    # sixth_cycle = single_reshuffle_cycle(fifth_cycle[0], fifth_cycle[1])
    # print(first_cycle[1])
    # print(second_cycle[1])
    # print(third_cycle[1])
    # print(fourth_cycle[1])
    # print(fifth_cycle[1])
    # first round is still correct
    # print(first_cycle[0])
    # print(first_cycle[2])
    # print(fifth_cycle[0])
    # print(areSame(fifth_cycle[1], sixth_cycle[1]))

    # next_cycle = single_reshuffle_cycle(seat_array, adjacency_matrix)
    # aloa_cylce = single_reshuffle_cycle(next_cycle[0], next_cycle[1])
    # print(seat_array)
    # print(next_cycle[0])
    # print(aloa_cylce)
    print(multiple_reshuffle_cycles(seat_array, adjacency_matrix)[0])

if __name__ == "__main__":
    main()    
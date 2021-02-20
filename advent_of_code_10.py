from scipy.special import comb

def read_data(path):
    try:
        file = open(path, 'r')
    except:
        print('file ', path, ' wurde nicht gefunden')
        quit()

    data = file.readlines()
    file.close()

    return(data)

def listcreater(data, sep = None, replace_old = None, replace_new = None):
    if sep is not None:
        sep_list = data.split(sep)
        if replace_old is not None:
            for e in range(len(sep_list)):
                sep_list[e] = sep_list[e].replace(replace_old, replace_new)
        return sep_list        
    else:
        for e in range(len(data)):
            data[e] = data[e].replace(replace_old, replace_new)          
        return data

#-----------------------part1----------------------#

def climb_up(data):
    list_of_ones = []
    list_of_threes = [3]
    int_data = [int(i) for i in data]
    int_data.sort()
    if int_data[0] == 1:
        list_of_ones.append(1)
    for i in range(len(int_data)-1):
        if int_data[i+1] - int_data[i] == 1:
            list_of_ones.append(1)
        elif int_data[i+1] - int_data[i] == 3:
            list_of_threes.append(3)
    return len(list_of_ones) * len(list_of_threes)        

#-----------------------part2----------------------#

def detect_differences(data):
    diff_list = []
    int_data = [int(i) for i in data]
    int_data.sort()
    for i in range(len(int_data)-2):
        if (int_data[i+1] - int_data[i] == 1) and (int_data[i+2] - int_data[i+1] == 1):
            diff_list.append(1)
    return len(diff_list)        

def binomial(n):
    binom_sum = 0
    for k in range(n+1):
        binom_sum += comb(n, k)
    return binom_sum

# math.factorial(n) // math.factorial(k) // math.factorial(n - k)

def main():
    data = read_data("test_2_10.txt")
    cleaned_data = listcreater(data, None, "\n", "")
#-----------------------part1----------------------#
#    print(climb_up(cleaned_data))

#-----------------------part2----------------------#
    print(binomial(detect_differences(cleaned_data)))
#    print(binomial(5))

if __name__ == "__main__":
    main()
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
        if (i == 0) and (int_data[i+1] - int_data[i] == 1) and (int_data[i] == 1):
            diff_list.append(int_data[i])
        if (int_data[i+1] - int_data[i] == 1) and (int_data[i+2] - int_data[i+1] == 1):
            diff_list.append(int_data[i+1])
    return diff_list    

def get_chains(diff_list): # alle ketten bestimmen
    chain_list = [''] * len(diff_list)
    chain_num = 0
    for i in range(len(diff_list)):
        if (i == 0) and (diff_list[i+1] - diff_list[i] == 1) and (diff_list[i] == 1):
            #print(f"{chain_num} {diff_list[i]}")
            chain_list[chain_num] += str(1)
        elif (i != 0) and (diff_list[i] - diff_list[i-1] == 1):
            #print(f"{chain_num} {diff_list[i]}")
            chain_list[chain_num] += str(1)
        elif (i != 0) and (diff_list[i] - diff_list[i-1] != 1) and (diff_list[i+1] - diff_list[i] == 1):
            chain_num += 1
            #print(f"{chain_num} {diff_list[i]}")
            chain_list[chain_num] += str(1)
        elif (i != 0) and (diff_list[i] - diff_list[i-1] != 1) and (diff_list[i+1] - diff_list[i] != 1):
            chain_num += 1
            #print(f"{chain_num} {diff_list[i]}")
            chain_list[chain_num] += str(1)

    chain_list = [x for x in chain_list if x] # alle leeren Einträge im Nachhinein entfernen
    return chain_list        
        
def sub_permutations(n): # anzahl der eingeschränkten permutationen
    if n == 1:
        return 2
    elif n == 2:
        return 4
    elif n == 3:
        return 7    
    elif n > 3:
        perm_list = [2,4,7]
        for i in range(3, n):
            perm_list.append(perm_list[i-1]+perm_list[i-2]+perm_list[i-3])
        return perm_list[-1]    

def calculate_perm(chain_list):
    num_perm = 1
    for e in chain_list:
        num_perm *= sub_permutations(len(e))
    return num_perm

def main():
    data = read_data("test_2_10.txt")
    cleaned_data = listcreater(data, None, "\n", "")
#-----------------------part1----------------------#
#    print(climb_up(cleaned_data))

#-----------------------part2----------------------#
    diff_list = detect_differences(cleaned_data)
    
    chain_list = get_chains(diff_list)
    print(chain_list)
    print(calculate_perm(chain_list))
#    print(sub_permutations(3))
    
if __name__ == "__main__":
    main()
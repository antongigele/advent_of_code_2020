def read_data(path):
    try:
        file = open(path,'r')
    except:
        print('file ', path, ' wurde nicht gefunden.')
        quit()

    data = file.readlines()
    file.close()

    return(data)

# zuerst alle strings "bags" und "bag" loeschen, und dann alle "contain" durch ":" ersetzen
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

def get_valid_bag(data, valid_bag_lst):
    next_bag_layer_lst = []
    for line in data:
        for i in range(len(valid_bag_lst)):
            if valid_bag_lst[i] in line:
                splitted_line = line.split()
                if not (splitted_line[0] + splitted_line[1] == valid_bag_lst[i]): # wenn die ersten zwei woerter nicht das gesuchte bag sind, man moechte nur enthaltene bags
                    next_bag_layer_lst.append(splitted_line[0]+" "+splitted_line[1])   

    new_list = list(set(next_bag_layer_lst + valid_bag_lst))
    return list(set(new_list))

def look_into_all_bags(data, valid_bag_lst):
    len_list = [] # liste welche die laenge von jeder listeniteration speichert
    i = 0
    not_ending = True
    while not_ending:
        new_list = get_valid_bag(data, valid_bag_lst)
        len_list.append(len(new_list))
        if len_list[i] == len_list[i-1] and i > 1: # abfrage ob zwei listen gleich lange sind, in dem fall abbrechen
            not_ending = False
        i += 1    
    return new_list


def put_bags_inside(valid_bag_lst, data):
    count = 0
    for line in data:
        for entry in valid_bag_lst:
            if entry in line:
                count += 1
                # print(line)
    return count

def main():
    data = read_data("advent_of_code_7.txt")
    #------------------part1-------------------
    cleaned_data = listcreater(data, None, "\n", "")
    cleaned_data = listcreater(cleaned_data, None, "contain", ":")
    cleaned_data = listcreater(cleaned_data, None, " bags", "")
    cleaned_data = listcreater(cleaned_data, None, " bag", "")
    cleaned_data = listcreater(cleaned_data, None, ".", "")

    valid_bag_lst = ["shiny gold"]
    print(look_into_all_bags(cleaned_data, valid_bag_lst))
    # second_layer = get_valid_bag(cleaned_data, valid_bag_lst)
    # third_layer = get_valid_bag(cleaned_data, second_layer)
    # fourth_layer = get_valid_bag(cleaned_data, third_layer)
    # print(second_layer)
    # print(third_layer)
    # fourth_layer.remove("shiny gold")
    # print(fourth_layer)
    # print(put_bags_inside(valid_bag_lst, data))
    #------------------------------------------
if __name__ == "__main__":
    main()
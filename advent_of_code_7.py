import pandas

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

def get_valid_bag(data, valid_bag_lst, len_list = []):
    next_bag_layer_lst = [] # next_bag_layer_lst wird bei jeder iteration neu gemacht und and valid_bag_lst drangehaengt

    if len(len_list) > 2 and len_list[len(len_list)-1] == len_list[len(len_list)-2]: # abbruchbedingung, die laengenliste nimmt bei jeder iteration die laenge der returnliste auf
        return valid_bag_lst # wenn die letzte und vorletzte liste gleich lang sind, dann brich ab
            # achtung: valid_bag_lst ist immer ein neuer und aktueller input
    else:
        for line in data:
            for i in range(len(valid_bag_lst)):
                if valid_bag_lst[i] in line:
                    splitted_line = line.split()
                    if not (splitted_line[0] + splitted_line[1] == valid_bag_lst[i]): # wenn die ersten zwei woerter nicht das gesuchte bag sind, man moechte nur enthaltene bags
                        next_bag_layer_lst.append(splitted_line[0]+" "+splitted_line[1])   

        new_list = list(set(next_bag_layer_lst + valid_bag_lst))
        len_list.append(len(new_list))
        return get_valid_bag(data, new_list) # meine erste listenrekursion


def count_bags_inside(data, valid_bag_lst):
    count = 0
    for l in range(len(data)):
        for entry in valid_bag_lst:
            if entry in data[l]:
                count += 1
                data[l] = "empty"
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
    valid_bags = get_valid_bag(cleaned_data, valid_bag_lst)
    valid_bags.remove("shiny gold")

    print(count_bags_inside(cleaned_data, valid_bags))
    #------------------part1-------------------

if __name__ == "__main__":
    main()

def read_data(path):
    try:
        file = open(path,'r')
    except:
        print('file ', path, ' wurde nicht gefunden.')
        quit()

    data = file.readlines()
    file.close()

    return(data)

#-----------------------part1----------------------#
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

def get_valid_bag(data, valid_bag_lst, len_list = []): # listenlängen werden in der len_list festgehalten
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

#-----------------------part2----------------------#
def get_bag_content(data, bag):
    splitted_string_bag = bag.split() # tasche in "shiny" und "gold" aufteilen
    for line in data:
        splitted_line = line.split() # zeile im datensatz wird aufgeteilt
        if splitted_line[0] == splitted_string_bag[0] and splitted_line[1] == splitted_string_bag[1]: # such die tasche am anfang jeder zeile in der liste
            split_by_colon = line.split(":")
            inside_bag = split_by_colon[1].split(",")
            for i in range(len(inside_bag)):
                if inside_bag[i][0] == " ":
                   inside_bag[i] = inside_bag[i].replace(" ", "", 1)
                if inside_bag[i][-1] == " ":
                   inside_bag[i] = inside_bag[i][:-1]

    return inside_bag # alles was in der tasche ist als eine saubere liste mit der man arbeiten kann

# war viel einfacher als ich anfangs gedacht hatte
def try_count(data, bag_content, upper_bag_num = 0):
    lnn = 0
    if not "no other" in bag_content:
        for entry in bag_content:
            contents = entry.split(" ", 1) # erstes leerzeichen als trennzeichen
            entry_num = int(contents[0])
            entry_bag = contents[1]
            lnn += entry_num + entry_num*try_count(data, get_bag_content(data, entry_bag), entry_num)
    return lnn


def main():
    data = read_data("test_7_modified.txt") # data ist schon eine liste
    cleaned_data = listcreater(data, None, "\n", "") # mit listcreater werden alle unnötigen chars entfernt
    cleaned_data = listcreater(cleaned_data, None, "contain", ":")
    cleaned_data = listcreater(cleaned_data, None, " bags", "")
    cleaned_data = listcreater(cleaned_data, None, " bag", "")
    cleaned_data = listcreater(cleaned_data, None, ".", "")
    # print(cleaned_data)
    #------------------part1-------------------
    # valid_bag_lst = ["shiny gold"]
    # valid_bags = get_valid_bag(cleaned_data, valid_bag_lst)
    # valid_bags.remove("shiny gold") # entferne shiny gold bag aus der suchliste weil shiny gold bag nicht in sich selbst enthalten sein soll

    # print(count_bags_inside(cleaned_data, valid_bags))
    #------------------part2-------------------
    shiny_gold_bag_content = get_bag_content(cleaned_data, "shiny gold")
    content = try_count(cleaned_data, shiny_gold_bag_content)
    print(content)
    # bag_content = get_bag_content(cleaned_data,"dotted black")
    # print(bag_content)
    # print(taschen_anzahl_ast(content, len(content)-1))

if __name__ == "__main__":
    main()
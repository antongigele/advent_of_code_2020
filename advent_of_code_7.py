
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
def first_bag(data, bag):
    splitted_string_bag = bag.split()
    for line in data:
        splitted_line = line.split()
        if splitted_line[0] == splitted_string_bag[0] and splitted_line[1] == splitted_string_bag[1]:
            split_by_comma = line.split(",")
            split_by_comma[0] = split_by_comma[0].replace(bag, "")
            split_by_comma[0] = split_by_comma[0].replace(":", "")
            split_by_comma[0] = split_by_comma[0].replace(" ", "", 1)
            return split_by_comma # alles was in der tasche ist als eine saubere liste mit der man arbeiten kann

def formula(n):
    return lambda x : x + x*n

def result(x, y):
    result = formula(x)
    return result(y)

# erster bag_content ist hier: [' 5 mirrored crimson', ' 5 mirrored tan', ' 5 drab green', ' 5 shiny silver']
def content_count(data, bag_content, num_pos_bags = 0):
    counting_bags = 0


    for entry in bag_content:
        contents = entry.replace(" ","",1) # von leerzeichen säubern
        contents = contents.split(" ", 1)
        # counting_bags += int(contents[0]) # summiert über alle taschenanzahlen in der jeweiligen tasche
        
        for line in data:
            splitted_line = line.split(":")
            if contents[1] in splitted_line[0] and not "no other" in splitted_line[1]:
                print(splitted_line[1])
                # print(line)
                # print("hello")
                # print(contents[1])

                # new_bag_content = first_bag(data, contents[1])     
        # print(new_bag_content)
        # if "no other" not in bag_content:      
                return content_count(data, first_bag(data, contents[1]), counting_bags) 
        # else:
        #     end_number = num_pos_bags + counting_bags
        #     return end_number
    

def main():
    data = read_data("advent_of_code_7.txt") # data ist schon eine liste
    cleaned_data = listcreater(data, None, "\n", "") # mit listcreater werden alle unnötigen chars entfernt
    cleaned_data = listcreater(cleaned_data, None, "contain", ":")
    cleaned_data = listcreater(cleaned_data, None, " bags", "")
    cleaned_data = listcreater(cleaned_data, None, " bag", "")
    cleaned_data = listcreater(cleaned_data, None, ".", "")
    # print(cleaned_data)
    #------------------part1-------------------
    valid_bag_lst = ["shiny gold"]
    valid_bags = get_valid_bag(cleaned_data, valid_bag_lst)
    valid_bags.remove("shiny gold") # entferne shiny gold bag aus der suchliste weil shiny gold bag nicht in sich selbst enthalten sein soll

    # print(count_bags_inside(cleaned_data, valid_bags))
    #------------------part2-------------------
    shiny_gold_bag_content = first_bag(cleaned_data, "shiny gold")
    content = content_count(cleaned_data, shiny_gold_bag_content)
    # print(shiny_gold_bag_content)
    content
    # print(result(2,11))
if __name__ == "__main__":
    main()
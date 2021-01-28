
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
    splitted_string_bag = bag.split()
    for line in data:
        splitted_line = line.split()
        if splitted_line[0] == splitted_string_bag[0] and splitted_line[1] == splitted_string_bag[1]:
            split_by_comma = line.split(",")
            split_by_comma[0] = split_by_comma[0].replace(bag, "")
            split_by_comma[0] = split_by_comma[0].replace(":", "")
            split_by_comma[0] = split_by_comma[0].replace(" ", "", 1)
            return split_by_comma # alles was in der tasche ist als eine saubere liste mit der man arbeiten kann


# formula = lambda x, n : x + x*n

# erster bag_content ist hier: [' 5 mirrored crimson', ' 5 mirrored tan', ' 5 drab green', ' 5 shiny silver']
# def content_count_1(data, bag_content, bags_content_list = []):
#     bags_content_list.append(bag_content)
    
#     # print(bag_content)
#     for entry in bag_content:
#         contents = entry.replace(" ","",1) # von leerzeichen säubern
#         contents = contents.split(" ", 1)
#         # counting_bags += int(contents[0]) # summiert über alle taschenanzahlen in der jeweiligen tasche
        
#         for line in data:
#             splitted_line = line.split(":")
#             if contents[1] in splitted_line[0] and not "no other" in splitted_line[1]:
#                 print(line)

#                 content_count_1(data, get_bag_content(data, contents[1]), bags_content_list)
#                 break
#             elif contents[1] in splitted_line[0] and "no other" in splitted_line[1]:
#                 print(line)

#                 content_count_1(data, get_bag_content(data, contents[1]), bags_content_list)
#                 break
#     return bags_content_list
        
# hier nochmal die gleiche funktion
def content_count(data, bag_content, level_new_number = 0, number_list = []):

    # bags_content_list.append(bag_content)
    # print(bag_content)
    for entry in bag_content:
        contents = entry.replace(" ","",1) # von leerzeichen säubern
        contents = contents.split(" ", 1) # erstes leerzeichen als trennzeichen
        upper_level_number = int(contents[0]) 
        upper_level_bag = contents[1]
        level_new_number += upper_level_number

        # print(contents)
        for line in data:
            splitted_line = line.split(":")
            outer_bag = splitted_line[0]
            inner_bags = splitted_line[1]
            inside_upper_level_bag = inner_bags.split(",") # alle einzelnen taschen mit ihren koeffizienten in der upper_level_bag

            if upper_level_bag in outer_bag and not "no other" in inner_bags: # ist die tasche am beginn der zeile von data und die tasche nicht leer dann...
                for inner_bag_entry in inside_upper_level_bag:
                    sub_contents = inner_bag_entry.replace(" ","",1) # von leerzeichen säubern
                    sub_contents = sub_contents.split(" ", 1) # erstes leerzeichen als trennzeichen
                    lower_level_number = int(sub_contents[0])
                    lower_level_bag = sub_contents[1]
                    level_new_number += upper_level_number*lower_level_number

                    print(sub_contents)
                    content_count(data, get_bag_content(data, lower_level_bag), level_new_number)
                # break
            elif upper_level_bag in outer_bag and "no other" in inner_bags:
                number_list.append(level_new_number)
                # content_count(data, get_bag_content(data, upper_level_bag), number_list)
                # break
            
    return level_new_number




# def taschen_anzahl_ast(content, n, anzahl = 0):
#     # l = len(content)
#     if n < 1:
#         # print(l)
#         return anzahl
#     else:
#         for tasche in content[n]:
#             taschen_inhalt = tasche.split()
#             anzahl = int(taschen_inhalt[0])
#             print(anzahl)
#         # print(taschen_inhalt[0])
#         return anzahl + anzahl*taschen_anzahl_ast(content, n-1, anzahl) ## funktioniert nur für einen ast als liste wie bei "test_7_2.txt" eigentlich bräuchte man dafür jetzt jeden ast als so eine liste


def main():
    data = read_data("test_7_2.txt") # data ist schon eine liste
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
    shiny_gold_bag_content = get_bag_content(cleaned_data, "shiny gold")
    content = content_count(cleaned_data, shiny_gold_bag_content)
    print(content)
    # print(taschen_anzahl_ast(content, len(content)-1))

if __name__ == "__main__":
    main()
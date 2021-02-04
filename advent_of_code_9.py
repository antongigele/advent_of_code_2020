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
#liste der länge 25 + 1 die mit start ab irgendwo im datensatz bestimmt werden kann
def altering_list(data, start):
    alt_list = []
    for e in range(start, len(data)):
        alt_list.append(data[e])
        if e == start + 25:
            break
    return alt_list

# erstellt die summenliste der letzten 25 einträge
def find_rulebreaker(list_input):
    sum_list = []
    for i in range(len(list_input)-1):  # den letzten eintrag nicht
        for j in range(len(list_input)-1):  # den letzten eintrag nicht
            if i != j: # summanden paarweise unterschiedlich
                sum = int(list_input[i]) + int(list_input[j])
                sum_list.append(sum)
    if int(list_input[-1]) in sum_list:
        return True, f'{list_input[-1]} is in the 25-list'
    else:
        return False, f'{list_input[-1]} is a rulebreaker'          

def go_through_list(data): # die summenliste wird laufend durch alle einträge mit find_rulebreaker ermittelt
    for i in range(len(data)):
        current_list = altering_list(data, i)
        # print(find_rulebreaker(current_list))
        result = find_rulebreaker(current_list)
        if result[0] == False:
            return f'{result[1]} at position {i}'
            break

def main():
    data = read_data('advent_of_code_9.txt')
    cleaned_data = listcreater(data, None, '\n', '')
#-----------------------part1----------------------#        
    print(go_through_list(cleaned_data))

#-----------------------part2----------------------#


if __name__ == '__main__':
    main()    
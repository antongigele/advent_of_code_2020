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
        if e == start + 25: # präambel mit länge 25
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
        return False, list_input[-1]         

# die summenliste wird laufend durch alle einträge mit find_rulebreaker ermittelt
def go_through_list(data):
    for i in range(len(data)):
        current_list = altering_list(data, i)
        # print(find_rulebreaker(current_list))
        result = find_rulebreaker(current_list)
        if result[0] == False:
            return result[1], i + 25 # position, weil startposition + 25 dazu
            break

#-----------------------part2----------------------#

def partial_sums(data, rule_break_number):
    partial_sum_list = []
    partial_sum = 0
    for i in range(rule_break_number[1]):
        # if int(data[i]) < int(rule_break_number[0]): #  very partial weil alle zahlen die größer sind als der rulebreaker rausfliegen
        partial_sum += int(data[i])
        partial_sum_list.append(partial_sum)
    return partial_sum_list


def partly_partial_sums(data, rule_break_number, partial_sums, start = 0):
    for i in range(start, len(partial_sums)):
        if partial_sums[i] - partial_sums[start] == int(rule_break_number[0]): # partialsummen von aufsteigenden startpunkten weg
            print(f'Von {start + 1} bis {i}')
            return start + 1, i

def lookup_range(data, rule_break_number, partial_sums):
    for k in range(len(partial_sums)):
        result = partly_partial_sums(data, rule_break_number, partial_sums, k)
        if type(result) == tuple: # wenn die Funktion etwas zurückgibt, auf eine abstruse Art
            range_list = data[result[0]:result[1] + 1]
            return range_list # die sequenz der lösungszahlen als liste

def result(range_list):
    int_list = [int(i) for i in range_list] # alle listeneintraege in integer verwandeln
    print(min(int_list) + max(int_list))


def main():
    data = read_data('advent_of_code_9.txt')
    cleaned_data = listcreater(data, None, '\n', '')
#-----------------------part1----------------------#        
    
    rule_break_number = go_through_list(cleaned_data)
    # print(rule_break_number)
#-----------------------part2----------------------#
    partialsummen_liste = partial_sums(cleaned_data, rule_break_number)
    range_list = lookup_range(cleaned_data, rule_break_number, partialsummen_liste)
    result(range_list)
if __name__ == '__main__':
    main()    
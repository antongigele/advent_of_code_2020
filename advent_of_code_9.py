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

def altering_list(data):
    alt_list = []
    for count, entry in enumerate(data,1):
        alt_list.append(entry)
        if count == 26:
            break
    return alt_list    

def find_rulebreaker(list_input):
    sum_list = []
    for i in range(len(list_input)):
        for j in range(len(list_input)):
            if i != j:
                sum = int(list_input[i]) + int(list_input[j])
                sum_list.append(sum)
    if int(list_input[-1]) in sum_list:
        return f'{list_input[-1]} is in the 25-list'
    else:
        return f'{list_input[-1]} is a rulebreaker'          



def main():
    data = read_data('advent_of_code_9.txt')
    cleaned_data = listcreater(data, None, '\n', '')
    twentyfive_list = altering_list(cleaned_data)
    print(find_rulebreaker(twentyfive_list))

if __name__ == '__main__':
    main()    
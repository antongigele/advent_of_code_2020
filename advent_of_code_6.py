def read_data(path):
    try:
        file = open(path,'r')
    except:
        print('file ', path, ' wurde nicht gefunden.')
        quit()

    data = file.read()
    file.close()

    return(data)

def listcreater(data, sep, replace_old = None, replace_new = None):
    sep_list = data.split(sep)
    if replace_old is not None:
        for e in range(len(sep_list)):
            sep_list[e] = sep_list[e].replace(replace_old, replace_new)
    return sep_list

def main():
    data = read_data('advent_of_code_6.txt')
    print(data)
    # data_list = listcreater(data, '\n\n')
    #print(data_list)

if __name__ == '__main__':
    main()             
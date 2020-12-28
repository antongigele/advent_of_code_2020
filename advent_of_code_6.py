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

class Dictionary:
    alphabet = ['a','b','c','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    length = 26
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def dict_creater(self):
        return    

def count_questions_part1(data_list):
    l = 0
    for entry in data_list:
        l += len(set(entry))

    return l    

def count_questions_part2(data_list):
    l = 0
    for entry in data_list:
        len(entry)

def main():
    data = read_data('advent_of_code_6.txt')
    data_list = listcreater(data, '\n\n', '\n', '')
    print(count_questions_part1(data_list))

if __name__ == '__main__':
    main()             
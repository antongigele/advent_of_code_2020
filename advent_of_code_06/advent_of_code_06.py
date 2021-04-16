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
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    def __init__(self, buchstabe = 0):
        self.buchstabe = buchstabe

    def dict_creater(self):
        alphabet_dict = {letter : self.buchstabe for letter in Dictionary.alphabet}
        return alphabet_dict

def count_group_size(count_data):
    count = 0
    count_list = [entry.count('\n') + 1 for entry in count_data]

    return count_list

def count_questions_part1(data_list):
    l = 0
    for entry in data_list:
        l += len(set(entry))

    return l    

def count_questions_part2(data_list, group_size_list):
    l = 0
    for question_entry, size_entry in zip(data_list, group_size_list):
        question_dict = Dictionary().dict_creater()
        for letter in question_entry:
            if letter in question_dict:
                question_dict[letter] += 1
                
        # print(question_entry)            
        for key in question_dict:        
            if size_entry == question_dict[key]:
                # print(size_entry,key)
                l += 1    
                   
    return l

def main():
    data = read_data('advent_of_code_6.txt')
    data_list = listcreater(data, '\n\n', '\n', '')

    #---------------part1--------------#
    print(count_questions_part1(data_list))

    #---------------part2--------------#
    count_data = listcreater(data, '\n\n')
    group_size_list = count_group_size(count_data)
    print(count_questions_part2(data_list, group_size_list))
    

if __name__ == '__main__':
    main()             
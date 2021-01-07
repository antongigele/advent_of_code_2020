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

def get_valid_bag(data):
    initial_state = "shiny gold bag"
    valid_bag_lst = []
    for line in data:
        if initial_state in line:
            splitted_three = line.split()
            if not (splitted_three[0] == "shiny" and splitted_three[1] == "gold"):
                if splitted_three[2][-1:] == "s":
                    valid_bag_lst.append(splitted_three[0]+" "+splitted_three[1]+" "+splitted_three[2][:-1])
                else:
                    valid_bag_lst.append(splitted_three[0]+" "+splitted_three[1]+" "+splitted_three[2])

    return valid_bag_lst

def put_bags_inside(valid_bag_lst, data):
    count = 0
    for line in data:
        for entry in valid_bag_lst:
            if entry in line:
                count += 1
                # print(line)
    return count

def main():
    data = read_data("advent_of_code_7_2.txt")
    #------------------part1-------------------
    valid_bag_lst = get_valid_bag(data)
    print(valid_bag_lst)
    print(put_bags_inside(valid_bag_lst, data))
    #------------------------------------------
if __name__ == "__main__":
    main()
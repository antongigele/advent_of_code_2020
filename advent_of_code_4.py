def read_data(path):
    try:
        file = open(path,"r")
    except:
        print("File", path, "wurde nicht gefunden.")
        quit()

    data = file.read()
    file.close()

    return data

def listcreater(data, sep, replace_old, replace_new):
    sep_list = data.split(sep)
    for e in range(len(sep_list)):
        sep_list[e] = sep_list[e].replace(replace_old, replace_new)
    return sep_list

# check for:
    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID)

def checkcredentials(data_list):
    count_part1 = 0
    for entry in data_list:
        if ("byr" in entry 
        and "iyr" in entry 
        and "eyr" in entry 
        and "hgt" in entry
        and "hcl" in entry
        and "ecl" in entry
        and "pid" in entry):
            count_part1 += 1

    return count_part1

def create_dict(data_list):
    # count_break = 0
    dictlist = []
    for i, entry in enumerate(data_list):
        xlist = entry.split(" ") # ['byr:1962', 'pid:547578491', 'eyr:2028', 'ecl:hzl', 'hgt:65in', 'iyr:2013', 'hcl:#623a2f']
        tuplelist = []
        for subentry in xlist:
            ylist = subentry.split(":") # ['hcl', '#623a2f']
            ytuple = tuple(ylist) # ('hcl', '#623a2f')
            tuplelist.append(ytuple) # create list of tuples like above
        dictlist.append(dict(tuplelist)) #  create list of dict-turned lists  
        # count_break += 1
        # if count_break == 2:
        #     break 

    return dictlist

def main():
    data = read_data("advent_of_code_4.txt")
    data_list = listcreater(data, "\n\n", "\n", " ")
    # print(checkcredentials(data_list))
    dict_list = create_dict(data_list)
    print(dict_list)
if __name__ == "__main__":
    main()    
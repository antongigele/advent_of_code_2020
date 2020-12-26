import re

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

def height(dict_entry):
    
    return  ((((re.search('cm$',dict_entry) is not None) == True) and (int(dict_entry[:-2]) in range(150,193 + 1)))
    or (((re.search('in$',dict_entry) is not None) == True) and (int(dict_entry[:-2]) in range(59,76 + 1))))

def check_additional_cred(dict_list):
    count_part2 = 0
    for dict in dict_list:
        if ("byr" in dict 
        and "iyr" in dict 
        and "eyr" in dict 
        and "hgt" in dict
        and "hcl" in dict
        and "ecl" in dict
        and "pid" in dict):
            if ((len(dict['byr']) == 4 and int(dict['byr']) in range(1920, 2002 + 1))
            and (len(dict['iyr']) == 4 and int(dict['iyr']) in range(2010, 2020 + 1))
            and (len(dict['eyr']) == 4 and int(dict['eyr']) in range(2020, 2030 + 1))
            and (height(dict['hgt']) == True)
            and (len(dict['hcl']) == 7 and re.search('^#[0-9a-f]{6}', dict['hcl']) is not None)
            and (dict['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'})
            and (len(dict['pid']) == 9 and re.search('[0-9]{9}', dict['pid']) is not None)):
                count_part2 += 1
    return count_part2            

def main():
    data = read_data("advent_of_code_4.txt")
    data_list = listcreater(data, "\n\n", "\n", " ")
    dict_list = create_dict(data_list)
    print(check_additional_cred(dict_list))
    print(height('167cm'))

if __name__ == "__main__":
    main()    
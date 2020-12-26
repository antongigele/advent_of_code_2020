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
    if (re.search('cm$',dict['hgl']) is not None and int(dict['hgl'][:-2]) in range(150,193 + 1) == True
    or re.search('in$',dict['hgl']) is not None and int(dict['hgl'][:-2]) in range(59,76 + 1) == True):
        return True

def check_additional_cred(dict_list):
    count_part2 = 0
    for dict in dict_list:
        if ((len(dict['byr']) == 4 and 1920 < int(dict['byr']) < 2002)
        and (len(dict['iyr']) == 4 and 2010 < int(dict['iyr']) < 2020)
        and (len(dict['eyr']) == 4 and 2020 < int(dict['eyr']) < 2030)
        and ()    
        and (len(dict['hcl']) == 7 and re.search('^#[0-9a-f]{6}', dict['hcl']) is not None)
        and (dict['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'})
        and (len(dict['pid']) == 9 and re.search('^000', dict['pid']) is not None)
        ):
            pass

def main():
    data = read_data("advent_of_code_4.txt")
    data_list = listcreater(data, "\n\n", "\n", " ")
    dict_list = create_dict(data_list)
    print(check_additional_cred(dict_list))


if __name__ == "__main__":
    main()    
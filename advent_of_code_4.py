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
    pass

def main():
    data = read_data("advent_of_code_4.txt")
    data_list = listcreater(data, "\n\n", "\n", " ")

if __name__ == "__main__":
    main()    
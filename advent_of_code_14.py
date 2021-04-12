
def read_data(path):
    try:
        file = open(path, 'r')
    except:
        print('file ', path, ' wurde nicht gefunden')
        quit()

    data = file.readlines()
    file.close()

    return(data)

def dict_list_creater(data):
    cleaned_data = []
    for e in data:
        e = e.replace("\n", "").replace("mem[", "").replace("]", "").replace(" ","")
        cleaned_data.append(dict([e.split("=")]))
    return cleaned_data    

def dec_to_bin(decimal): # verwandelt die zahl in binary-format mit führenden nullen
    bin_num = bin(int(decimal))[2:]
    for _ in range(36-len(bin_num)):
        bin_num = "0" + bin_num
    return bin_num

def bin_to_dec(binary): # verwandelt die zahl in decimal
    decimal = int(binary, base = 2)
    return decimal

#-----------------------part1----------------------#
def apply_mask(mask, decimal): # wendet die maske an, mask ist ein string
    binary_num = dec_to_bin(decimal)
    for i, e in enumerate(mask):
        if e == "X":
            pass
        elif e == "1":
            binary_num = binary_num[:i] + e + binary_num[i+1:]
        elif e == "0":
            binary_num = binary_num[:i] + e + binary_num[i+1:]
    return binary_num   

def memory_dict(dict_list):
    mask = ""
    mem_dict = {}
    for i in range(len(dict_list)):
        if "mask" in dict_list[i].keys():
            mask = dict_list[i].get("mask")
        else:
            values_view = dict_list[i].values()
            value_iterator = iter(values_view)
            first_value = next(value_iterator)
            first_key = next(iter(dict_list[i]))

            mem_dict.update({first_key : bin_to_dec(apply_mask(mask, first_value))}) # dict jedes mal um key-value pair erweitern
    return mem_dict

def sum_memory_values(mem_dict):
    # mem_sum = 0
    # for value in mem_dict.values():
    #     mem_sum += value
    values = mem_dict.values()
    values = list(map(int, values))

    return sum(values)

#-----------------------part2----------------------#

def apply_mask_with_X(mask, decimal): # wendet die maske an, mask ist ein string
    binary_num = dec_to_bin(decimal)
    for i, e in enumerate(mask):
        if e == "X":
            binary_num = binary_num[:i] + e + binary_num[i+1:]
        elif e == "1":
            binary_num = binary_num[:i] + e + binary_num[i+1:]
        elif e == "0":
            pass
    return binary_num

def gen_adr_list(s, mem_adr = []):
    if 'X' in s:
        s1 = s.replace('X','0',1) #only replace once
        s2 = s.replace('X','1',1) #only replace once
        gen_adr_list(s1, mem_adr)
        gen_adr_list(s2, mem_adr)
    else: mem_adr.append(s)
    return mem_adr

def mem_adr_dict(dict_list):
    output_dict = {}
    mask = ""
    for i in range(len(dict_list)):
        if "mask" in dict_list[i].keys():
            mask = dict_list[i].get("mask")
        else:
            values_view = dict_list[i].values()
            value_iterator = iter(values_view)
            first_value = next(value_iterator)
            first_key = next(iter(dict_list[i]))

            mem_adr = gen_adr_list(apply_mask_with_X(mask, first_key), mem_adr = [])
            mem_adr = [bin_to_dec(e) for e in mem_adr]

            for a in mem_adr:
                output_dict.update({a : first_value}) # dictionary wird immer upgedated: neue werte dazuschreiben oder alte überschreiben
    return output_dict

#-----------------------main----------------------#

def main():
    data = read_data("advent_of_code_14/advent_of_code_14.txt")
    dict_list = dict_list_creater(data)
#-----------------------part1----------------------#    
    mem_dict = memory_dict(dict_list)
    print(sum_memory_values(mem_dict))
#-----------------------part2----------------------#
    humongous_mem_dict = mem_adr_dict(dict_list)
    print(sum_memory_values(humongous_mem_dict))

    # # Ein durchlauf mit zwei schritten
    # # 1.schritt
    # this_mem_dict = {}
    # value = "100"
    # mem_adr = gen_adr_list(apply_mask_with_X("000000000000000000000000000000X1001X", "42"), mem_adr = [])
    # mem_adr = [bin_to_dec(e) for e in mem_adr]
    # for a in mem_adr:
    #     this_mem_dict.update({a : value})
    # print(this_mem_dict)
    # # 2.schritt
    # value2 = "1"   
    # mem_adr2 = gen_adr_list(apply_mask_with_X("00000000000000000000000000000000X0XX", "26"), mem_adr = [])
    # mem_adr2 = [bin_to_dec(e) for e in mem_adr2]
    # for a in mem_adr2:
    #     this_mem_dict.update({a : value2})
    # print(this_mem_dict)

    # values = this_mem_dict.values()
    # values = list(map(int, values))
    # print(sum(values))

if __name__ == "__main__":
    main()    

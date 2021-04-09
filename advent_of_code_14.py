
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

            # print(bin_to_dec(apply_mask(mask, first_value)))
            # print(first_key)
            mem_dict.update({first_key : bin_to_dec(apply_mask(mask, first_value))})

    return mem_dict

def sum_memory_values(mem_dict):
    mem_sum = 0
    for value in mem_dict.values():
        mem_sum += value
    return mem_sum

def main():
    data = read_data("advent_of_code_14/advent_of_code_14.txt")
    dict_list = dict_list_creater(data)
    mem_dict = memory_dict(dict_list)
    print(sum_memory_values(mem_dict))

if __name__ == "__main__":
    main()    

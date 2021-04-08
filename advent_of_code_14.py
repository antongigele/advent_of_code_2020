
def read_data(path):
    try:
        file = open(path, 'r')
    except:
        print('file ', path, ' wurde nicht gefunden')
        quit()

    data = file.readlines()
    file.close()

    return(data)

def dec_to_bin(decimal): # verwandelt die zahl in binary-format mit führenden nullen
    bin_num = bin(int(decimal))[2:]
    for _ in range(36-len(bin_num)):
        bin_num = "0" + bin_num
    return bin_num

def bin_to_dec(binary): # verwandelt die zahl in decimal
    decimal = int(binary, base = 2)
    return decimal

def apply_mask(mask, decimal): # wendet die maske an
    binary_num = dec_to_bin(decimal)
    for i, e in enumerate(mask):
        if e == "X":
            pass
        elif e == "1":
            binary_num = binary_num[:i] + e + binary_num[i+1:]
        elif e == "0":
            binary_num = binary_num[:i] + e + binary_num[i+1:]
    return binary_num   

def main():
    data = read_data("advent_of_code_14/test_14.txt")
    print(f"11 = {dec_to_bin('11')}")
    applied_value = apply_mask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", "11")
    print(bin_to_dec(applied_value))

if __name__ == "__main__":
    main()    

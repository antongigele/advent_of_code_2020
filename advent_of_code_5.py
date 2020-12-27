def read_data(path):
    try:
        file = open(path,"r")
    except:
        print("File", path, "wurde nicht gefunden.")
        quit()

    data = file.readlines()
    file.close()

    return data

def list_cleaner(data, replace_old, replace_new):
    cleaned_data = [data[e].replace(replace_old, replace_new) for e in range(len(data))]

    return cleaned_data

def bin_to_dec(bin):
    l = len(str(bin)) - 1
    dec_num = 0
    for count, binary in enumerate(str(bin)):
        dec_num += int(binary)*2**(l-count) # turn any binary into decimal
    return dec_num    

def list_to_dec(bin_data, start, end):
    # for entry in bin_data:
    #     bin_to_dec(int(entry[:-3]))
    dec_data = [bin_to_dec(int(entry[start:end])) for entry in bin_data]    
    return dec_data

def main():
    data = read_data('advent_of_code_5.txt')
    cleaned_data = list_cleaner(data,'\n','') # remove "\n"
    bin_data = list_cleaner(list_cleaner(list_cleaner(list_cleaner(cleaned_data,'B','1'),'F','0'),'L','0'),'R','1') # turn completely into binary
    dec_data_row = [bin_to_dec(int(entry[:-3])) for entry in bin_data]
    dec_data_col = [bin_to_dec(int(entry[-3:])) for entry in bin_data]

    seat_id_list = [ a*8 + b for a, b in zip(dec_data_row, dec_data_col)]

    print(seat_id_list)
if __name__ == "__main__":
    main()     
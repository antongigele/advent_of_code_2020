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

def remover(seat_id_list, lower_bound, upper_bound):
    removal_list = [entry for entry in seat_id_list if (int(entry) in range(lower_bound, upper_bound + 1))]

    return removal_list
    
def main():
    data = read_data('advent_of_code_5.txt')
    cleaned_data = list_cleaner(data,'\n','') # remove "\n"
    bin_data = list_cleaner(list_cleaner(list_cleaner(list_cleaner(cleaned_data,'B','1'),'F','0'),'L','0'),'R','1') # turn completely into binary
    
    dec_data_row = [bin_to_dec(int(entry[:-3])) for entry in bin_data] # convert till last 3rd position
    dec_data_col = [bin_to_dec(int(entry[-3:])) for entry in bin_data] # convert from last 3rd position

    seat_id_list = [ row*8 + col for row, col in zip(dec_data_row, dec_data_col)] # multiply the two lists
    print(max(seat_id_list))
    print(min(seat_id_list))

    smaller_list = remover(seat_id_list, 100, 800)
    print(smaller_list)

if __name__ == "__main__":
    main()     
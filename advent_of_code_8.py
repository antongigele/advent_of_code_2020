def read_data(path):
    try:
        file = open(path,"r")
    except:
        print("File", path, "nicht gefunden")
        quit()

    data = file.readlines()
    file.close()
    return data

def count_dict(data):
    command_count_dict = {i : 0 for i in range(len(data))}

    return command_count_dict    

def command_runner(data, count_dict):
    # for line in data:
        
    i = 0
    acc = 0
    while i < len(data):
        if "nop" in data[i] and count_dict[i] == 0:
            count_dict[i] = count_dict[i] + 1
            i += 1
        elif "acc" in data[i] and count_dict[i] == 0:
            splitted_line = data[i].split()
            acc += int(splitted_line[1])
            count_dict[i] = count_dict[i] + 1
            print(acc)
            i += 1
        elif "jmp" in data[i] and count_dict[i] == 0:
            splitted_line = data[i].split()
            count_dict[i] = count_dict[i] + 1
            i += int(splitted_line[1])
        else:
            i += 1       
    return acc, count_dict

def main():
    data = read_data("advent_of_code_8.txt")
#-------------------part1---------------------#
    count_command_dict = count_dict(data)
    print(command_runner(data, count_command_dict))

if __name__ == "__main__":
    main()        
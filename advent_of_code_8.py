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

def command_runner_part1(data, count_dict):
    i = 0
    acc = 0
    loop_indices = []
    while True:
        if "nop" in data[i] and count_dict[i] == 0:
            count_dict[i] = count_dict[i] + 1
            loop_indices.append(i)
            i += 1
        elif "acc" in data[i] and count_dict[i] == 0:
            splitted_line = data[i].split()
            acc += int(splitted_line[1])
            count_dict[i] = count_dict[i] + 1
            loop_indices.append(i)
            i += 1
        elif "jmp" in data[i] and count_dict[i] == 0:
            splitted_line = data[i].split()
            count_dict[i] = count_dict[i] + 1
            loop_indices.append(i)
            i += int(splitted_line[1])
        else:
            break       
    return count_dict, acc, loop_indices

def find_exitpoints(data):
    jumpout = 1
    count_exitpoints = 0
    exitpoints = []
    for i in range(len(data)-1, -1, -1):
        splittet_line = data[i].split()
        if splittet_line[0] == "acc":
            exitpoints.append(i)
            # print(data[i] + "ist Ausstiegspunkt")
            count_exitpoints += 1
        elif splittet_line[0] == "jmp" and splittet_line[1] == "+" + str(jumpout):
            exitpoints.append(i)
            # print(data[i] + "\nist Ausstiegspunkt")
            count_exitpoints += 1
        elif splittet_line[0] == "nop":
            exitpoints.append(i)
            # print(data[i] + "ist Ausstiegspunkt")
            count_exitpoints += 1
        else:
            break    
        jumpout += 1
    return exitpoints      

def exit_point_connect(data):
    zeros_dict = count_dict(data) # neues dict mit nur nullen als values
    used_and_unused_entries_dict = command_runner_part1(data, zeros_dict)[0] #part1 durchlaufen lassen um zu sehen welche commands ausserhalb der schleife liegen im dictionary
    exit_points = find_exitpoints(data) # Ausstiegspunkte wiedergeben als liste
    loop_indices = command_runner_part1(data, zeros_dict)[2]
    # for k, v in used_and_unused_entries_dict.items():
    #     if k == "jmp" and v in exit_points:
    #         print(k)
    print(command_runner_part1(data, zeros_dict)[2]) # is printing an empty list for some reason!
    # for i in lo_indices:
    #     print(data[i])op

    loop_size = sum(1 for value in used_and_unused_entries_dict.values() if value == 1)

    return used_and_unused_entries_dict, exit_points
    
    # print(command_runner_part1(data, count_command_dict)) 

def main():
    data = read_data("advent_of_code_8.txt")
    count_command_dict = count_dict(data)
#-------------------part1---------------------#    
    # print(command_runner_part1(data, count_command_dict))
#-------------------part2---------------------#
    exit_point_connect(data)


if __name__ == "__main__":
    main()        
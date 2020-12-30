# #!/bin/bash

while read line || [ -n "$line" ] ;
    do 
        # echo "$line"
        array[$i]="$line"
        let i++ ;

    done < advent_of_code_7.txt    
for ((i=0;i<=20;i++))
    do
        IFS=' ' read -a arr <<< ${array[i]}
        string_array[i]=$arr
        # if [[ ${array[i]} == *"shiny gold bags"* ]]; then
        #     num=$(($i + 1))
        #     echo "There it is in line ${num}";
        # fi
        # echo "${string_array[i]}"    
    done

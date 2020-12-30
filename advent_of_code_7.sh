# #!/bin/bash

while read line || [ -n "$line" ] ;
    do 
        # echo "$line"
        array[$i]="$line"
        let i++ ;

    done < advent_of_code_7.txt    
for ((i=0;i<=20;i++))
    do
        # if [[ ${array[i]} == *"shiny gold bags"* ]]; then
        #     num=$(($i + 1))
        #     echo "There it is in line ${num}";
        # fi    
    done
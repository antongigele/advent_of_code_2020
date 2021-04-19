#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define MAXCHAR 50 // maximale länge der Zeilen plus 5

#define NUMBER_OF_STRING 4
#define MAX_STRING_SIZE 40
#define DEST_SIZE 100


int count_file_len(char *path) {
    FILE *fp;
    char c;
    int count = 1;

    fp = fopen(path, "r");
    if (fp == NULL){
        printf("Could not open file %s",path);
        return 1;
    }
    for (c = getc(fp);c != EOF;c = getc(fp)) {
        if (c == '\n') {
            count++;
        }
    }
    fclose(fp);

    return count;
}

static void string_arr(char *p[]) {
    p[0] = "Hello";
    p[1] = "World!";
}

static void read_in_arr(char *input[], char *path) {

    FILE *fptr = NULL; 
    int i = 0;
    int tot = 0;	
    int F_ROWS = count_file_len(path);
    char line[F_ROWS][MAXCHAR];
    fptr = fopen(path, "r");
    while(fgets(line[i], MAXCHAR, fptr)) {
        if (line[i][strlen(line[i])-1] == '0') {
            line[i][strlen(line[i])] = '\0';
            i++;
        }
        else {
            line[i][strlen(line[i])-1] = '\0';
            i++;
        }
    }
}

int main() {

    char *strings[2];
    string_arr(strings);
    printf("%s %s\n", strings[0], strings[1]);

    // int i;

    // char ch_arr[3][10] = {
    //                          "spike",
    //                          "tom",
    //                          "jerry"
    //                      };

    // printf("1st way \n\n");

    // for(i = 0; i < 3; i++)
    // {
    //     printf("string = %s \t address = %u\n", ch_arr + i, ch_arr + i);
    // }


    // char input[5][100] = {"element0", "element2", "element4", "element6", "element8"};

    // int i;

    // for (i = 0; i < 5; ++i)
    // {
    //     printf("%s\n", input[i]);
    // }

    char fname[MAXCHAR];
    FILE *fptr = NULL; 
    int i = 0;
    int tot = 0;
    printf("\n\n Read the file and store the lines into an array :\n");
	printf("------------------------------------------------------\n"); 
	printf(" Input the filename to be opened : ");
	scanf("%s",fname);	
    int F_ROWS = count_file_len(fname);
    char line[F_ROWS][MAXCHAR];
    fptr = fopen(fname, "r");
    while(fgets(line[i], MAXCHAR, fptr)) {
        if (line[i][strlen(line[i])-1] == '0') {
            line[i][strlen(line[i])] = '\0';
            i++;
        }
        else {
            line[i][strlen(line[i])-1] = '\0';
            i++;
        }
    }
    tot = i;
	printf("\n The contents of the file %s  are : \n",fname);    
    for(i = 0; i < tot; ++i) {
        printf(" %s\n", line[i]);
    }
    printf("\n");

    return 0;
}
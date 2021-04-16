#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define MAXCHAR 50 // maximale länge der Zeilen + 5

#define LSIZ 45 

// char *lines_array (char *path) {
//     int MAX_FILE_ROWS = 550;
//     int i = 0;
//     int tot = 0;
//     char lines[MAX_FILE_ROWS][MAXCHAR];

//     scanf("%s", path);

//     FILE *file = fopen(path, "r");
//     while(fgets(lines[i], MAX_FILE_ROWS, file)) {
//         lines[i][strlen(lines[i]) - 1] = '\0';
//         i++;
//     }
    // for (int i = 0; i < MAX_FILE_ROWS; ++i) {
    //     printf(" %s\n", lines[i]);
    // }
    // printf("\n");
//     fclose(file);
//     return 0;
// }

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

int **matrix_sum(int matrix1[][3], int matrix2[][3]){
    int i, j;
    int **matrix3;
    matrix3 = malloc(sizeof(int*) * 3);
     
    for(i = 0; i < 3; i++) {
        matrix3[i] = malloc(sizeof(int*) * 3);
    }
 
    for(i = 0; i < 3; i++){
        for(j = 0; j < 3; j++){
            matrix3[i][j] = matrix1[i][j] + matrix2[i][j];
        }
    }
    return matrix3;
}

// void create_Array() {
//     char fname[50];
//     FILE *fptr = NULL; 
//     int i = 0;
//     int tot = 0;

// 	printf(" Input the filename to be opened : ");
// 	scanf("%s",fname);	
//     int F_ROWS = count_file_len(fname);
//     char line[F_ROWS][LSIZ];
//     fptr = fopen(fname, "r");
//     while(fgets(line[i], LSIZ, fptr)) {
//         if (line[i][strlen(line[i])-1] == '0') {
//             line[i][strlen(line[i])] = '\0';
//             i++;
//         }
//         else {
//             line[i][strlen(line[i])-1] = '\0';
//             i++;
//         }
//     }
//     tot = i;
// 	printf("\n The contents of the file %s  are : \n",fname);    
//     for(i = 0; i < tot; ++i)
//     {
//         printf(" %s\n", line[i]);
//     }
//     printf("\n");
//     return 0;
// }

// char dec_to_bin(dec_number) {


// }

int main() {

    // char path[] = "test_14.txt";
    
    // lines_array(path);
    // // char *p = lines_array(path);

    //--------------------------------------------//
	char fname[MAXCHAR];
    FILE *fptr = NULL; 
    int i = 0;
    int tot = 0;
    printf("\n\n Read the file and store the lines into an array :\n");
	printf("------------------------------------------------------\n"); 
	printf(" Input the filename to be opened : ");
	scanf("%s",fname);	
    int F_ROWS = count_file_len(fname);
    char line[F_ROWS][LSIZ];
    fptr = fopen(fname, "r");
    while(fgets(line[i], LSIZ, fptr)) {
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
    // for(i = 0; i < tot; ++i)
    // {
    //     printf(" %s\n", line[i]);
    // }
    printf("%s\n", line[1]);
    printf("\n");
    return 0;
}
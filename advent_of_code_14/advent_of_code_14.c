#include<stdio.h>
#define MAXCHAR 1000

// char *lines_array (int count, char *path) {

// }

int count_file_len(char *path) {
    FILE *fp;
    // char* filename = *path;
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

int main() {

    char path[] = "advent_of_code_14.txt";
    printf("%d\n", count_file_len(path));

    // FILE *fp;
    // char str[MAXCHAR];
    // char* filename = "test_14.txt";
    
    // fp = fopen(filename, "r");
    // if (fp == NULL){
    //     printf("Could not open file %s",filename);
    //     return 1;
    // }
    // while (fgets(str, MAXCHAR, fp) != NULL)
    //     printf("%s", str);
    // fclose(fp);
    return 0;
}
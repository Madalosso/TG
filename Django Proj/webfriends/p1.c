#include <stdio.h>

#define BUFSIZE 1000

int main(int argc, char **argv){

	if(argc!=2){
		printf("Entre com o nome do arquivo de entrada");
		return 0; 
	}

   FILE *fp = fopen(argv[1], "r"); /* "r" = open for reading */

    char buff[BUFSIZE]; /* a buffer to hold what you read in */

    /* read in one line, up to BUFSIZE-1 in length */
    while(fgets(buff, BUFSIZE - 1, fp) != NULL) 
    {
        /* buff has one line of the file, do with it what you will... */

        printf ("%s\n", buff); /* ...such as show it on the screen */
    }
	printf("LBLARLALBRLBLARBLARLBRLA");
    fclose(fp); /* close the file */ 
}

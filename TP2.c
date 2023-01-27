#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*TABLEAU STANDAR
ABDOULAYE DIOP 
P27 1207
Master 1 CCA*/
/*  je me suis basée sur ce code fait en cours C={0101,1011,1110,0000}  */
char *tableaustandar(char* code)
{
	int i,j,p;
	/*creation d'un tableau de chaine de caractere de 16lignes et d'une colonne*/char* mat[16]= {"0000","0101","1011","1110","1000","1101","0011","0110","0100","1111","0001","1010","0010","1001","0111","1100"};
	i=0;
	while(strcmp(&mat[i][0],code)!=0)
	{
	i++;   
	}
    p=((i+1)%4);
	if(p==0)
		  p=4;	
	printf("le mot est corrigé par: \n");
    puts(&mat[p-1][0]);
    return(&mat[p-1][0]);
}
int main()
{
	char* code;
	code=(char*)malloc(sizeof(char)*4);
	do/* si la saisie est incorrecte il vous dit de saisir a nouveau*/
	{
	 	printf("donner un mot de code de longueur 4  \n");
	    gets(code);
		
	} while (strlen(code)!=4);
	char* chaine;
	chaine=(char*)malloc(sizeof(char)*4);
    chaine=tableaustandar(code);
}

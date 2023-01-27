#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*ABDOULAYE DIOP 
P27 1207
Master 1 CCA*/
int puissance(int x, int n)/*calcul de puissance d'un nombre */
{
    int i, p=1;

    for(i=0; i<n; i++)
    p*=x;

    return p;
}
int nombrechiffre(int n) /* Fonction me permet de savoir  le nombre de bits necessaire pour la conversion d'un entier donné */
  {
  int p=0;
  while (n!=0){
    p++;
    n=n/2;
  }
  return p;
}
int ascii(char c) 
{
    return (int)(c);
}
int** haming1(int r, int *nc)           /*fonction retournant une matrice de r lignes et de nc colonnes*/
{
    int l,nbr,taille,x,k,i,j,nt,p;
    int*t;int**tab; int **mat;
    p=(puissance(2,r)-1);
    *nc=p;
    tab= (int**)malloc(sizeof(int*)*p);
    for(j=0;j<p;j++)
       tab[j]=(int*)malloc(sizeof(int)*r);
     mat= (int**)malloc(sizeof(int*)*r);
    for(j=0;j<r;j++)
       mat[j]=(int*)malloc(sizeof(int)*p);
    
     k=0;
    for(i=1;i<=p;i++)
    {
          taille = nombrechiffre(p);
          t= (int*)malloc(sizeof(int)*taille);
          nbr=i;
          for(l=0; nbr !=0; l++)
            {
              t[l] = nbr%2;
              nbr = nbr/2;
             
            }
          nt=nombrechiffre(i);
         for (j=0;j<nt;j++)  /*remplissage d'une matrice de p lignes et de r colonnes */
         {
            tab[k][j]=t[j];
         }
         while(nt<r)/*ajout de 0 pour les nombres aui n'ont pas atteint r bits */
         {
          tab[k][nt]=0;
          nt++;
         }
         k++;
    } 
    for(i=0;i<r;i++) /*calcul de transposé de la matrice remplie*/
    {
      for(j=0;j<p;j++)
        mat[i][j]=tab[j][i];
    }
    for (i=0;i<r;i++)  /*affichage de la matrice */
     {
        for(j=0;j<p;j++)
         printf("%d ",mat[i][j]);
         printf("\n");
     } 
return mat;
}
int main()
{
  int n, r, i,j,p;
  int** matrice;
  printf("donner le parametre r: ");
  scanf("%d",&r);
  printf("\n");
  p=(puissance(2,r)-1);
  matrice= (int**)malloc(sizeof(int*)*p);
  for(j=0;j<p;j++)
    matrice[j]=(int*)malloc(sizeof(int)*r);
  matrice = haming1(r, &n);
  
  return 0;

}

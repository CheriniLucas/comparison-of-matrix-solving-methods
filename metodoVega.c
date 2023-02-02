#include <stdio.h>
#include <stdlib.h>

int main()
{
	//Metodo Vega, version

	//Determinacion de variables
	int i, j, k, x;
	float M[1][11][11] = {{{0,0,0,0,0,0,0,0,0,0,0}, {0,0,0,0,0,0,0,0,0,0,0}, {0,0,0,0,0,0,0,0,0,0,0}, {0,0,0,0,0,0,0,0,0,0,0}, {0,0,0,0,0,0,0,0,0,0,0}, {0,0,0,0,0,0,0,0,0,0,0}, {0,0,0,0,0,0,0,0,0,0,0}, {0,0,0,0,0,0,0,0,0,0,0}, {0,0,0,0,0,0,0,0,0,0,0}, {0,0,0,0,0,0,0,0,0,0,0}, {0,0,0,0,0,0,0,0,0,0,0}}};
	float X[1];

	system("clear");
	printf("Bienvenido a Metodo Vega\nPor favor, ingrese la cantidad de variables a determinar (max 10):\t");
	scanf("%d", &x);
	fflush(stdin);

	system("clear");
	printf("\t\tMetodo Vega\nIngrese los datos respetando el orden por filas:\n");
	for (int i = 0; i < x; ++i)
	{
		for (int j = 0; j < x+1; ++j)
		{
			scanf("%f", &M[0][i][j]);
			fflush(stdin);
		}
		printf("\n");
	}
	system("clear");

	//Ejecucion de calculos
	for (int k = 1; k < x; ++k)
	{
		for (int i = 0; i < x; ++i)
		{
			for (int j = 0; j < x+1; ++j)
			{
				M[k][i][j] = M[k-1][0][0] * M[k-1][i+1][j+1] - M[k-1][i+1][0] * M[k-1][0][j+1];
			}
		}
	}

	for (int i = x; i > 0; --i)
	{
		X[i] = (M[i-1][0][x-i+2] - M[i-1][0][1] * X[2] - M[i-1][0][2] * X[3] - M[i-1][0][3] * X[4] - M[i-1][0][4] * X[5] - M[i-1][0][5] * X[6] - M[i-1][0][6] * X[7] - M[i-1][0][7] * X[8] - M[i-1][0][8] * X[9] - M[i-1][0][9] * X[10])/M[i-1][0][0];
	}

	//Muestra de resultados
	printf("\t\tMETODO VEGA\n\nLas matrices quedan:\n\n");
	for (int k = 0; k < x; ++k)
	 {
	 	for (int i = 0; i < x; ++i)
	 	{
	 		for (int j = 0; j < x+1; ++j)
	 		{
	 			printf("%.2f\t\t", M[k][i][j]);
			}
			printf("\n\n");
		}
		printf("\n\n\n");
	 }
	 printf("Finalmente las variables son:\n");
	 for (int i = 1; i <= x; ++i)
	 {
	 	printf("\tx%d:\t%.2f\n", i, X[i]);
	 }

	return 0;
}

//9 programa
//Marlon Emiliano Olvera Gallegos
//28-05-25
//código que permite capturar 10 valores numéricos(puede ser negativo, positivo, decimal) 
//y posteriormente los ordena en un arreglo de manera ascendente y los imprime en la pantalla
#include <conio.h>
#include <stdio.h>

int main() {
    double numeros[10];
    int i, j;
    
    printf("Ingrese 10 valores numericos (pueden ser decimales, positivos o negativos):\n");
    for(i = 0; i < 10; i++) {
        printf("\nValor %d: ", i + 1);
        scanf("%lf", &numeros[i]);
    }
    
    for(i = 0; i < 9; i++) {
        for(j = 0; j < 9 - i; j++) {
            if(numeros[j] > numeros[j + 1]) {
                double temp = numeros[j];
                numeros[j] = numeros[j + 1];
                numeros[j + 1] = temp;
            }
        }
    }
    
    printf("\nValores ordenados de forma ascendente:\n");
    for(i = 0; i < 10; i++) {
        printf("%.2f\n", numeros[i]);
    }
    
    getch();
}

//2 programa 
//Marlon Emiliano Olvera Gallegos
//9-05-25
//Calcula el perimetro o el area del circulo con clase
#include <stdio.h>
#include <conio.h>
#include <math.h>

class Circulo{
public:
    float radio;
    
    float perimetro() {
        return 2 * M_PI * radio;
    }
    
    float area() {
        return M_PI * radio * radio;
    }
};

int main() {
    Circulo c;
    char opcion;
    
    printf("Seleccione 'p' para perimetro o 'a' para area: ");
    opcion = getchar();
    
    printf("Ingrese el radio: ");
    scanf("%f", &c.radio);
     
    switch(opcion) {
        case 'p':
        printf("El perimetro del circulo es: %.2f", c.perimetro());
        break;
        case 'a':
        printf("El area del circulo es: %.2f", c.area());
        break;
        default:
        printf("Opcion invalida");
    }
    
    getch();
}

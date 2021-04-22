#include <stdio.h>

float main(void) {
	float a;
	float b;
	float c;

	printf("Ingrese el valor a: ");  
	scanf("%f", &a);
	printf("Ingrese el valor b: ");  
	scanf("%f", &b);
	c = a+b;
	printf("La suma es: %f\n", c);
	return 0;
}

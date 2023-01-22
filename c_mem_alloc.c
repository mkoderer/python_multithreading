#include <stdio.h>
#include <stdlib.h>

typedef struct  {
	int num;
	char ch;
} myStruct;


int main() {
	myStruct *m =  malloc(sizeof(myStruct));
	m->num = 5;
	m->ch = 'A';
	free(m);
	exit(0);
}

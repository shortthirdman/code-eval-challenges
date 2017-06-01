#include <stdio.h>

int main(int argc, char *argv[]) {
	FILE *fp;
	unsigned a;

	if (argc != 2) {
		printf("Usage: %s [FILE]\n", argv[0]);
		return 1;
	}
	fp = fopen(*++argv, "r");
	while (fscanf(fp, "%d", &a) != EOF)
		printf("%d\n", __builtin_popcount(a));
	return 0;
}

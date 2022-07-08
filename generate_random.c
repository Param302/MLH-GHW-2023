#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
#include <math.h>

long random_no(void);

int main(int n, char *argv[])
{
    if ((n < 2) || (n > 3)) {
        printf("Invalid arguments passed\ntype:\tgenerate_random --h for help\n");
        return 1;
    }
    printf("%i\n", n);
    printf("%s, %s\n", argv[0], argv[1]);
    if (n == 2) {
        printf("Help generate_random\nUsage: \n\tgenerate_random -h\n\t\tHelp genearte_random\n\tgenerate_random -n n\n\t\tn is no. of random numbers to be generated.\nn should be a positive number.\n");
        return 0;
    }

    int nos = atoi(argv[2]);
    if (nos == 0)
    {
        printf("n should be a positive number, you have passed `%i`\n", nos);
        return 2;
    }

    printf("Total number of random numbers: %i\n", nos);
    for (int i = 1; i <= nos; i++)
    {
        printf("Random no. %i\t%li\n", i, random_no());
        Sleep(1000);
    }
    return 0;
}

long random_no(void)
{
    time_t seconds;
    seconds = time(NULL);
    int s1 = seconds / 3;
    int s2 = seconds / 2;
    return abs((seconds % 2) ? seconds * s1 : seconds * s2);
}
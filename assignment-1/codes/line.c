#include <stdio.h>
#include <math.h>

int main() {
    // Direction ratios
    double a = 6.0, b = 2.0, c = 3.0;

    // Calculate the magnitude
    double magnitude = sqrt(a * a + b * b + c * c);

    // Calculate direction cosines
    double l = a / magnitude;
    double m = b / magnitude;
    double n = c / magnitude;

    // Output the results to a file
    FILE *file = fopen("output.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    fprintf(file, "Direction Cosines:\n");
    fprintf(file, "l = %lf\n", l);
    fprintf(file, "m = %lf\n", m);
    fprintf(file, "n = %lf\n", n);
    
    fclose(file);
    return 0;
}


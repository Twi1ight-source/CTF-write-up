#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int driver(char flag[], long long vecto[], int times);
int multi(long long matrix[3][3], long long vecto[]);
long long scalar(long long v1[], long long v2[]);


int main() {
    char flag[22]="dctf{@UuZZj'^8:Y5Wbj5}";
    unsigned long long vecto[3]={4677356919945ULL, 3064867953928ULL, 5592055376297ULL};
    int times=25;

    driver(flag, vecto, times);
    puts(flag);
}
int driver(char flag[],long long  vecto[], int times) {
    for (int i=times; i>0; i--) {
        decrypt(flag,vecto);
        long long inv[3][3]={
            {1,2,-2},
            {2,1,-2},
            {-2,-2,3}
        };

        multi(inv, vecto);

        for (int i=0;i<3;i++) {
                if (vecto[i]<0) {
                    vecto[i]*=-1;
                }
        }

        printf("[%llu, %llu, %llu],\n", vecto[0], vecto[1], vecto[2]);

    }
}

int multi(long long matrix[3][3], long long vecto[]) {
    long long result[3];
    for (int i =0;i<3;i++) {
        result[i]= scalar(matrix[i], vecto);
    }
    for (int j=0;j<3;j++) {
            vecto[j]=result[j];
    }
    return 0;
}

long long scalar(long long v1[], long long v2[]) {
    long long  sum=0;
    for (int i=0;i<3;i++) {
            sum+=v1[i] * v2[i];
    }
    return sum;
}

int decrypt(char flag[], long long vector[]) {
    for (int i=5;i<strlen(flag)-1;i++) {
        int mic = vector[i%3] % 95;

        int chr = flag[i];
        chr -= mic;
        if (chr < 32) {
            chr += 95;
        }
        flag[i] = chr;
    }
    return 0;
}








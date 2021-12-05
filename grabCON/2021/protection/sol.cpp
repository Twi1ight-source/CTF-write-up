#include <stdint.h>
#include <iostream>

uint32_t arr[8] = {
    0xDEADBEEF,
    0xB105F00D,
    0xDEAD2BAD,
    0xFEEDC0DE,
    0xC00010FF,
    0x0D15EA5E,
    0xCAFED00D,
    0xBAD22222,
};

uint32_t rol(uint32_t value, unsigned int count) {
    return value >> count | value << (32 - count);
}

uint32_t ror(uint32_t value, unsigned int count) {
    return value << count | value >> (32 - count);
}

uint32_t func(uint32_t a1, uint32_t a2){
    return ((a1-a2) ^ ((a1+a2)<<8) ^ ((a1+a2)>>0xf));
}
void updateKey(int a)
{
    uint32_t x1=((arr[1]&0xf)<<1);
    uint32_t x2=((arr[3]&0xf0)>>4);
    uint32_t x3=((arr[5]&0xf)<<1);
    uint32_t x4=((arr[7]&0xf0)>>4);

    uint32_t y1 = ((rol(arr[0], x1) + ror(arr[1], x2)) ^ (rol(arr[2], x3) + ror(arr[3], x4)));
    uint32_t y2 = ((rol(arr[4], x1) + ror(arr[5], x2)) ^ (rol(arr[6], x3) + ror(arr[7], x4)));

    arr[(a + 0) % 8] = (y1 + y2);
    arr[(a + 2) % 8] = (y1 | y2);
    arr[(a + 4) % 8] = (y1 - y2);
    arr[(a + 6) % 8] = (y1 & y2);
}

int main()
{
	uint32_t keys[15][16]{};

    for (int i = 0; i < 15; i++) {
        for (int j = 0; j < 16; j++) {
            updateKey(j);
            keys[i][j] = arr[j % 8];
        }
    }

    uint32_t check[] = {0x1565560d, 0x9a37177f, 0x4baf7822, 0x49c476b8, 0x36515199, 0x1112c40f, 0x11b9e7ac, 0x77697b72, 0x7def0a5c, 0x6a5da2f9, 0xef0afefc, 0x01f46cec, 0xe5364262, 0x7ca1eb57, 0xbc83bf53, 0xef5e1120};

    for (int i = 14; i >= 0; --i) {
        uint32_t a = check[i];
        uint32_t b = check[i+1];
        for (int j = 15; j >= 0; --j) {
            uint32_t x = keys[i][j];
            b -= func(x,a);
            a -= func(x,b);
        }
        check[i] = a;
        check[i+1] = b;
    }
    uint8_t* flag = (uint8_t*) check;

    for (int i=0;i<16;i++) {
        std::cout<<check[i]<<std::endl;
    }
    std::cout << flag << std::endl;
    return 0;
}

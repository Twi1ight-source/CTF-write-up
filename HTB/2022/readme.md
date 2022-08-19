## Indefinite

### Đây là một bài ptrace

Cụ thể là gồm 2 luồng riêng biệt cha và con trong đó cha điều khiển luồng của con

### Hàm tracer (cha)

![image](https://user-images.githubusercontent.com/84214843/185588007-d1bf19a8-64c0-42d6-8704-c1f4742eb750.png)

### Cơ bản nó check 2 byte đầu là UD2 và zlib decompress từ byte thứ 8 trở đi khi chạy chương trình -> decrypt bằng IDA python.

### Hàm encryt sau khi decrypt code:

![image](https://user-images.githubusercontent.com/84214843/185588106-ccb899d6-4359-493e-be85-33dbae714735.png)


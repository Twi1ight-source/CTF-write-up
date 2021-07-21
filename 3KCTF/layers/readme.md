Bài này được obfucated dùng LLVM, mình dùng một tool để deobfucated (https://github.com/mrT4ntr4/MODeflattener) ra được file layers.pacthed

Sau khi deobfucated thì hàm main cơ bản là như vầy:

![1](https://user-images.githubusercontent.com/84214843/126470734-246f81ab-9f95-48cc-af30-d721482b8ef3.png)
![2](https://user-images.githubusercontent.com/84214843/126470753-c8553a40-eada-4f5d-8dd3-094ccb5688c6.png)

+Cơ bản là hàm main sử dụng tổng các char của input(sub_400DA0) như seed trong srand() 

+Rồi sau đó input được encrypted bằng hàm sub_403D00() và tiếp tục encrypted với sub_400880() và cuối cùng được so sánh với byte_605090

+Qua phân tích thì hàm sub_400880() là TEA encryption (sử dụng một hằng số là 0x61c88647 và phân tích các biến đổi dựa trên biểu thức sau: ~x&y | ~y&x = x^y )

+còn hàm còn lại quá phức tạp nên không phân tích luôn (đọc wu mới biết là serpent cipher)

-->Với TEA encryption thì có thể kiếm được decrypt một cách trên wikipedia

![1](https://user-images.githubusercontent.com/84214843/126472229-22440278-50ea-4f6d-9c9c-9d2967c36418.png)

-->Còn serpent cipher thì đọc wu mới biết người ta làm template để decrypt luôn (https://github.com/aaruel/Serpent-Implementation/tree/master/Serpent%20--%20C) dùng serpent_decrypt_bitslice() trong đó 

-->Giờ thì viết script để brute-force seed và decrypt ngược lại hai hàm để ra flag



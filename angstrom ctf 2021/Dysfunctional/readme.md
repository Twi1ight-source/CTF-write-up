Load vào IDA

Hàm main:

![1](https://user-images.githubusercontent.com/84214843/120740938-5f178600-c51e-11eb-88d9-7c4d253e2338.png)

Sau 1 hồi phân tích thì mình ghi lại chức năng của mỗi hàm cơ bản như trong comments trên IDA

Recap lại chương trình 1 chút:

+Đầu tiên nó sẽ đọc file flag của mình và data từ file not_flag(Sbox)
+Sau đó flag lần lượt đi qua 6 hàm như các bạn thấy đó (closure1 ,closure2, comp1, comp2, map1 ,map2) và map2 là hàm encrypt cuối cùng để xuất kết quả như chúng ta đã thấy

-->Mục tiêu của chúng ta là tìm flag sao cho khi chương trình encrypt thì được các số như trong file đề cho

Mình viết lại nguyên cái chương trình bằng python:

![1](https://user-images.githubusercontent.com/84214843/120741564-730fb780-c51f-11eb-98e5-c6baf27c948c.png)
![2](https://user-images.githubusercontent.com/84214843/120741575-773bd500-c51f-11eb-8f31-a7b2bf21692b.png)

Solution:

Mình viết một script đảo ngược lại hết các hàm để từ enc_flag ==> flag (sol.py)







đây là một binary viết bằng golang

load vào IDA xem thử, vì nó viết bằng golang nên IDA không xác định được chính xác hàm main là chỗ nào
vì thế nên ta phải phân tích bằng tay để xác định hàm main

Kiểm tra strings ta thấy một số string quan trọng như: (Hello from ARM64, congratulation you did it!), ta có thể chắc chắn 
rằng đây là những strings của hàm main

Tình cờ mình tìm được một hàm nhận những strings đó (sau khi điên cuồng dùng c(make code) để analyze những data trong binary)
đó là tại địa chỉ 0x401584
![401584](https://user-images.githubusercontent.com/84214843/118347039-4f81ce80-b56a-11eb-8619-70644bc9db28.png)

 giờ chỉ việc sau đó bấm P để define function rồi F5 để xem mã giả C thôi :))
 
 ![113](https://user-images.githubusercontent.com/84214843/118347072-94a60080-b56a-11eb-8eb6-fb30b6ecf774.png)
 
Và đây chính là hàm main mà chúng ta sẽ phân tích
Phân tích nhanh ta thấy được input ta đưa vào là v4[i], sau đó được encoded thông qua hàm sub_401328 và output sẽ được so sánh 
với qword_50E010

đây là hàm encrypted(sub_401328):
![113](https://user-images.githubusercontent.com/84214843/118347821-3f6ced80-b570-11eb-9a01-e284eb2614a4.png)
![114](https://user-images.githubusercontent.com/84214843/118347824-472c9200-b570-11eb-966f-750c57c2247e.png)

Output sẽ được so sánh với qword_50E010:
![113](https://user-images.githubusercontent.com/84214843/118347862-704d2280-b570-11eb-8a93-e5829ae34a6f.png)

Vậy bây giờ ta chỉ cần extract thuật toán trong hàm encrypted rồi bruteforce để tìm flag thôi :)) ez













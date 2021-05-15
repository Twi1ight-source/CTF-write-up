đây là một binary viết bằng golang

load vào IDA xem thử, vì nó viết bằng golang nên IDA không xác định được chính xác hàm main là chỗ nào
vì thế nên ta phải phân tích bằng tay để xác định hàm main

Kiểm tra strings ta thấy một số string quan trọng như: Hello from ARM64, congratulation you did it!, ta có thể chắc chắn 
rằng đây là những strings của hàm main

Tình cờ mình tìm được một hàm nhận những strings đó (sau khi điên cuồng dùng c(make code) để analyze những data trong binary)
đó là tại địa chỉ 0x401584





